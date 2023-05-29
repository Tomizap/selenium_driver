import time
import random
from pprint import pprint

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc


class selenium_driver(uc.Chrome):

    def __init__(self, port=random.randrange(9000, 9999), profil=False, secret=True, inconito=False, headless=False) -> None:
        options = uc.ChromeOptions()
        # options.add_experimental_option("debuggerAddress", "127.0.0.1:" + str(port))
        options.add_argument("--remote-debugging-port=" + str(port))
        if profil is True:
            options.add_argument(
                "user-data-dir=C:\\Users\\Conta\\AppData\\Local\\Google\\Chrome\\User Data")
        if inconito is True:
            options.add_argument('--incognito')
        if headless is True:
            options.add_argument('--headless')
        if secret is True:
            options.add_argument('--disable-infobars')
            options.add_argument('--start-maximized')
            options.add_argument('--disable-extensions')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
        self.driver = uc.Chrome(options=options)
        print('driver lunched')
        self.action = ActionChains(self.driver)
        self.driver.get('https://google.com')
        self.driver.maximize_window()
        time.sleep(1)
        try:
            self.driver.find_element(By.CSS_SELECTOR, '#L2AGLb').click()
            time.sleep()
        except:
            pass
        return

    def captcha(self) -> None:
        captcha_selector = '.Captcha, .captcha, #Captcha, #captcha, .pass-Captcha'
        if "checkpoint" in self.driver.current_url or "challenge" in self.driver.current_url or self.is_attached(captcha_selector):
            print('captcha')
            while "checkpoint" in self.driver.current_url or "challenge" in self.driver.current_url or self.is_attached(captcha_selector):
                time.sleep(2)
                print('wait')
        return

    def find_element(self, CSS_SELECTOR):
        for _ in range(3):
            try:
                return self.driver.find_element(By.CSS_SELECTOR, CSS_SELECTOR)
            except:
                time.sleep(1)

    def find_elements(self, CSS_SELECTOR):
        for _ in range(3):
            try:
                return self.driver.find_elements(By.CSS_SELECTOR, CSS_SELECTOR)
            except:
                time.sleep(1)

    def current_url(self) -> str:
        return self.driver.current_url

    def is_attached(self, CSS_SELECTOR) -> bool:
        for _ in range(3):
            try:
                if len(self.driver.find_elements(By.CSS_SELECTOR, CSS_SELECTOR)) > 0:
                    return True
            except:
                time.sleep(1)
        return False

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

    def window_handles(self):
        return self.driver.window_handles

    def switch_to_window(self, window=None):
        if window is None:
            return
        self.switch_to.window(window)

    def click(self, CSS_SELECTOR) -> bool:
        time.sleep(1)
        print(f'click | {CSS_SELECTOR}')
        try:
            element = self.driver.find_element(By.CSS_SELECTOR, CSS_SELECTOR)
            self.action.move_to_element(element).click().perform()
        except:
            print('error')
            return False
        return True

    def write(self, CSS_SELECTOR, string) -> bool:
        self.click(CSS_SELECTOR)
        time.sleep(1)
        print(f'write | {CSS_SELECTOR}')
        self.execute_script(f"document.querySelector('{CSS_SELECTOR}').value = ''")
        for letter in string:
            try:
                self.driver.find_element(
                    By.CSS_SELECTOR, CSS_SELECTOR).send_keys(letter)
                time.sleep(random.randrange(1, 4)/10)
            except:
                print('error')
                return False
        return True
