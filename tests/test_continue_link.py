import pytest
from playwright.sync_api import expect
from pages.continue_page import ContinuePage
from pages.home_page import HomePage

@pytest.mark.sanity
def test_continue_button(page):
    continue_page = ContinuePage(page)
    home_page = HomePage(page)
    continue_page.continue_link()
    print(home_page.test_homepage_title())

