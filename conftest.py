import pytest
from playwright.sync_api import sync_playwright, Page
from configs.settings import SETTINGS

@pytest.fixture(scope="session")
def browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=SETTINGS["headless"])
    yield browser
    browser.close()
    playwright.stop()

@pytest.fixture(scope="function")
def page(browser) -> Page:
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()