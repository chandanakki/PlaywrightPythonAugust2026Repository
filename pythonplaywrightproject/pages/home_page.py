from playwright.sync_api import Page
 
class HomePage:
    def __init__(self, page:Page):
        self.page=page
        self.lnk_logout_link=page.locator("//button[normalize-space()='Logout']")
 
    def click_logout_link(self):
        self.lnk_logout_link.click()