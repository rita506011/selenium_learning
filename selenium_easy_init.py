from helper.helper_logging import SeleniumEasyLogging
from helper.helper_browser_controller import BrowserController
import variables_global


class SeleniumEasyInit:
    logger = SeleniumEasyLogging().loggingInit(__name__)
    browser_controller = BrowserController()

    @classmethod
    def setUpClass(cls):
        cls.browser_controller.openBrowserChrome()
        cls.browser_controller.buttonClick(variables_global.STR_XPATH_BTN_WELCOME_OPTION_NO)

    @classmethod
    def tearDownClass(cls):
        cls.browser_controller.closeBrowserChrome()
