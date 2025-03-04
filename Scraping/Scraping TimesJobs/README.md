# Scraping TimesJobs

Scraping TimesJobs is a web scraping project designed to extract job listings from the TimesJobs website. The project utilizes Python, BeautifulSoup, and Selenium to navigate through job postings, handle dynamic content, and extract relevant job details such as company names, years of experience required, skills, locations, salaries, and job links. The extracted data is then stored in CSV files for further analysis.

## Table of Contents

1. [Overview](#overview)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Configuration](#configuration)
5. [Legal and Ethical Considerations](#legal-and-ethical-considerations)
6. [Future Improvements](#future-improvements)
7. [Contact](#contact)

## Overview

This project automates the process of scraping job postings from the TimesJobs website. It consists of three main Python modules:

- **Beautifulsoup_utils.py**: Extracts job details from HTML content using BeautifulSoup.
- **csv_Handler.py**: Appends the scraped job data to CSV files.
- **Selenium_scrapper.py**: Drives a Chrome browser using Selenium to navigate pages and handle dynamic content.

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Google Chrome (with the corresponding ChromeDriver)

### Dependencies

Ensure you have the required dependencies installed. If you haven't already, install them using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/elbehwash0/Python_Projects.git
   ```
   Navigate to the Scraping TimesJobs Directory:

   ```bash
   cd Python_Projects/Scraping/Scraping\ TimesJobs
   ```
   
2. Ensure that the `CHROMEDRIVER_PATH` variable in `Selenium_scrapper.py` points to your local ChromeDriver executable location.

3. In `csv_Handler.py`, modify the `csv_path` variable to specify your desired output folder. **By default, it is set to a specific local path and must be changed to run successfully on your system.**

## Usage

Run the main script:

```bash
python Selenium_scrapper.py
```

The script will prompt you to input "s" to start executing. It will then navigate through job listings, scrape job details, and save the data to CSV files.

### Output

The extracted job data will be saved in the specified output folder as multiple CSV files named according to the page number.

### Example CSV Format

The output CSV file will have the following columns:

```csv
Company Names, Years of experience, Skills, Locations, Salaries, Links
ABC Corp, 2+ years, Python, Data Analysis, Remote, $70,000, https://example.com/job123
XYZ Ltd, 3-5 years, Java, Spring Boot, New York, $85,000, https://example.com/job456
```

Each page scraped will generate a new CSV file named `pageX.csv` (where X is the page number).

## Configuration

- **CHROMEDRIVER_PATH**: Update this variable in `Selenium_scrapper.py` with the correct path to your ChromeDriver.
- **CSV file output path**: Change the `csv_path` variable in `csv_Handler.py` to match your system's directory structure.

## Legal and Ethical Considerations

Before using this scraper, please ensure that you comply with the Terms of Service of the TimesJobs website. Web scraping can have legal implications, and it is important to use this tool responsibly. Avoid overwhelming the website with requests and consider reaching out to the website owner if you plan extensive data extraction.

## Future Improvements

- Enhance error handling and logging.
- Implement asynchronous scraping for efficiency.
- Expand support to additional job listing websites.
- Integrate proxy and user-agent rotation.
- Introduce a configuration file for dynamic settings.
- Develop a simple GUI for user-friendly interaction.

## Contact

For questions or suggestions, feel free to reach out:

- Email: [abdullah.mohamed.9511@gmail.com](mailto:abdullah.mohamed.9511@gmail.com)
- GitHub: [elbehwash0](https://github.com/elbehwash0)
