#Case 3: Playwright example for Multiple key combination
from playwright.sync_api import Page, expect
 
def test_multiple_key_combination(page:Page):
    page.goto("https://sgtestinginstituteapp.onrender.com/")
    page.wait_for_timeout(3000)
    page.keyboard.press("Tab")
    page.wait_for_timeout(1000)
    page.keyboard.type("Hello World!")
    page.keyboard.press("ArrowLeft")
    page.keyboard.down("Shift")
    page.wait_for_timeout(1000)
    for i in range(6):
        page.keyboard.press("ArrowLeft")
        page.wait_for_timeout(1000)
    page.keyboard.up("Shift")
    page.keyboard.press("Backspace")
    page.wait_for_timeout(2000)
    # result text will end up saying "Hello!"