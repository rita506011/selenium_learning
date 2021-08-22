from helper.helper_logging import SeleniumEasyLogging
from selenium_easy_init import SeleniumEasyInit
import variables_global
from variables_basic import *


class TestBasicLevel(SeleniumEasyInit):
    logger = SeleniumEasyLogging().loggingInit(__name__)

    @classmethod
    def setUpClass(cls):
        super(TestBasicLevel, cls).setUpClass()
        cls.browser_controller = super(TestBasicLevel, cls).browser_controller

    @classmethod
    def tearDownClass(cls):
        super(TestBasicLevel, cls).tearDownClass()

    def setUp(self):
        self.browser_controller.buttonClick(STR_XPATH_BTN_BASIC_MENU)

    def teardown(self):
        self.browser_controller.buttonClick(variables_global.STR_XPATH_DEMO_HOME)

    def test_simple_form_single(self):
        self.browser_controller.buttonClick(STR_XPATH_BTN_SIMPLE_FORM)
        msg = 'This is a show message.'
        self.browser_controller.inputText(STR_XPATH_INPUT_SIMPLE_SINGLE_MSG, msg)
        self.browser_controller.buttonClick(STR_XPATH_BTN_SIMPLE_SINGLE_SHOW_MSG)
        get_text = self.browser_controller.getText(STR_XPATH_TEXT_SINGLE_SIMPLE_SHOW_TEXT)
        self.logger.debug('Get text result: %s' % get_text)
        assert msg == get_text

    def test_simple_form_two(self):
        self.browser_controller.buttonClick(STR_XPATH_BTN_SIMPLE_FORM)
        num1, num2 = 3, 5
        self.browser_controller.inputText(STR_XPATH_INPUT_SIMPLE_TWO_VAL_A, num1)
        self.browser_controller.inputText(STR_XPATH_INPUT_SIMPLE_TWO_VAL_B, num2)
        self.browser_controller.buttonClick(STR_XPATH_BTN_SIMPLE_TWO_TOTAL)
        get_text = self.browser_controller.getText(STR_XPATH_TEXT_SIMPLE_TWO_SHOW_SUM)
        self.logger.debug('Get text result: %s' % get_text)
        assert str(num1 + num2) == get_text





