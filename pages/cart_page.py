from playwright.sync_api import Page
from locators.cart_locators import CartLocators
from utils.data_loader import load_test_data
from configs.paths import *


class CartPage:

    def __init__(self, page: Page):
        self.page = page
        self.locator = CartLocators()
        self.data = load_test_data(TEST_THREE_DATA_PATH)


    def verify_final_amount(self):
        #print('Frog price :', self.page.locator(self.locator.frog_price_locator).inner_text())
        assert self.data['prices']['frog'] == self.page.locator(self.locator.frog_price_locator).inner_text()
        assert self.data['subtotal']['frog'] == self.page.locator(self.locator.frog_subtotal_locators).inner_text()
        assert self.data['prices']['bunny'] == self.page.locator(self.locator.bunny_price_locators).inner_text()
        assert self.data['subtotal']['bunny'] == self.page.locator(self.locator.bunny_subtotal_locator).inner_text()
        assert self.data['prices']['bear'] == self.page.locator(self.locator.bear_price_locator).inner_text()
        assert self.data['subtotal']['bear'] == self.page.locator(self.locator.bear_subtotal_locator).inner_text()
        assert self.data['total']['grand_total'] == self.page.locator(self.locator.total_price_locator).inner_text()
