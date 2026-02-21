from playwright.sync_api import expect
import pytest
from pages.home_page import HomePage
from pages.signin_page import signinPage


@pytest.mark.sanity
def test_homepage_logo(page):
    homepage = HomePage(page)
    page.wait_for_timeout(5000)
    expect(homepage.app_logo).to_be_visible()

@pytest.mark.sanity
def test_signin_link(page):
    homepage = HomePage(page)
    signin_page = signinPage(page)
    homepage.click_sigin_link()
    page.wait_for_timeout(5000)
    signinpage_text_element = signin_page.get_signin_page_text_element()
    expect(signinpage_text_element).to_be_visible(timeout=5000)
    expect(signinpage_text_element).to_have_text("Sign in or create account")

