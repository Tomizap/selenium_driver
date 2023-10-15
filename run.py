import time
from selenium_driver import SeleniumDriver

driver = SeleniumDriver(headless=False)
driver.get('https://indeed.com')
print(driver.find_element('body').get_property('innerText'))
print(driver.execute_script('console.log("hello")'))
time.sleep(2)
driver.get('https://linkedin.com')
driver2 = SeleniumDriver(headless=False)
driver.close()

# time.sleep(9999)
