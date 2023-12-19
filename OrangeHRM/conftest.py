import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@pytest.fixture(autouse=True)
def browser():
    '''set up the orange HRM webpage for login purpose'''
    service_object = Service('C:\ChromeDriver\chromedriver-win64\chromedriver-win64\chromedriver.exe')
    driver = webdriver.Chrome(service=service_object)
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH,"//input[@name='username']").send_keys('Admin')
    driver.find_element(By.XPATH,"//input[@name='password']").send_keys('admin123')
    driver.find_element(By.XPATH,"//button[@type='submit']").click()

    yield
    driver.find_element(By.XPATH,"//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']").click()
    driver.find_element(By.XPATH,"//a[normalize-space()='Logout']").click()
    driver.quit()
