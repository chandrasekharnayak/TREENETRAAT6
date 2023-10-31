from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service_object = Service('C:\ChromeDriver\chromedriver-win32\chromedriver.exe')
driver = webdriver.Chrome(service=service_object)

driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')

driver.implicitly_wait(3)
search_bar = driver.find_element(By.CSS_SELECTOR,'.search-keyword').send_keys('ber')
time.sleep(2)
result = driver.find_elements(By.XPATH,"//div[@class='products']/div")
# count = len(result)

for i in result:
    i.find_element(By.XPATH,'div/button').click()

cart_img_click = driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
checkout = driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

promo_code = driver.find_element(By.CSS_SELECTOR,'.promoCode').send_keys('ABCD')
apply = driver.find_element(By.CSS_SELECTOR,'.promoBtn').click()

# check = driver.find_element(By.CSS_SELECTOR,'.promoInfo').text
# print(check)
#explicit wait

wait = WebDriverWait(driver,15)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.promoInfo')))

time.sleep(3)

driver.quit()