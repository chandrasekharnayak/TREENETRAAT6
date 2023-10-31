from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_object = Service('C:\ChromeDriver\chromedriver-win32\chromedriver.exe')
driver = webdriver.Chrome(service=service_object)

driver.get('https://rahulshettyacademy.com/AutomationPractice/')

name = driver.find_element(By.ID,'name').send_keys('Abhi Don')
# alret_click = driver.find_element(By.ID,'alertbtn').click()
confirm_click = driver.find_element(By.ID,'confirmbtn').click()
alret_switch = driver.switch_to.alert
print(alret_switch.text)
time.sleep(2)
# alret_switch.accept()
alret_switch.dismiss()

time.sleep(3)
driver.quit()
