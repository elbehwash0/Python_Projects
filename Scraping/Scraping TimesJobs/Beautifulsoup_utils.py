from bs4 import BeautifulSoup
import requests

def get_job_info(html):
    """
    Extract job details from the provided HTML using BeautifulSoup.
    Returns a dictionary with company name, posted date, job description,
    skills, locations, and salary.
    """
    soup = BeautifulSoup(html, "lxml")

    company_name = soup.find('h2').text.strip()

    ul_element = soup.find('ul', class_='top-jd-dtl d-flex mt-8')
    years_of_experince = ul_element.find('li').text.strip().replace('\n', '').replace(' ', '').replace('\t', '').replace('to', ' - ')

    skills_elements = soup.find_all('span', class_='jd-skill-tag')
    skills = [skill.text.strip() for skill in skills_elements]

    locations = []
    location_tag = soup.find('span', class_='job-location-trunicate')
    locations = location_tag.text.split(", ")


    li_elements = ul_element.find_all('li')
    if len(li_elements) > 1:
        salary = li_elements[1].text.strip()

    return {
        'Company Names': company_name,
        'Years of experience': years_of_experince,
        'Skills': skills,
        'Locations': locations,
        'Salaries': salary
        #'Links': in selenium script
    }
