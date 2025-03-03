from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from Beautifulsoup_utils import get_job_info
from csv_Handler import csv_appender

# Constants
CHROMEDRIVER_PATH = r"D:\mozakra\Python\chromedriver-win64\chromedriver-win64\chromedriver.exe"
JOB_SEARCH_URL = (
    "https://www.timesjobs.com/candidate/job-search.html?"
    "searchType=personalizedSearch&from=submit&searchTextSrc=as&"
    "searchTextText=Python&txtKeywords=Python%2C&txtLocation="
)
NUM_NAME = 1
POPUP_FLAG = True
SCROLL_STEP = 290
MAX_SCROLL = 8000
WAIT_TIME = 10
NUM_PAGES_TO_TRAVERSE = 10  # Traverses the last 10 pagination elements


def init_driver() -> webdriver.Chrome:

    #Initializes and returns a Chrome driver instance.

    print("Initializing driver...")
    service = Service(executable_path=CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service)
    driver.get(JOB_SEARCH_URL)
    print("driver has been initialized ✅")
    return driver


def accept_initial_popups(driver: webdriver.Chrome) -> None:

    #Accepts any initial popup windows or cookie messages.

    # Wait for and click the close button for the first popup
    close_button = WebDriverWait(driver, WAIT_TIME).until(
        EC.element_to_be_clickable(
            (
                By.XPATH, "/html/body/div[2]/div[1]/table/tbody/tr/td[2]/div/span",
            )
        )
    )
    close_button.click(); print("Popup Closed successfully✅")

    # Wait for and click the cookie OK button
    cookie_ok_button = WebDriverWait(driver, WAIT_TIME).until(
        EC.element_to_be_clickable(
            (
                By.XPATH, "//*[@id='site']/div[6]/div/div[2]/button"
            )
        )
    )
    cookie_ok_button.click(); print("Cookies accepted✅")


def accept_page_popup(driver: webdriver.Chrome) -> None:
    """
    Accepts popups in the first applying page
    """
    global POPUP_FLAG
    if(POPUP_FLAG):
        no_button = WebDriverWait(driver, WAIT_TIME).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH, '/html/body/div[1]/div[6]/div[1]/div[2]/div[6]/div/div[1]/a[2]'
                )
            )
        )
        no_button.click(); print("Popup Closed successfully✅")
        POPUP_FLAG = False


def Page_Scrapper(driver: webdriver.Chrome) -> None:
    """
    Scrap the current page
    """
    print("Scrapping current page...")
    sleep(3)
    global NUM_NAME
    current_job_link = driver.current_url

    accept_page_popup(driver)

    html_text = driver.page_source
    job_info = get_job_info(html_text); print("Extracting job info...")
    job_info.update({"Links": current_job_link})
    print("Page has been scrapped successfully✅")
    sleep(0.3)

    print("Appending the data to csv file...")
    sleep(0.3)
    csv_appender(f"{str(NUM_NAME)}", job_info)



def scroll_and_click_buttons(driver: webdriver.Chrome) -> None:
    """
    Finds job listing buttons and clicks through them,
    scrolling the page with each interaction.
    """
    open_buttons = driver.find_elements(
        By.XPATH, "/html/body/div[1]/div[5]/section/div[2]/div[2]/ul/li[a]"
    )

    for scroll_y, button in zip(range(SCROLL_STEP, MAX_SCROLL, SCROLL_STEP), open_buttons):
        print("Opening the new job page...")
        sleep(1)
        button.click()

        # Handle and Scrap the new tab(page): switch, accept popup, scrap, close it, then switch back to the main window.
        if len(driver.window_handles) > 1:
            driver.switch_to.window(driver.window_handles[1])
            Page_Scrapper(driver)
            driver.close(); print("Returned to the main page")
            sleep(1)
            driver.switch_to.window(driver.window_handles[0])
        driver.execute_script("window.scrollTo(0, arguments[0]);", scroll_y)
        print("Page has been scrolled successfully✅")
        sleep(0.5)



def traverse_pages(driver: webdriver.Chrome) -> None:
    """
    Loops over a subset of pagination elements to click through them.
    """
    # Find the pagination container and its <em> tags
    pagination_container = driver.find_element(
        By.XPATH, '//*[@id="searchResultData"]/div[4]'
    )
    page_elements = pagination_container.find_elements(By.TAG_NAME, "em")
    num_pages = len(page_elements)

    # Traverse the last NUM_PAGES_TO_TRAVERSE pagination elements
    for page_index in range(max(0, num_pages - NUM_PAGES_TO_TRAVERSE), num_pages):

        global NUM_NAME
        scroll_and_click_buttons(driver)
        NUM_NAME = NUM_NAME + 1

        # Click the pagination element after waiting for it to be clickable
        page_button = WebDriverWait(driver, WAIT_TIME).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    f"//*[@id='searchResultData']/div[4]/em[{page_index + 1}]",
                )
            )
        )
        page_button.click()

        # Scroll to the top after clicking the page button
        driver.execute_script("window.scrollTo(0, 0);")
        sleep(1)


def main():
    start_script = input("Enter s to start executing the script: ")
    if start_script.lower() == "s":
        driver = init_driver()
        try:
            accept_initial_popups(driver)

            while True:
                traverse_pages(driver)

        except Exception as e:
            print("An error occurred:", e)
        finally:
            driver.quit()


if __name__ == "__main__":
    main()