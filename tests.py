#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from selenium import webdriver
import random
import time

AZ=[chr(i) for i in range(65,91)]
az=[chr(i) for i in range(97,123)]
n=[chr(i) for i in range(48,57)]

email=random.choice(AZ)+random.choice(az)+random.choice(n)+'@yandex.ru'
nickname=random.choice(AZ)+random.choice(az)+random.choice(n)
password=random.choice(AZ)+random.choice(az)+random.choice(n)

chromedriver = "/home/usr/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

driver.get("http://127.0.0.1:8000/login")
elem = driver.find_element_by_name("email")
elem.send_keys(email)
time.sleep(1)

elem = driver.find_element_by_name("nickname")
elem.send_keys(nickname)
time.sleep(1)

elem = driver.find_element_by_name("password")
elem.send_keys(password)
time.sleep(1)

button = driver.find_element_by_name("btn_log")
button.click()
time.sleep(1)

driver.get("http://127.0.0.1:8000/signin")
elem = driver.find_element_by_name("username")
elem.send_keys(nickname)
time.sleep(1)

elem = driver.find_element_by_name("password")
elem.send_keys(password)
time.sleep(1)

button = driver.find_element_by_name("btn_sgn")
button.click()
