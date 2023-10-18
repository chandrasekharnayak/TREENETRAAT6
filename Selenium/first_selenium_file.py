from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service_object = Service('C:\ChromeDriver\chromedriver-win32\chromedriver.exe')
driver = webdriver.Chrome(service=service_object)

driver.get('https://www.treenetra.in/')

time.sleep(10)

driver.quit()

#Locater


