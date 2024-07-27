
# Appiontment Checker Script

This script constantly checks for available appointments on the Texas DPS scheduling website to get a driver's permit. It automates the process of filling in personal details and checking for new appointments using Selenium WebDriver.

## Prerequisites
- Python 3.x installed
- Selenium installed (pip install selenium)
- ChromeDriver downloaded and placed in a known directory

## Setup
1. Download ChromeDriver:
- Download the version of ChromeDriver that matches your version of Google Chrome from [here](https://developer.chrome.com/docs/chromedriver/downloads).
- Place the chromedriver.exe file in a directory of your choice, e.g., C://Users/Dell/Desktop/py4e/.
2. Install Selenium:

Open a terminal or command prompt and run:

```bash
  pip install selenium
```
## Configuration
1. Update Personal Details:

- Replace ** in the dob and ssn fields with your actual date of birth and the last 4 digits of your Social Security Number, respectively.
- Update all the other personal information: name, email, zipcode
2. Adjust ChromeDriver Path:

- Ensure the path to chromedriver.exe is correct. Modify this line if necessary:
```python
    browser = webdriver.Chrome(executable_path="C://Users/Dell/Desktop/py4e/chromedriver.exe", options=chrome_options)
```
## Script Details
- Browser Configuration:
    - Runs Chrome in headless mode (no UI) for efficiency.
- Automation Steps:
    - Navigates to the DPS scheduling website.
    - Fills in personal details.
    - Clicks through various buttons to check for new appointment slots.
    - Plays a beep sound if an available appointment is found.
- Rechecking Frequency:
    - The script waits 7.5 minutes (450 seconds) between checks to avoid overwhelming the server.
## Usage

Monitor the console output for status updates. The script will print "not cool" with a count of attempts and "woah" if an available appointment is found.

## Troubleshooting
- No Appointments Found:

    - Ensure your personal details are correctly filled in.
    - Increase the script's sleep time if appointments are not appearing as expected.
- Browser Errors:

    - Make sure the ChromeDriver version matches your installed Google Chrome version.
    - Update ChromeDriver if needed.