from playwright.sync_api import Page

class signinPage:
    def __init__(self, page: Page):
        self.page = page
        self.signin_page_text_element = page.locator('.a-size-medium-plus.a-spacing-small')

    def get_signin_page_text_element(self):
        return self.signin_page_text_element