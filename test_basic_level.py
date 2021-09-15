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
        checkbox_status = self.browser_controller.isCheckedCheckboxorRadio(STR_XPATH_CHECKBOX_CHECK_SINGLE_CHECKBOX)
        self.logger.debug('Checkbox default status is %s.' % ('checked' if checkbox_status else 'unchecked'))
        assert checkbox_status is False, 'Default value is wrong, should be unchecked.'
        # checked checkbox
        check_res = 'Success - Check box is checked'
        self.browser_controller.buttonClick(STR_XPATH_CHECKBOX_CHECK_SINGLE_CHECKBOX)
        get_msg = self.browser_controller.getText(STR_XPATH_TEXT_CHECK_SINGLE_SHOW_MSG)
        self.logger.debug('Message of checkbox is selected: %s.' % get_msg)
        assert check_res == get_msg, 'Checkbox selected message is wrong.'
        # unchecked checkbox
        self.browser_controller.buttonClick(STR_XPATH_CHECKBOX_CHECK_SINGLE_CHECKBOX)
        get_msg = self.browser_controller.getText(STR_XPATH_TEXT_CHECK_SINGLE_SHOW_MSG)
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

    def test_radio_buttons_first_default_check(self):
        self.browser_controller.buttonClick(STR_XPATH_BTN_RADIO_BUTTONS)
        radio_male_status = self.browser_controller.isCheckedCheckboxorRadio(STR_XPATH_RADIO_RADIO_FIRST_RADIO_MALE)
        radio_female_status = self.browser_controller.isCheckedCheckboxorRadio(STR_XPATH_RADIO_RADIO_FIRST_RADIO_FEMALE)
        self.logger.debug('Radio male status is %s, radio female status is %s.'
                          % (('checked' if radio_male_status else 'unchecked'), ('checked' if radio_female_status else 'unchecked')))
        assert radio_male_status is False and radio_female_status is False,\
                f'Radio button default status is wrong, male is {radio_male_status} and female is {radio_female_status}.'
        self.browser_controller.buttonClick(STR_XPATH_BTN_RADIO_FIRST_SHOW)
        get_show_msg = self.browser_controller.getText(STR_XPATH_TEXT_RADIO_FIRST_SHOW_MSG)
        self.logger.debug('Get show message is "%s".' % get_show_msg)
        assert get_show_msg == 'Radio button is Not checked', f'Show message is wrong. Actual result is "{get_show_msg}".'

    def test_radio_buttons_first(self):
        self.browser_controller.buttonClick(STR_XPATH_BTN_RADIO_BUTTONS)
        radio_button_list = ['Male', 'Female']
        for option in radio_button_list:
            # radio button
            self.browser_controller.buttonClick(globals()[f'STR_XPATH_RADIO_RADIO_FIRST_RADIO_{option.upper()}'])
            radio_status = self.browser_controller.isCheckedCheckboxorRadio(globals()[f'STR_XPATH_RADIO_RADIO_FIRST_RADIO_{option.upper()}'])
            self.logger.debug(f'Radio {option} status is %s.' % (('checked' if radio_status else 'unchecked')))
            assert radio_status is True, f'Radio button status is wrong, {option} is {radio_status}.'
            # get show message
            self.browser_controller.buttonClick(STR_XPATH_BTN_RADIO_FIRST_SHOW)
            get_show_msg = self.browser_controller.getText(STR_XPATH_TEXT_RADIO_FIRST_SHOW_MSG)
            self.logger.debug('Get show message is "%s".' % get_show_msg)
            assert get_show_msg == f'Radio button \'{option}\' is checked', f'Show message is wrong. Actual result is "{get_show_msg}".'

    def test_radio_buttons_group_default_check(self):
        self.browser_controller.buttonClick(STR_XPATH_BTN_RADIO_BUTTONS)
        radio_button_list = ['Male', 'Female', '0', '5', '15']
        for option in radio_button_list:
            radio_status = self.browser_controller.isCheckedCheckboxorRadio(globals()[f'STR_XPATH_RADIO_RADIO_GROUP_RADIO_{option.upper()}'])
            self.logger.debug(f'Radio {option} status is %s.' % (('checked' if radio_status else 'unchecked')))
            assert radio_status is False, f'Radio button default status is wrong, {option} is {radio_status}.'
        self.browser_controller.buttonClick(STR_XPATH_BTN_RADIO_GROUP_SHOW)
        get_show_msg = self.browser_controller.getText(STR_XPATH_TEXT_RADIO_GROUP_SHOW_MSG)
        self.logger.debug('Get show message is "%s".' % get_show_msg)
        assert get_show_msg == f'Sex :\nAge group:', f'Show message is wrong. Actual result is "{get_show_msg}".'

    def test_radio_buttons_group(self):
        self.browser_controller.buttonClick(STR_XPATH_BTN_RADIO_BUTTONS)
        radio_button_sex_list = ['Male', 'Female']
        radio_button_age_list = ['0', '5', '15', '50']
        for sex in radio_button_sex_list:
            for age_key in range(0, len(radio_button_age_list)-1):
                # click radio button
                self.browser_controller.buttonClick(globals()[f'STR_XPATH_RADIO_RADIO_GROUP_RADIO_{sex.upper()}'])
                self.browser_controller.buttonClick(globals()[f'STR_XPATH_RADIO_RADIO_GROUP_RADIO_{radio_button_age_list[age_key]}'])
                # get message
                self.browser_controller.buttonClick(STR_XPATH_BTN_RADIO_GROUP_SHOW)
                get_show_msg = self.browser_controller.getText(STR_XPATH_TEXT_RADIO_GROUP_SHOW_MSG)
                self.logger.debug('Get show message is "%s".' % get_show_msg)
                assert get_show_msg == f'Sex : {sex}\nAge group: {radio_button_age_list[age_key]} - {radio_button_age_list[age_key+1]}',\
                        f'Show message is wrong. Actual result is "{get_show_msg}".'

    def _check_box_is_checked(self):
        """
        For form 'Check Box Demo', return a list that checkbox is checked.
        """
        checked_list = []
        for option in range(1, 5):
            checkbox_status = self.browser_controller. \
                isCheckedCheckboxorRadio(globals()[f'STR_XPATH_CHECKBOX_CHECK_MULTIPLE_OPTION_{option}'])
            self.logger.debug('Checkbox option %d status is %s.'
                              % (option, ('checked' if checkbox_status else 'unchecked')))
            if checkbox_status is True:
                checked_list.append(option)
        return checked_list
