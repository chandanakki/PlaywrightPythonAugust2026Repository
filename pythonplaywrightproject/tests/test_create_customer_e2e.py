# login -> createCustomer-> Delete Customer -> Logout
from playwright.sync_api import Page, expect
 
def test_customer_createscenario(page:Page):
    page.goto("https://sgtestinginstituteapp.onrender.com/")
    page.wait_for_timeout(3000)
    expect(page).to_have_url("https://sgtestinginstituteapp.onrender.com/login")
    # Do Login Action
    page.locator("//input[@name='username']").fill("pgudi")
    page.locator("//input[@name='password']").fill("pgudi")
    page.locator("//button[normalize-space()='Sign In']").click()
    page.wait_for_timeout(3000)
    expect(page.locator("//h2[normalize-space()='S G Software Testing Institute']")).to_have_text("S G Software Testing Institute")
    # NAvigate to Customers
    page.locator("//a[normalize-space()='Customers']").click()
    expect(page.locator("//h4[normalize-space()='Display Customers']")).to_have_text("Display Customers")
    page.locator("//a[normalize-space()='Add Customer']").click()
    expect(page.locator("//h3[normalize-space()='Add Customer']")).to_have_text("Add Customer")
    page.wait_for_timeout(3000)
    # Do Create Customer Action
    page.locator("//input[@placeholder='Enter Customer Name']").fill("demo_auto_01")
    page.locator("//input[@placeholder='Enter EmailId']").fill("auto_cust@sg.com")
    page.locator("//input[@placeholder='Enter Location']").fill("California")
    page.locator("//input[@placeholder='Enter Description']").fill("Testing Purpose")
    page.locator("//button[normalize-space()='Save']").click()
    page.wait_for_timeout(3000)
    expect(page.locator("//td[normalize-space()='demo_auto_01']")).to_be_visible()
 
    page.on("dialog", lambda dialog:(print("alert Message :",dialog.message, dialog.accept())))
 
    # Delete Customer
    page.locator("//td[text()='demo_auto_01']/following-sibling::td/following-sibling::td/following-sibling::td/following-sibling::td/button[2]").click()
    page.wait_for_timeout(3000)
    expect(page.locator("//td[normalize-space()='demo_auto_01']")).not_to_be_visible()
 
    # Logout Action
    page.locator("//button[normalize-space()='Logout']").click()
    # Validation
    expect(page.locator("//h2[normalize-space()='Login']")).to_have_text("Login")
