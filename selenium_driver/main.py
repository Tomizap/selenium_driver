import os
import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as ChromeOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import FirefoxDriverManager

# import undetected_chromedriver as uc

from colorama import Fore



class SeleniumDriver:

    def __init__(self, port=random.randrange(9000, 9999), url='https://google.com', incognito=False,
                 headless=True) -> None:
        
        # super().__init__()

        # d = DesiredCapabilities.CHROME
        # d['loggingPrefs'] = { 'browser':'OFF' }

        options = ChromeOptions()
        # options.add_argument("--remote-debugging-port=" + str(port))
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-browser-side-navigation")
        options.add_argument('--disable-application-cache')
        options.add_argument("--log-level=3")

        if incognito:
            options.add_argument('--incognito')
        if headless:
            options.add_argument('--headless')

        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-dev-shm-usage") 
        options.add_argument("--disable-setuid-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-features=VizDisplayCompositor")
        options.add_argument("--safe-mode")
        options.add_argument("--disable-webgl")
        options.add_argument("--disable-webrtc")
        options.add_argument("--disable-preload")
        options.add_argument("--disable-prerender")

        # from selenium import webdriver
        # self.driver = webdriver.Firefox()

        # self.driver = webdriver.Firefox(ChromeDriverManager().install())

        for _ in range(1):

            # try:
            #     self.driver = uc.Chrome()
            # except Exception as e1:
            #     print(Fore.RED + f'Create Driver Method 1 failed')
            #     print(Fore.WHITE + str(e1))

            try:
                self.driver = webdriver.Chrome(options=options)
                continue
            except Exception as e2:
                print(Fore.RED + f'Create Driver Method 2 failed')
                print(Fore.WHITE + str(e2))

            try:
                self.driver = webdriver.Chrome(
                    service=ChromeService(
                        executable_path='C:/Users/Conta/Desktop/driver/chromedriver.exe'), 
                    options=options)
                continue
            except Exception as e3:
                print(Fore.RED + 'Create Driver Method 3 failed')
                print(Fore.WHITE + str(e3))
                
            try:
                self.driver = webdriver.Chrome(options=options)
                continue
            except Exception as e2:
                print(Fore.RED + f'Create Driver Method 2 failed')
                print(Fore.WHITE + str(e2))

            try:
                self.driver = webdriver.Firefox(
                    service=FirefoxService(executable_path="C:/Users/Conta/Desktop/driver/geckodriver.exe")
                )
                continue
            except Exception as e4:
                print(Fore.RED + 'Create Driver Method 4 failed')
                print(Fore.WHITE + str(e4))
                
        self.action = ActionChains(self.driver)
        self.driver.get(url)
        time.sleep(1)

        try:
            self.driver.find_element(By.CSS_SELECTOR, '#L2AGLb').click()
        except:
            pass
    
    # ------------ Security ---------------

    def captcha(self) -> None:
        captcha_selector = '.Captcha, .captcha, #Captcha, #captcha, .pass-Captcha'
        if "checkpoint" in self.driver.current_url or "challenge" in self.driver.current_url or self.is_attached(captcha_selector):
            print('captcha')
            while "checkpoint" in self.driver.current_url or "challenge" in self.driver.current_url or self.is_attached(captcha_selector):
                time.sleep(2)
                print('wait')
        return
    
    # ------------ Elements ---------------

    def find_element(self, css_selector):
        if self.is_attached(css_selector):
            return self.driver.find_element(By.CSS_SELECTOR, css_selector)

    def find_elements(self, css_selector) -> list:
        if self.is_attached(css_selector):
            return self.driver.find_elements(By.CSS_SELECTOR, css_selector)
        else:
            return []

    def is_attached(self, css_selector) -> bool:

        for _ in range(3):
            if len(self.driver.find_elements(By.CSS_SELECTOR, css_selector)) > 0:
                return True
            time.sleep(1)
        return False
    
    # ------------ Window ---------------

    def window_handles(self):
        return self.driver.window_handles

    def switch_to_window(self, window=None):
        if window is None:
            return
        self.driver.switch_to.window(window)

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()

    # ------------ USER ACTION ---------------

    def get(self, url) -> None:
        print(f'get | {url}')
        self.driver.get(url)
        return

    def execute_script(self, script) -> None:
        try:
            self.driver.execute_script(script)
        except:
            pass
        return

    def click(self, css_selector) -> bool:
        if not self.is_attached(css_selector):
            return False
        time.sleep(1)
        print(f'click | {css_selector}')
        try:
            element = self.driver.find_element(By.CSS_SELECTOR, css_selector)
            self.action.move_to_element(element).click().perform()
        except:
            print('error')
            return False
        return True
           
    def write(self, css_selector, string) -> bool:
        if not self.is_attached(css_selector):
            return False
        self.click(css_selector)
        time.sleep(1)
        print(f'write | {css_selector}')
        self.execute_script(f"document.querySelector('{css_selector}').textContent = ''")
        self.execute_script(f"document.querySelector('{css_selector}').value = ''")
        for letter in string:
            try:
                self.driver.find_element(
                    By.CSS_SELECTOR, css_selector).send_keys(letter)
                time.sleep(random.randrange(1, 4)/10)
            except:
                print('error')
                return False
        return True

    # ------------ USER ACTION ---------------

    def add_cookie(self, cookie):
        self.driver.add_cookie(cookie)

    def current_url(self) -> str:
        return self.driver.current_url
