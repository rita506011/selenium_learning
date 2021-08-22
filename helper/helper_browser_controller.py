from helper.helper_logging import SeleniumEasyLogging
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from variables_global import *


class BrowserController:
    logger = SeleniumEasyLogging().loggingInit(__name__)

    @classmethod
    def openBrowserChrome(cls, url=STR_URL_SELENIUM_EASY_DEMO):
        """
        Open Chrome browser with URL.
        """
        cls.chrome_browser = webdriver.Chrome(ChromeDriverManager().install())
        cls.chrome_browser.implicitly_wait(INT_IMPLICITLY_TIMEOUT)
        cls.chrome_browser.maximize_window()  # resolve element duplicate problem
        cls.chrome_browser.get(url)

    @classmethod
    def closeBrowserChrome(cls):
        """
        Close Chrome browser.
        """
        # close full of chrome window (even if have multiple tabs), include session
        cls.chrome_browser.quit()

    def buttonClick(self, xpath):
        """
        Click button element by xpath.
        """
        try:
            WebDriverWait(self.chrome_browser, INT_EXPLICITLY_TIMEOUT).until(
                EC.presence_of_element_located((By.XPATH, xpath))).click()
        except Exception as e:
            print(e)
            self.logger.exception(e)

    def inputText(self, xpath, text='text'):
        """
        Input text by xpath.
        """
        try:
            element = WebDriverWait(self.chrome_browser, INT_EXPLICITLY_TIMEOUT).until(
                EC.presence_of_element_located((By.XPATH, xpath)))
            element.clear()
            element.send_keys(text)
        except Exception as e:
            print(e)
            self.logger.exception(e)

    def getText(self, xpath):
        """
        Return text by xpath.
        """
        try:
            return WebDriverWait(self.chrome_browser, INT_EXPLICITLY_TIMEOUT).until(
                EC.presence_of_element_located((By.XPATH, xpath))).text
        except Exception as e:
            print(e)
            self.logger.exception(e)