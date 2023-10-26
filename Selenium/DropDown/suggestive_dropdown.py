from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

service_object = Service('C:\ChromeDriver\chromedriver-win32\chromedriver.exe')
driver = webdriver.Chrome(service=service_object)

driver.get('https://rahulshettyacademy.com/client')

register = driver.find_element(By.LINK_TEXT,'Register').click()

#selective dropdown
occupation_option_selet = Select(driver.find_element(By.XPATH,'//select[@formcontrolname="occupation" ]'))
# occupation_option_selet.select_by_visible_text('Engineer')
# occupation_option_selet.select_by_value('2: Student')
occupation_option_selet.select_by_index(4)
time.sleep(2)

occupation_option_selet.deselect_by_index(4)

driver.f


time.sleep(2)
driver.quit()


#Auto suggestive -- css selector
#table
#selenium math
#iframe
#window handel
#action chain
#jump window and create new window
#screnshot
#pop-up
#mouse hover
#cross browser
