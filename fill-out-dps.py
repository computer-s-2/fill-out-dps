from selenium import webdriver
from selenium.webdriver.chrome.options import Options


import time


import winsound


frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second


date = ""


x = 1
count = 0


c_date = 12282021




chrome_options = Options()


# incognito window


chrome_options.add_argument("--headless")


while x != 0 or count != 10000:
    browser = webdriver.Chrome(executable_path = "C://Users/Dell/Desktop/py4e/chromedriver.exe",options = chrome_options)
    # browser.switch_to.window(browser.current_window_handle)
    browser.get("https://public.txdpsscheduler.com/")
    browser.implicitly_wait(10)
    languageQuestion = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div/div/div[2]/button[1]')
    languageQuestion.click()


    time.sleep(3)