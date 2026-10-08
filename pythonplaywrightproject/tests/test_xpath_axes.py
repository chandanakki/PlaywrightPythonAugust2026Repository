#following-sibling
#Case 1: For Person name Sachin Tendulkar enter the Salary 25000.
def test_personname_schintendulkar_entersalary(page:Page):
    page.goto("file:///C:/Important Folder/PythonPlaywrightTrainingPgudi/HTML_Pages/WebTableHTML.html")
    page.wait_for_timeout(2000)
    page.locator("xpath=//td[text()='Sachin Tendulkar']/following-sibling::td/following-sibling::td/following-sibling::td/following-sibling::td/input").fill("25000")
    page.wait_for_timeout(2000)
 
 
#following
#Case 2: Enter the salary 32000 for person who is next to Rahul Dravid
def test_entersalary_forpersonname_nextto_rahuldrvid(page:Page):
    page.goto("file:///C:/Important Folder/PythonPlaywrightTrainingPgudi/HTML_Pages/WebTableHTML.html")
    page.wait_for_timeout(2000)
    page.locator("xpath=//td[text()='Rahul Dravid']/following::tr[1]/td[6]/input").fill("32000")
    page.wait_for_timeout(2000)
 
#preceding-sibling
#Case 3: Make status as Active for Designation India Freedom fighter
def test_entersalary_forpersonname_nextto_rahuldrvid(page:Page):
    page.goto("file:///C:/Important Folder/PythonPlaywrightTrainingPgudi/HTML_Pages/WebTableHTML.html")
    page.wait_for_timeout(2000)
    page.locator("xpath=//td[text()='Indian Freedom Fighter']/preceding-sibling::td[1]/preceding-sibling::td[1]/input").click()
    page.wait_for_timeout(2000)
 
#preceding
#Case 4: Make the status as Active for a Record which is previous to Rahul Dravid
def test_makestatsuasactive_forrecordwhichis_previoustoRahuldravid(page:Page):
    page.goto("file:///C:/Important Folder/PythonPlaywrightTrainingPgudi/HTML_Pages/WebTableHTML.html")
    page.wait_for_timeout(2000)
    page.locator("xpath=//td[text()='Rahul Dravid']/preceding::tr[1]/td[1]/input").click()
    page.wait_for_timeout(2000)
 
#decendant
#Case 5: Based on Table id, Enter the salary in for 5th record.
def test_basedon_parent_reference_identifychild(page:Page):
    page.goto("file:///C:/Important Folder/PythonPlaywrightTrainingPgudi/HTML_Pages/WebTableHTML.html")
    page.wait_for_timeout(2000)
    page.locator("xpath=//table[@id='tbl1']/descendant::tr[5]/td[6]/input").fill("37000")
    page.wait_for_timeout(2000)
 
#ancestor
#Case 6: Based on Salary field identify the same table
def test_basedon_child_reference_identifyparent(page:Page):
    page.goto("file:///C:/Important Folder/PythonPlaywrightTrainingPgudi/HTML_Pages/WebTableHTML.html")
    page.wait_for_timeout(2000)
    attributevalue=page.locator("xpath=//input[@id='edit4']/ancestor::td/ancestor::tr/ancestor::table").get_attribute("id")
    print("Table Id Attribute Value :",attributevalue)
    page.wait_for_timeout(2000)
