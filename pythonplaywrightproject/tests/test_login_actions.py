from playwright.sync_api import Page, expect
 
def test_login_action(page:Page):
    page.goto("https://sgtestinginstituteapp.onrender.com/")
    page.wait_for_timeout(3000)
    # Login Action
    page.locator("//input[@name='username']").fill("chandan")
    page.locator("//input[@name='password']").fill("Test@123")
    page.locator("//button[normalize-space()='Sign In']").click()
    page.wait_for_timeout(3000)