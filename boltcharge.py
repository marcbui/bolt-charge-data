#!/usr/bin/env python

#from six.moves import configparser
#from configparser import ConfigParser
import configparser
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

config = configparser.ConfigParser()
config.read("config.ini")

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(executable_path=os.path.abspath("/home/marcb/chromedriver"),
                          chrome_options=chrome_options)

driver.get("https://my.chevrolet.com/login")

user = driver.find_element_by_id("login_username")
passwd = driver.find_element_by_id("login_password")

print(config['default']['user'])
print(config['default']['passwd'])
user.send_keys(config['default']['user'])
passwd.send_keys(config['default']['passwd'])
driver.find_element_by_id("Login_Button").click()

timeout = 120
try:
    element_present = EC.presence_of_element_located((By.CLASS_NAME, 'status-box'))
    WebDriverWait(driver, timeout).until(element_present)
    print(driver.find_element_by_class_name("status-box").text)
    print(driver.find_element_by_class_name("status-right").text)
except TimeoutException:
    print("Timed out waiting for page to load")

print("Done!")
