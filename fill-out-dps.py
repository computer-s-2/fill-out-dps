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


    first_name = browser.find_element_by_xpath('/html/body/div[1]/div/main/div/div/section/div/main/div/section/div[2]/div/div/form/div[2]/div[3]/div[2]/div/div[1]/div/input')
    first_name.send_keys("Sachi")
    time.sleep(.25)
    last_name = browser.find_element_by_xpath('/html/body/div[1]/div/main/div/div/section/div/main/div/section/div[2]/div/div/form/div[2]/div[3]/div[3]/div/div[1]/div/input')
    last_name.send_keys("Goel")
    time.sleep(.25)
    dob = browser.find_element_by_xpath('/html/body/div[1]/div/main/div/div/section/div/main/div/section/div[2]/div/div/form/div[2]/div[3]/div[4]/div/div[1]/div[1]/input')
    dob.send_keys("**") # Replaced actual birthday value
    time.sleep(.25)
    ssn = browser.find_element_by_xpath('/html/body/div[1]/div/main/div/div/section/div/main/div/section/div[2]/div/div/form/div[2]/div[3]/div[5]/div/div[1]/div[1]/input')
    ssn.send_keys("**") # Replaced actual last 4 digits of ssn
    time.sleep(3)


    submit = browser.find_element_by_xpath('/html/body/div[1]/div/main/div/div/section/div/main/div/section/div[2]/div/div/form/div[2]/div[4]/button')
    submit.click()
    print("submit")


    time.sleep(.25)


    new_app = browser.find_element_by_xpath('/html/body/div[1]/div/main/div/div/section/div/main/div/section/div[2]/div/div/div[3]/div/button')
    new_app.click()
    time.sleep(.25)
    ok = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[2]/button')
    ok.click()
    time.sleep(.25)


    renew_dl = browser.find_element_by_xpath('/html/body/div[1]/div[2]/main/div/div/section/div/main/div/section/div[2]/div/main/div/div/div[1]/div[2]')
    renew_dl.click()
    time.sleep(.25)
    email = browser.find_element_by_xpath('/html/body/div[1]/div[2]/main/div/div/section/div/main/div/section/div[2]/div/form/div/div[1]/div/div[5]/div/div/div/div[1]/div/input')
    email.send_keys("sachigoel27@gmail.com")
    time.sleep(.25)
    email_v = browser.find_element_by_xpath('/html/body/div[1]/div[2]/main/div/div/section/div/main/div/section/div[2]/div/form/div/div[1]/div/div[6]/div/div/div/div[1]/div/input')
    email_v.send_keys("sachigoel27@gmail.com")
    time.sleep(.25)
    zip = browser.find_element_by_xpath('/html/body/div[1]/div[2]/main/div/div/section/div/main/div/section/div[2]/div/form/div/div[2]/div[1]/div[4]/div[1]/div/div/div[1]/div[1]/input')
    zip.send_keys("75025")
    time.sleep(.25)
    next = browser.find_element_by_xpath('/html/body/div[1]/div[2]/main/div/div/section/div/main/div/section/div[2]/div/form/div/div[2]/div[2]/div/div[2]/button')
    next.click()
    time.sleep(.25)
    date = browser.find_element_by_xpath('/html/body/div[1]/div[2]/main/div/div/section/div/main/div/section/div[2]/div/div[1]/div/table/tbody/tr/td[3]').text
    date =  date.replace("/", "")
    date = date[-7:]
    print (date)


    if int(date) < 6302022:
        print ("woah")
        x = 0
        winsound.Beep(frequency, duration)
        break
    else:
        count = count + 1
        time.sleep(450)
        browser.close()
        print("not cool")
        print(count)