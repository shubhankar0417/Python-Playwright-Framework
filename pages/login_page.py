from playwright.sync_api import Page
from locators.login_locators import LoginLocators

class LoginPage:

    def __init__(self, page: Page, url: str):
        self.page = page
        self.url = url
        self.locator = LoginLocators()

    def navigate(self):
        self.page.goto(self.url)

    def click_contact(self):
        self.page.click(self.locator.contact_locator)
        self.page.wait_for_timeout(1000)

    def click_shop(self):
        self.page.click(self.locator.shop_locator)
        

