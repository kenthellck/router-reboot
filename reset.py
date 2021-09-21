print('Router change time script Initiated...')

#Importing the helper libraries
from selenium import webdriver
from selenium.webdriver.common import keys
import time
import datetime
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Setting the chromepath
PATH= "C:\chromedriver.exe"
driver=webdriver.Chrome(PATH)

#Printing the script start
time_now=datetime.datetime.now()
print(time_now.strftime("%m/%d/%Y, %H:%M:%S")+' Router change time script Started...')

#Get the current IP and append to file
public_ip=requests.get('https://api.ipify.org').text
print('The current IP: '+public_ip)
file = open("change.log", "a")
file.write(time_now.strftime("%m/%d/%Y, %H:%M:%S")+" ::Current IP: "+public_ip + "\n")
file.close()
time.sleep(1)
#Rebooting the router
driver.get("http://192.168.1.1")

username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")
btn_login = driver.find_element_by_name("loginBT")

username.send_keys("admin")
password.send_keys("admin")
btn_login.click()

time.sleep(2)
driver.find_element_by_id("Advance").click()
time.sleep(5)
driver.find_element_by_link_text("Maintenance").click()
driver.find_element_by_link_text("Reboot Device").click()
#Switchinng to IFrame
driver.switch_to.frame("mainFrame")
#Hit reboot
driver.find_element_by_id("do_reboot").click()
WebDriverWait(driver, 10).until(EC.alert_is_present())
driver.switch_to.alert.accept()
print('Router Rebooting...')

#Put script to sleep until the router is back
time.sleep(170)
print('Router Reboot Completed')

#Get the New IP and append to file
public_ip=requests.get('https://api.ipify.org').text
time_now=datetime.datetime.now()
print('The New IP: '+public_ip)
file = open("change.log", "a")
file.write(time_now.strftime("%m/%d/%Y, %H:%M:%S")+" ::New IP: "+public_ip + "\n" + "\n")
file.close()

#Quitting the script
driver.quit()
print(time_now.strftime("%m/%d/%Y, %H:%M:%S")+' Router change time script Stopped...')