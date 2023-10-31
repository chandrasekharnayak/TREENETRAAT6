from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_object = Service('C:\ChromeDriver\chromedriver-win32\chromedriver.exe')
driver = webdriver.Chrome(service=service_object)

driver.get('https://rahulshettyacademy.com/AutomationPractice/')

#First to end scroll

# scrol1 = driver.execute_script('window.scrollBy(0,document.body.scrollHeight)')

#position to position(top - down)
scrol2 =driver.execute_script('window.scrollBy(0,300)')

# down- top :- window.scrollTo(y,x)

driver.get_screenshot_as_file('scrnsht1.png')



time.sleep(3)
driver.quit()
