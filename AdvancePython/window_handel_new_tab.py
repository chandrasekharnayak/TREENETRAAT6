from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_object = Service('C:\ChromeDriver\chromedriver-win32\chromedriver.exe')
driver = webdriver.Chrome(service=service_object)

driver.get('https://rahulshettyacademy.com/AutomationPractice/')


#open a new tab
driver.execute_script("window.open('','_blank');")

#jump one window to another
driver.switch_to.window(driver.window_handles[1])
driver.get('https://treenetra.in/en/treenetra/NewTreentera/')

#return
driver.switch_to.window(driver.window_handles[0])
time.sleep(10)
driver.quit()