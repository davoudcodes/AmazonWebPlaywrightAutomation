from playwright.sync_api import expect
import pytest
from pages.home_page import HomePage
from pages.signin_page import signinPage



def test_homepage_logo(page):
    homepage = HomePage(page)
    page.wait_for_timeout(5000)
    expect(homepage.app_logo).to_be_visible()


def test_signin_link(page):
    homepage = HomePage(page)
    signin_page = signinPage(page)
    homepage.click_signin_link()
    page.wait_for_timeout(5000)
    signinpage_text_element = signin_page.get_signin_page_text_element()
    expect(signinpage_text_element).to_be_visible(timeout=5000)
    expect(signinpage_text_element).to_have_text("Sign in or create account")

@pytest.mark.sanity
def test_language_options(page):
    homepage = HomePage(page)
    page.wait_for_timeout(5000)
    language_options = homepage.get_language_options().all()
    for language_option in language_options:
        print(language_option.inner_text())
        expect(language_option).to_be_visible()

