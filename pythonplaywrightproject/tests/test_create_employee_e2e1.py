#Navigate URL -> Login -> CreateEmployee -> DeleteEmployee -> Logout 
from playwright.sync_api import Page, expect
 
def test_employee_createscenario(page:Page):
    page.goto("https://sgtestinginstituteapp.onrender.com/")
    page.wait_for_timeout(3000)
    expect(page).to_have_url("https://sgtestinginstituteapp.onrender.com/login")
    # Do Login Action
    page.locator("//input[@name='username']").fill("pgudi")
    page.locator("//input[@name='password']").fill("pgudi")
    page.locator("//button[normalize-space()='Sign In']").click()
    page.wait_for_timeout(3000)
    expect(page.locator("//h2[normalize-space()='S G Software Testing Institute']")).to_have_text("S G Software Testing Institute")

    #Navigate to Employees
    page.locator("//a[normalize-space()='Employees']").click()
    expect(page.locator("//h4[normalize-space()='Display Employees']")).to_have_text("Display Employees")
    page.locator("//a[normalize-space()='Add Employee']").click()
    expect(page.locator("//h3[normalize-space()='Add Employee']")).to_have_text("Add Employee")
    page.wait_for_timeout(3000)
    # Do Create Employee Action
    page.locator("//input[@placeholder='Enter First Name']").fill("Chandan")
    page.locator("//input[@placeholder='Enter Last Name']").fill("Akki")
    page.locator("//input[@placeholder='Enter Job Name']").fill("")
    page.locator("//input[@placeholder='Enter Email Id']").fill("auto_emp@stg.com")
    page.locator("//input[@placeholder='Enter Age']").fill("44")
    page.locator("//input[@placeholder='Enter Contact Number']").fill("9876543219")
    page.locator("//input[@placeholder='Enter Salary']").fill("100000")
    page.locator("//input[@placeholder='Enter Department Name']").fill("QA")
    page.locator("//input[@placeholder='Enter City Name']").fill("Bengaluru")
    page.locator("//input[@placeholder='Enter Address']").fill("House No 2 Uttarahalli Bengaluru")
    page.locator("//button[normalize-space()='Save']").click()
    page.wait_for_timeout(3000)