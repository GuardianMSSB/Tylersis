from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome(executable_path=r"C:\Users\abdel\Downloads\chromedriver_win32\chromedriver.exe")
browser.get('https://sdm.sisk12.com/RP360x3/login')
time.sleep(5)

student = browser.find_element_by_id("mat-tab-label-0-2")
student.click()


username = browser.find_element_by_id("txtUserName")
username.clear()
username.send_keys("g.abdelgawad547")

password = browser.find_element_by_id("txtPassword")
password.clear()
password.send_keys("rp215207")
password.send_keys(Keys.RETURN)

