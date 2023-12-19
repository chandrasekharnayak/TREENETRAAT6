# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time
#
# service_object = Service('C:\ChromeDriver\chromedriver-win64\chromedriver-win64\chromedriver.exe')
# driver = webdriver.Chrome(service=service_object)
# driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
#
# driver.implicitly_wait(5)
#
# driver.find_element(By.XPATH,"//input[@name='username']").send_keys('Admin')
# driver.find_element(By.XPATH,"//input[@name='password']").send_keys('admin123')
# driver.find_element(By.XPATH,"//button[@type='submit']").click()