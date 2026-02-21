from playwright.sync_api import Page

class ContinuePage:
    def __init__(self, page: Page):
        self.page = page
        self.continue_link = page.locator('.a-button-text')

    def click_continue(self):
        try:
            self.continue_link.click()
        except Exception as e:
            print(f" Exception while clicking 'My Account': {e}")
            raise
