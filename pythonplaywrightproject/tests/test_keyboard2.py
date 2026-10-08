#Case 2: Perform Multiple keyboard combination

from playwright.sync_api import Page, expect
 
def test_multiple_key_combination(page:Page):
    page.goto("https://sgtestinginstituteapp.onrender.com/")
    page.wait_for_timeout(3000)
    page.keyboard.press("Tab")
    page.wait_for_timeout(1000)
    page.keyboard.type("PLAYWRIGHT AUTOMATION")
    page.wait_for_timeout(1000)
    page.keyboard.press("Control+A")
    page.wait_for_timeout(1000)
    page.keyboard.press("Control+X")
    page.wait_for_timeout(1000)
    page.keyboard.press("Control+V")
    page.wait_for_timeout(3000)