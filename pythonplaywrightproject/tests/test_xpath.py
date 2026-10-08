from playwright.sync_api import Page, expect
# 1) Absolute XPath:
def test_absolute_xpath(page:Page):
    page.goto("file:///C:/Important Folder/PythonPlaywrightTrainingPgudi/HTML_Pages/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("xpath=html/body/div/form/input").first.fill("DemoUser1")
    page.wait_for_timeout(2000)
 
# Case 1: Identify the UI Element using tagName
def test_relative_xpath_using_tagname(page:Page):
    page.goto("file:///C:/Important Folder/PythonPlaywrightTrainingPgudi/HTML_Pages/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("xpath=//input").first.fill("DemoUser1")
    page.wait_for_timeout(2000)
 
# Case 2: Identify the UI Element using TagName and  index
def test_relative_xpath_using_tagname_index(page:Page):
    page.goto("file:///C:/Important Folder/PythonPlaywrightTrainingPgudi/HTML_Pages/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("xpath=//input").nth(1).fill("DemoPassword1")
    page.wait_for_timeout(2000)
 
# Case 3: Identify the UI Element using TagName with Attribute Name and Value
def test_relative_xpath_attributename_attributevalue(page:Page):
    #page.goto("file:///D:/Example/Sample.html")
    page.goto("file:///C:/Important Folder/PythonPlaywrightTrainingPgudi/HTML_Pages/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("xpath=//input[@name='pass1word1']").fill("DemoPassword2")
    page.wait_for_timeout(2000)
 
# Case 4: Identify the UI Element using  Attribute Name and Value combination
def test_relative_xpath_attributename_attributevalue_combination(page:Page):
    page.goto("file:///C:/Important Folder/PythonPlaywrightTrainingPgudi/HTML_Pages/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("xpath=//*[@id='pwd1pass1word1']").fill("DemoPassword3")
    page.wait_for_timeout(2000)
 
# Case 5: Identify the UI Element using  Attribute Value alone
def test_relative_xpath_attributevalue_alone(page:Page):
    page.goto("file:///C:/Important Folder/PythonPlaywrightTrainingPgudi/HTML_Pages/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("xpath=//*[@*='pwd1pass1word1']").fill("DemoPassword4")
    page.wait_for_timeout(2000)

# Case 6: Identify the UI Element using  TagName with Multiple Attribute Name and Value combination
def test_relative_xpath_attributevalue_alone(page:Page):
    page.goto("file:///C:/Important Folder/PythonPlaywrightTrainingPgudi/HTML_Pages/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("xpath=//input[@type='checkbox'][@name='windows']").click()
    page.wait_for_timeout(2000)

# Case 7: Identify the UI Element using  TagName with Multiple Attribute Name and Value combination by or operator
def test_relative_xpath_multiple_attributenamevalue_or_operator(page:Page):
    page.goto("file:///C:/Important Folder/PythonPlaywrightTrainingPgudi/HTML_Pages/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("xpath=//input[@type='checkbox' or @id='chk2linux']").nth(1).click()
    page.wait_for_timeout(2000)

# Case 8: Identify the UI Element using  TagName with Multiple Attribute Name and Value combination by and operator
def test_relative_xpath_multiple_attributenamevalue_and_operator(page:Page):
    page.goto("file:///C:/Important Folder/PythonPlaywrightTrainingPgudi/HTML_Pages/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("xpath=//input[@type='radio' and @id='rad2firefox']").click()
    page.wait_for_timeout(2000)

# Case 9:  Identify the UI Element using  TagName with Attribute Name combination.
# Find number of Links in the Application
def test_relative_xpath_tagname_attributename_combination01(page:Page):
    page.goto("file:///C:/Important Folder/PythonPlaywrightTrainingPgudi/HTML_Pages/Sample.html")
    page.wait_for_timeout(2000)
    oLinks=page.locator("xpath=//a[@href]")
    print("Number of Links in Application :",oLinks.count())
    page.wait_for_timeout(2000)
 
# Display Link Names
def test_relative_xpath_tagname_attributename_combination02(page:Page):
    page.goto("file:///C:/Important Folder/PythonPlaywrightTrainingPgudi/HTML_Pages/Sample.html")
    page.wait_for_timeout(2000)
    oLinks=page.locator("xpath=//a[@href]")
    for i in range(0, oLinks.count()):
        print("Link Name :",oLinks.nth(i).text_content())
    page.wait_for_timeout(2000)
 
# Perform Click operation on a specific Link Names
def test_relative_xpath_tagname_attributename_combination03(page:Page):
    page.goto("file:///C:/Important Folder/PythonPlaywrightTrainingPgudi/HTML_Pages/Sample.html")
    page.wait_for_timeout(2000)
    oLinks=page.locator("xpath=//a[@href]")
    for i in range(0, oLinks.count()):
        linkname=oLinks.nth(i).text_content()
        if(linkname.endswith("Testing")):
            oLinks.nth(i).click()
            break
    page.wait_for_timeout(2000)

# Case 10: Identify the UI Element using  TagName with Partial Matching of Attribute Value
def test_relative_xpath_partial_attributevalue(page:Page):
    page.goto("file:///C:/Important Folder/PythonPlaywrightTrainingPgudi/HTML_Pages/Sample.html")
    page.wait_for_timeout(2000)
    #page.locator("xpath=//input[starts-with(@id,'rad2')]").click()
    page.locator("xpath=//input[contains(@id,'rad2')]").click()
    page.wait_for_timeout(2000)

# Case 11 : Inbetween open tag and close if any content available then we can use for below case
# Syntax: //tagName[text()='Exact Text Content']
def test_relative_xpath_exact_text_content(page:Page):
    page.goto("file:///C:/Important Folder/PythonPlaywrightTrainingPgudi/HTML_Pages/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("xpath=//a[text()='S G Software Testing']").click()
    page.wait_for_timeout(2000)

#Case 12: Identify the UI Element using TagName with Exact Text Content with normalize-space()
#Syntax: //tagName[normalize-space()='Exact Text Content']
# Inbetween open tag and close if any content available then we can use for below case
 
def test_relative_xpath_exact_normalizespace_content(page:Page):
    page.goto("file:///C:/Important Folder/PythonPlaywrightTrainingPgudi/HTML_Pages/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("xpath=//a[normalize-space()='S G Software Testing']").click()
    page.wait_for_timeout(2000)

#Case 13:  Identify the UI Element using TagName with Partial Matching of Text Content
'''
starts-with(text(),'partial Text Content')
ends-with(text(),'partial Text Content')
contains(text(),'partial Text Content')
syntax: //tagName[starts-with(text(),'partial Text Content')]
syntax: //tagName[ends-with(text(),'partial Text Content')]
syntax: //tagName[contains(text(),'partial Text Content')]
'''
# Inbetween open tag and close if any content available tehn we can use for below case
def test_relative_xpath_partial_text_content(page:Page):
    page.goto("file:///C:/Important Folder/PythonPlaywrightTrainingPgudi/HTML_Pages/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("xpath=//a[contains(text(),'Software')]").click()
    page.wait_for_timeout(2000)