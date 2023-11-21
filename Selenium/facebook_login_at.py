

# button = driver.find_element(By.XPATH,"//button[@name='login' and contains(@type,'submit')]")
# button.click()


#linktext and paritial link text

# forget_account = driver.find_element(By.LINK_TEXT,'Forgotten account?')
# forget_account.click()

# forgot_account_partial = driver.find_element(By.PARTIAL_LINK_TEXT,'Forgotten')
# forgot_account_partial.click()



# time.sleep(8)
#
# driver.quit()


#task

#https://www.facebook.com/r.php?locale=en_GB&display=page

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# import time
#
# service_object = Service('C:\ChromeDriver\chromedriver-win32\chromedriver.exe')
# driver = webdriver.Chrome(service=service_object)
#
# driver.get('https://www.facebook.com/r.php?locale=en_GB&display=page')
#
#
# first_name = driver.find_element(By.NAME,'firstname')
# first_name.send_keys('Abhishek')
#
# last_name = driver.find_element(By.NAME,'lastname')
# last_name.send_keys('Patra')
#
# input_text = driver.find_element(By.NAME,'reg_email__')
# input_text.send_keys('abhishek@gmail.com')
#
# # input_text = driver.find_element(By.NAME,'reg_email__')
# # input_text.send_keys('abhishek@gmail.com')
#
# pass_input = driver.find_element(By.NAME,'reg_passwd__')
# pass_input.send_keys('Abhi@123')
#
#
# radio_button = driver.find_element(By.ID,'u_0_4_rC')
# radio_button.click()
#
# time.sleep(3)