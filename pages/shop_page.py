from playwright.sync_api import Page
from locators.shop_locators import ShopLocators

class ShopPage:

    def __init__(self, page: Page,):
        self.page = page
        self.locator = ShopLocators()

    def buy_items(self):

        # 2 frogs
        self.page.click(self.locator.stuffed_frog_buy_locator)
        self.page.click(self.locator.stuffed_frog_buy_locator)
        
        # 5 bunny
        self.page.click(self.locator.fluffy_bunny_bug_locator)
        self.page.click(self.locator.fluffy_bunny_bug_locator)
        self.page.click(self.locator.fluffy_bunny_bug_locator)
        self.page.click(self.locator.fluffy_bunny_bug_locator)
        self.page.click(self.locator.fluffy_bunny_bug_locator)        

        # 3 bear
        self.page.click(self.locator.valentine_bear_buy_locator)
        self.page.click(self.locator.valentine_bear_buy_locator)
        self.page.click(self.locator.valentine_bear_buy_locator)
    
    def click_cart(self):
        self.page.click(self.locator.cart_locator)