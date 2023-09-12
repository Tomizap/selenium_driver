import time
from selenium_driver import SeleniumDriver

driver = SeleniumDriver(headless=False)
driver.get('https://indeed.com')
# print(driver.find_element('body').get_property('innerText'))
driver.close()

time.sleep(9999)
