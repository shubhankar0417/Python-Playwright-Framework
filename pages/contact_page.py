from playwright.sync_api import Page, expect
from locators.contact_locators import ContactLocators
from utils.data_loader import load_test_data
from configs.paths import *

class ContactPage:

    def __init__(self, page: Page):
        self.page = page
        self.locator = ContactLocators()
        self.data = load_test_data(TEST_ONE_DATA_PATH)

    def click_submit(self):
        #print('In click submit function')
        #self.page.wait_for_load_state('domcontentloaded')
        self.page.click(self.locator.submit_btn_locator)
        #print('Button is clicked')

    def verify_error_messages(self):
        expect(self.page.locator(self.locator.welcome_error_locator)).to_have_text(self.data["error_messages"]["msgOne"])
        expect(self.page.locator(self.locator.forename_error_locator)).to_have_text(self.data["error_messages"]["msgTwo"])
        expect(self.page.locator(self.locator.email_error_locator)).to_have_text(self.data["error_messages"]["msgThree"])
        expect(self.page.locator(self.locator.message_error_locator)).to_have_text(self.data["error_messages"]["msgFour"])
        self.page.wait_for_timeout(2000)

    def populate_mandatory_fields(self):
        self.page.fill(self.locator.forename_locator, self.data['mandatory_fields']['forename'])
        self.page.fill(self.locator.email_locator, self.data['mandatory_fields']['email'])
        self.page.fill(self.locator.message_locator, self.data['mandatory_fields']['message'])
        self.page.wait_for_timeout(2000)

    def validate_errors_are_gone(self):
        expect(self.page.locator(self.locator.welcome_error_locator)).not_to_be_visible()
        expect(self.page.locator(self.locator.forename_error_locator)).not_to_be_visible()
        expect(self.page.locator(self.locator.email_error_locator)).not_to_be_visible()
        expect(self.page.locator(self.locator.message_error_locator)).not_to_be_visible()

    def validate_success_msg(self):
        self.page.wait_for_selector(self.locator.back_button_locator).is_visible()
        expect(self.page.locator(self.locator.success_msg_locator)).to_be_visible()