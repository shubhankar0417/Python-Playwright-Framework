import pytest
from configs.urls import URLS
from pages.login_page import LoginPage
from pages.contact_page import ContactPage
from pages.shop_page import ShopPage
from pages.cart_page import CartPage

# Global variable
url = URLS["jupiter_toys"]

def test_one(page):  
   
    # navigate to the login page
    login_page = LoginPage(page, url)
    
    login_page.navigate()

    # click on the contact button
    login_page.click_contact()

    # click submit button for being prompted to enter mandatory fields
    contact_page = ContactPage(page)
    contact_page.click_submit()

    # verify the mandatory fields
    contact_page.verify_error_messages()

    # populate the manadatory fields
    contact_page.populate_mandatory_fields()

    # validate errors are gone
    contact_page.validate_errors_are_gone()

@pytest.mark.parametrize('run', range(5))
def test_two(page, run):

    login_page = LoginPage(page, url)
    login_page.navigate()

    # click on the contact button
    login_page.click_contact()

    # fill the mandatory fields
    contact_page = ContactPage(page)
    contact_page.populate_mandatory_fields()
    
    # click submit button
    contact_page.click_submit()

    # validate successful submission
    contact_page.validate_success_msg()


def test_three(page):

    # navigate to the url
    login_page = LoginPage(page, url)
    login_page.navigate()

    # click on the contact button
    login_page.click_shop()

    # select items
    shop_page = ShopPage(page)
    shop_page.buy_items()

    # click cart
    shop_page.click_cart()

    # verify total amount
    cart_page = CartPage(page)
    cart_page.verify_final_amount()

    page.wait_for_timeout(2000)
