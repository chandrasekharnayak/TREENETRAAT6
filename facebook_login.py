from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoAlertPresentException


from selenium.webdriver.common.by import By
import time


service_object = Service('C:\ChromeDriver\chromedriver-win64\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service_object)

driver.get('https://www.facebook.com/')
driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//input[@id='email']").send_keys("suvam49@ovi.com")
driver.find_element(By.XPATH,"//input[@id='pass']").send_keys("suvam@1996")
driver.find_element(By.XPATH,'//button[@name="login" and contains(@type,"submit")]').click()

# alret_switch = driver.switch_to.alert
# print(alret_switch.text)

time.sleep(10)
# try:
#  driver.switch_to.alert.dismiss()
#
# except NoAlertPresentException:
#      print("No alert present")


# time.sleep(10)
