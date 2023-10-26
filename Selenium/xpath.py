from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_object = Service('C:\ChromeDriver\chromedriver-win32\chromedriver.exe')
driver = webdriver.Chrome(service=service_object)

driver.get('https://rahulshettyacademy.com/AutomationPractice/')

# check_box = driver.find_element(By.XPATH,'//body/div/div[4]/fieldset/label[1]/input').click()

#following sibling

# cureent_element = driver.find_element(By.XPATH,"//label[@for='bmw']")
# sibling_element = cureent_element.find_element(By.XPATH,'following-sibling::label')
# sec_sibling_element = sibling_element.find_element(By.XPATH,'following-sibling::label/input')
# sec_sibling_element.click()
#current_var.fid_element(By.Xapth,'following-sibling::tag']
#
# data = sec_sibling_element.text
# print(data)


#proceding siblling
# time.sleep(2)
# driver.quit()