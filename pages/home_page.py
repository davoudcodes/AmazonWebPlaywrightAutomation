from playwright.sync_api import Page, expect


class HomePage:
    def __init__(self, page:Page):
        self.page = page
        self.signin_link = page.locator('#nav-link-accountList a')
        self.app_logo = page.locator('#nav-logo a')

    def get_homepage_title(self):
        title = self.page.title()
        return title

    def click_sigin_link(self):
        try:
            self.signin_link.click()
        except Exception as e:
            print(f" Exception while clicking 'Sign in': {e}")
            raise



