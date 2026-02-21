from playwright.sync_api import Page, expect


class HomePage:
    def __init__(self, page:Page):
        self.page = page
        self.signin_link = page.locator('#nav-link-accountList a')
        self.app_logo = page.locator('#nav-logo a')
        self.choose_language_element = page.locator("span[class='icp-nav-link-inner'] span[class='nav-line-2']")
        self.get_language_option_element =  page.locator("#nav-flyout-icp  ul[role='list'] > li")

    def get_homepage_title(self):
        title = self.page.title()
        return title

    def click_signin_link(self):
        try:
            self.signin_link.click()
        except Exception as e:
            print(f" Exception while clicking 'Sign in': {e}")
            raise
    def get_language_options(self):
        self.choose_language_element.hover()
        self.page.wait_for_timeout(5000)
        return self.get_language_option_element





