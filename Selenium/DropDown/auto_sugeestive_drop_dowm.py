from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_object = Service('C:\ChromeDriver\chromedriver-win32\chromedriver.exe')

driver= webdriver.Chrome(service=service_object)

driver.get('https://rahulshettyacademy.com/dropdownsPractise/')

#css - selector
'''
tagname[attribute= 'value']

tag tag tag tag:nth-child(index) :- div div:nth-child(2)  div:nth-child(2) div:nth-child(2)

# id and .class name

#id_value also a css_selector


'''


input_data = driver.find_element(By.ID,'autosuggest').send_keys('ind')
time.sleep(3)

countries = driver.find_elements(By.CSS_SELECTOR,"li[role='presentation'] a")

for country in countries:
    if country.text == 'India':
        country.click()


time.sleep(2)
driver.quit()


'''
Xpath vs CSS

s

 yntax:

XPath: XPath uses a more complex syntax and allows for selecting elements based on their hierarchy and attributes. It provides fine-grained control over element selection.

CSS Selector: CSS Selectors use a simpler syntax that is similar to how you'd define styles in a stylesheet. It's more concise and easier to read for simple selections.

Browser Support:

XPath: XPath is supported by all modern web browsers but may have slight variations in implementation. It is considered a standard for XML documents.

CSS Selector: CSS Selectors are widely supported by modern web browsers, and they are a standard for HTML documents.

Hierarchy:

XPath: XPath allows you to traverse both upward and downward in the DOM hierarchy, making it versatile for selecting complex elements.

CSS Selector: CSS Selectors are primarily used for selecting elements based on their relationships within the DOM hierarchy. They are not as versatile for traversing the hierarchy compared to XPath.

Performance:

XPath: XPath can be slower in terms of performance for complex queries, especially in older browsers. It may not be as efficient for large-scale web scraping tasks.

CSS Selector: CSS Selectors are generally faster and more efficient, especially for simple element selections. They are preferred for performance-critical tasks.

Readability:

XPath: XPath can become complex and less readable for intricate queries, especially when selecting elements with complex conditions.

CSS Selector: CSS Selectors are often more concise and easier to read, making them a good choice for straightforward selections.

Flexibility:

XPath: XPath provides more flexibility and can be used for selecting elements based on various attributes, including text content.

CSS Selector: CSS Selectors are limited to selecting elements based on their attributes, classes, and IDs. They are more rigid in this regard.


'''



