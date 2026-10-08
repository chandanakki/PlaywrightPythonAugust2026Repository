from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.home_page import HomePage
 
def test_pom_login_logout_scenario(page:Page):
    page.goto("https://sgtestinginstituteapp.onrender.com/")
    page.wait_for_timeout(3000)
    # Do Login Action
    oLogin=LoginPage(page)
    oLogin.set_user_name_textfield("pgudi")
    oLogin.set_password_textfield("pgudi")
    oLogin.click_signin_button()
    page.wait_for_timeout(3000)
    # Do Logout
    oHome=HomePage(page)
    oHome.click_logout_link()
    page.wait_for_timeout(3000)