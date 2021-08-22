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
        self.browser_controller.buttonClick(variables_global.STR_XPATH_BTN_DEMO_HOME)

    def test_simple_form_single(self):
        self.browser_controller.buttonClick(STR_XPATH_BTN_SIMPLE_FORM)
        msg = 'This is a show message.'
        self.browser_controller.inputText(STR_XPATH_INPUT_SIMPLE_SINGLE_MSG, msg)
        self.browser_controller.buttonClick(STR_XPATH_BTN_SIMPLE_SINGLE_SHOW_MSG)
        get_res = self.browser_controller.getText(STR_XPATH_TEXT_SINGLE_SIMPLE_SHOW_TEXT)
        self.logger.debug('Get text result: %s' % get_res)
        assert msg == get_res

    """
    About test scope, due to this form do not set clearly scope, so too many test cases can be tested. We should
    automate test cases as much as possible in sanity test (e.g. daily automation job), but we can only test the most
    important user scenario in smoke test.
    """
    def test_simple_form_two_valid(self):
        self.browser_controller.buttonClick(STR_XPATH_BTN_SIMPLE_FORM)
        input_a, input_b = 3, 5
        self.browser_controller.inputText(STR_XPATH_INPUT_SIMPLE_TWO_VAL_A, input_a)
        self.browser_controller.inputText(STR_XPATH_INPUT_SIMPLE_TWO_VAL_B, input_b)
        self.browser_controller.buttonClick(STR_XPATH_BTN_SIMPLE_TWO_TOTAL)
        get_res = self.browser_controller.getText(STR_XPATH_TEXT_SIMPLE_TWO_SHOW_SUM)
        self.logger.debug('Get text result: %s' % get_res)
        assert str(input_a + input_b) == get_res

    def test_simple_form_two_valid_with_negative(self):
        self.browser_controller.buttonClick(STR_XPATH_BTN_SIMPLE_FORM)
        input_a, input_b = -1, 5
        self.browser_controller.inputText(STR_XPATH_INPUT_SIMPLE_TWO_VAL_A, input_a)
        self.browser_controller.inputText(STR_XPATH_INPUT_SIMPLE_TWO_VAL_B, input_b)
        self.browser_controller.buttonClick(STR_XPATH_BTN_SIMPLE_TWO_TOTAL)
        get_res = self.browser_controller.getText(STR_XPATH_TEXT_SIMPLE_TWO_SHOW_SUM)
        self.logger.debug('Get text result: %s' % get_res)
        assert str(input_a + input_b) == get_res

    def test_simple_form_two_invalid_with_empty(self):
        self.browser_controller.buttonClick(STR_XPATH_BTN_SIMPLE_FORM)
        input_a, input_b = '', 3
        invalid_res = 'NaN'
        self.browser_controller.inputText(STR_XPATH_INPUT_SIMPLE_TWO_VAL_A, input_a)
        self.browser_controller.inputText(STR_XPATH_INPUT_SIMPLE_TWO_VAL_B, input_b)
        self.browser_controller.buttonClick(STR_XPATH_BTN_SIMPLE_TWO_TOTAL)
        get_res = self.browser_controller.getText(STR_XPATH_TEXT_SIMPLE_TWO_SHOW_SUM)
        self.logger.debug('Get text result: %s' % get_res)
        assert invalid_res == get_res

    def test_simple_form_two_invalid_with_string(self):
        self.browser_controller.buttonClick(STR_XPATH_BTN_SIMPLE_FORM)
        input_a, input_b = 'This is a.', 3
        invalid_res = 'NaN'
        self.browser_controller.inputText(STR_XPATH_INPUT_SIMPLE_TWO_VAL_A, input_a)
        self.browser_controller.inputText(STR_XPATH_INPUT_SIMPLE_TWO_VAL_B, input_b)
        self.browser_controller.buttonClick(STR_XPATH_BTN_SIMPLE_TWO_TOTAL)
        get_res = self.browser_controller.getText(STR_XPATH_TEXT_SIMPLE_TWO_SHOW_SUM)
        self.logger.debug('Get text result: %s' % get_res)
        assert invalid_res == get_res




