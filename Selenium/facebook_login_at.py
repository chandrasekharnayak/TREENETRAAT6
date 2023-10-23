from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

service_object = Service('C:\ChromeDriver\chromedriver-win32\chromedriver.exe')
driver = webdriver.Chrome(service=service_object)

driver.get('https://www.facebook.com/login/')

#ID,NAME
# email_input = driver.find_element(By.ID,'email')
# email_input.send_keys('krishna@tr')
#
# password = driver.find_element(By.NAME,'pass')
# password.send_keys('WERTYrytv')
#
# button = driver.find_element(By.ID,'loginbutton')
# button.click()


#linktext and paritial link text

# forget_account = driver.find_element(By.LINK_TEXT,'Forgotten account?')
# forget_account.click()

forgot_account_partial = driver.find_element(By.PARTIAL_LINK_TEXT,'Forgotten')
forgot_account_partial.click()



time.sleep(8)

driver.quit()


#task

#https://www.facebook.com/r.php?locale=en_GB&display=page