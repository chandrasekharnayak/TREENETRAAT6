from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

service_object = Service('C:\ChromeDriver\chromedriver-win32\chromedriver.exe')
driver = webdriver.Chrome(service=service_object)

driver.get('https://rahulshettyacademy.com/AutomationPractice/')

def action_chain():
    hover_element= driver.find_element(By.ID,'mousehover') # seraching hover element
    actions = ActionChains(driver) # impliment action permit to driver
    return actions.move_to_element(hover_element).perform() # for the performance

# action_chain()
# top_click = driver.find_element(By.XPATH,"//a[text()='Top']")
# time.sleep(2)
# top_click.click

action_chain()
reload_click= driver.find_element(By.XPATH,"//a[text()='Reload']")
reload_click.click()


time.sleep(3)
driver.quit()