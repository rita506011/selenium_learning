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

    def test_check_box_single(self):
        self.browser_controller.buttonClick(STR_XPATH_BTN_CHECK_BOX)
        # check default status
        checkbox_status = self.browser_controller.isCheckedCheckbox(STR_XPATH_CHECKBOX_CHECK_SINGLE_CHECKBOX)
        self.logger.debug('Checkbox default status is %s.' % ('checked' if checkbox_status else 'unchecked'))
        assert checkbox_status is False, 'Default value is wrong, should be unchecked.'
        # checked checkbox
        check_res = 'Success - Check box is checked'
        self.browser_controller.buttonClick(STR_XPATH_CHECKBOX_CHECK_SINGLE_CHECKBOX)
        get_msg = self.browser_controller.getText(STR_XPATH_CHECKBOX_CHECK_SINGLE_SHOW_MSG)
        self.logger.debug('Message of checkbox is selected: %s.' % get_msg)
        assert check_res == get_msg, 'Checkbox selected message is wrong.'
        # unchecked checkbox
        self.browser_controller.buttonClick(STR_XPATH_CHECKBOX_CHECK_SINGLE_CHECKBOX)
        get_msg = self.browser_controller.getText(STR_XPATH_CHECKBOX_CHECK_SINGLE_SHOW_MSG)
        self.logger.debug('Checkbox unselect message: %s.' % get_msg)
        assert '' == get_msg, 'Checkbox unselected message is wrong.'

    def test_check_box_multiple_default_check(self):
        self.browser_controller.buttonClick(STR_XPATH_BTN_CHECK_BOX)
        get_checked_list = self._check_box_is_checked()
        assert not get_checked_list, f'At least one checkbox is checked. Checked list is {get_checked_list}.'

    def test_check_box_multiple_button(self):
        self.browser_controller.buttonClick(STR_XPATH_BTN_CHECK_BOX)
        btn_check_all_text = 'Check All'
        btn_uncheck_all_text = 'Uncheck All'
        checkbox_checked_all_list = [1, 2, 3, 4]

        # click 'Check All' (button show 'Uncheck all')
        self.logger.info('Click "Check All" button.')
        self.browser_controller.buttonClick(STR_XPATH_BTN_CHECK_MULTIPLE_ALL)
        get_checked_list = self._check_box_is_checked()
        get_btn_value = self.browser_controller.getAttribute(STR_XPATH_BTN_CHECK_MULTIPLE_ALL, 'value')
        assert get_checked_list == checkbox_checked_all_list, f'At least one checkbox is unchecked. Checked: {get_checked_list}'
        assert get_btn_value == btn_uncheck_all_text, f'Button text is not "{btn_uncheck_all_text}". Actual result is "{get_btn_value}".'

        # Check/unchecked each checkbox will influence button text
        self.logger.info('Start to check each checkbox.')
        for option in range(1, 5):
            self.logger.debug(f'Unchecked checkbox {option}.')
            checked_list = checkbox_checked_all_list.copy()
            # Uncheck checkbox
            self.browser_controller.buttonClick(globals()[f'STR_XPATH_CHECKBOX_CHECK_MULTIPLE_OPTION_{option}'])
            checked_list.remove(option)
            get_checked_list = self._check_box_is_checked()
            get_btn_value = self.browser_controller.getAttribute(STR_XPATH_BTN_CHECK_MULTIPLE_ALL, 'value')
            assert get_checked_list == checked_list,\
                                       f'Checkbox list is wrong. Actual list is {get_checked_list}.'
            assert get_btn_value == btn_check_all_text, f'Button text isn\'t "{btn_check_all_text}". Actual result is "{get_btn_value}".'
            # Checked checkbox again
            self.browser_controller.buttonClick(globals()[f'STR_XPATH_CHECKBOX_CHECK_MULTIPLE_OPTION_{option}'])
            get_btn_value = self.browser_controller.getAttribute(STR_XPATH_BTN_CHECK_MULTIPLE_ALL, 'value')
            assert get_btn_value == btn_uncheck_all_text,\
                                    f'Button text isn\'t "{btn_uncheck_all_text}". Actual result is "{get_btn_value}".'

        # click 'Uncheck All' (button show 'Check all')
        self.logger.info('Click "Uncheck All" button.')
        self.browser_controller.buttonClick(STR_XPATH_BTN_CHECK_MULTIPLE_ALL)
        get_checked_list = self._check_box_is_checked()
        get_btn_value = self.browser_controller.getAttribute(STR_XPATH_BTN_CHECK_MULTIPLE_ALL, 'value')
        assert not get_checked_list, f'At least one checkbox is checked. Checked: {get_checked_list}'
        assert get_btn_value == btn_check_all_text, f'Button text is not "{btn_check_all_text}". Actual result is "{get_btn_value}".'

    def test_select_dropdown_first_check_default_text(self):
        self.browser_controller.buttonClick(STR_XPATH_BTN_SELECT_DROPDOWN)
        correct_options = ['Please select', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        get_options = self.browser_controller.getDropdownAllOptionText(STR_XPATH_DROPDOWN_SELECT_FIRST_DROPDOWN)
        self.logger.debug(f'Get options: {get_options}')
        assert get_options == correct_options, f'Options list is not {correct_options}, actual result is {get_options}.'

    def test_select_dropdown_first(self):
        self.browser_controller.buttonClick(STR_XPATH_BTN_SELECT_DROPDOWN)
        dropdown_list = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        for option in dropdown_list:
            self.browser_controller.dropdownSelect(STR_XPATH_DROPDOWN_SELECT_FIRST_DROPDOWN, option)
            get_selected = self.browser_controller.getText(STR_XPATH_TEXT_SELECT_FIRST_SHOW_TEXT)
            self.logger.debug(f'Selected value is "{get_selected}".')
            assert get_selected == f'Day selected :- {option}',\
                f'Message should be "Day selected :- {option}", actual result is "{get_selected}".'

    def test_select_dropdown_multi_check_default_text(self):
        self.browser_controller.buttonClick(STR_XPATH_BTN_SELECT_DROPDOWN)
        correct_options = ['California', 'Florida', 'New Jersey', 'New York', 'Ohio', 'Texas', 'Pennsylvania', 'Washington']
        get_options = self.browser_controller.getDropdownAllOptionText(STR_XPATH_DROPDOWN_SELECT_MULTI_DROPDOWN)
        self.logger.debug(f'Get options: {get_options}')
        assert get_options == correct_options, f'Options list is not {correct_options}, actual result is {get_options}.'

    def _check_box_is_checked(self):
        """
        For form 'Check Box Demo', return a list that checkbox is checked.
        """
        checked_list = []
        for option in range(1, 5):
            checkbox_status = self.browser_controller. \
                isCheckedCheckbox(globals()[f'STR_XPATH_CHECKBOX_CHECK_MULTIPLE_OPTION_{option}'])
            self.logger.debug('Checkbox option %d status is %s.'
                              % (option, ('checked' if checkbox_status else 'unchecked')))
            if checkbox_status is True:
                checked_list.append(option)
        return checked_list
