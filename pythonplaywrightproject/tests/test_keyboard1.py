#Case 1: Perform Login using only keyboard operation

from playwright.sync_api import Page, expect
 
def test_keyboard_login(page:Page):
    page.goto("https://sgtestinginstituteapp.onrender.com/")
    page.wait_for_timeout(3000)
    page.keyboard.press("Tab")
    page.wait_for_timeout(1000)
    page.keyboard.type("pgudi")
    page.wait_for_timeout(1000)
    page.keyboard.press("Tab")
    page.wait_for_timeout(1000)
    page.keyboard.type("pgudi")
    page.wait_for_timeout(1000)
    page.keyboard.press("Enter")
    page.wait_for_timeout(3000)