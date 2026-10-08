from playwright.sync_api import Page, expect
# 1) Absolute CSS:
def test_absolute_css(page:Page):
    page.goto("file:///C:/Important Folder/PythonPlaywrightTrainingPgudi/HTML_Pages/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("css=html body div form input").first.fill("DemoUser1")
    page.wait_for_timeout(2000)
 

#If any CSS does not start with root tag HTML, that represents Relative CSS.
 
#Case 1: Identify the Element using tagName alone
def test_relative_tagname_alone(page:Page):
    page.goto("file:///C:/Important Folder/PythonPlaywrightTrainingPgudi/HTML_Pages/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("css=input").first.fill("DemoUser2")
    page.wait_for_timeout(2000)
 
#Case 2: Identify the Element using tagName with id attribute value
#Syntax: tagname#idattributevalue
def test_relative_tagname_with_idattributevalue(page:Page):
    page.goto("file:///C:/Important Folder/PythonPlaywrightTrainingPgudi/HTML_Pages/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("css=input#pwd1pass1word1").first.fill("DemoPassword1")
    page.wait_for_timeout(2000)
 
#Case 3: Identify the Element using id attribute value
#Syntax: idattributevalue
def test_relative_idattributevalue(page:Page):
    page.goto("file:///C:/Important Folder/PythonPlaywrightTrainingPgudi/HTML_Pages/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("css=#pwd1pass1word1").first.fill("DemoPassword2")
    page.wait_for_timeout(2000)
 
#Case 4: Identify the Element using tagName with class attribute value
#Syntax: tagname.classattributevalue
def test_relative_tagname_with_classattributevalue(page:Page):
    page.goto("file:///C:/Important Folder/PythonPlaywrightTrainingPgudi/HTML_Pages/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("css=input.pass1word1").first.fill("DemoPassword3")
    page.wait_for_timeout(2000)
 
#Case 5: Identify the Element using class attribute value
#Syntax: .classattributevalue
def test_relative_with_classattributevalue(page:Page):
    page.goto("file:///C:/Important Folder/PythonPlaywrightTrainingPgudi/HTML_Pages/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("css=.pass1word1").first.fill("DemoPassword4")
    page.wait_for_timeout(2000)

#Case 6: Identify the Element using tagname with attribute name and value combination
#Syntax: tagname[attributename=attributevalue]
def test_relative_tagname_with_attributenamevalue(page:Page):
    page.goto("file:///C:/Important Folder/PythonPlaywrightTrainingPgudi/HTML_Pages/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("css=input[id='chk1windows']").click()
    page.wait_for_timeout(2000)

#Case 7: Identify the Element using tagname with multiple attribute name and value combination
#Syntax: tagname[attributename=attributevalue][attributename=attributevalue]
def test_relative_tagname_with_multipleattributenamevalue(page:Page):
    page.goto("file:///C:/Important Folder/PythonPlaywrightTrainingPgudi/HTML_Pages/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("css=input[type='checkbox'][id='chk2linux']").click()
    page.wait_for_timeout(2000)

#Case 8: Identify the Element using tagname with partial matching of attribute value
#Syntax:
#tagname[attrubutename ^= attrubtevalue]    // starts-with
#tagname[attrubutename $= attrubtevalue]    // ends-with
#tagname[attrubutename *= attrubtevalue]    // contains
 
def test_relative_tagname_with_partialmatchingofattributevalue(page:Page):
    page.goto("file:///C:/Important Folder/PythonPlaywrightTrainingPgudi/HTML_Pages/Sample.html")
    page.wait_for_timeout(2000)
    #page.locator("css=input[id ^='rad1']").click()
    page.locator("css=input[id *='rad2']").click()
    page.wait_for_timeout(2000)

#Case 9: Identify the Element using tagname with attribute name
#Syntax: tagname[attributename]
# Find number of links in the Application
def test_relative_tagname_with_attributename01(page:Page):
    page.goto("file:///C:/Important Folder/PythonPlaywrightTrainingPgudi/HTML_Pages/Sample.html")
    page.wait_for_timeout(2000)
    olinks=page.locator("css=a[href]")
    print("Number of Links in the Application :",olinks.count())
    page.wait_for_timeout(2000)
 
# Display All links in the Application
def test_relative_tagname_with_attributename02(page:Page):
    page.goto("file:///C:/Important Folder/PythonPlaywrightTrainingPgudi/HTML_Pages/Sample.html")
    page.wait_for_timeout(2000)
    olinks=page.locator("css=a[href]")
    for i in range(0, olinks.count()):
        linkname=olinks.nth(i).text_content()
        print("Link Name :",linkname)
    page.wait_for_timeout(2000)
 
 
# Perform Click operation on a Particular link in the Application
def test_relative_tagname_with_attributename03(page:Page):
    page.goto("file:///C:/Important Folder/PythonPlaywrightTrainingPgudi/HTML_Pages/Sample.html")
    page.wait_for_timeout(2000)
    olinks=page.locator("css=a[href]")
    for i in range(0, olinks.count()):
        linkname=olinks.nth(i).text_content()
        if linkname.endswith("Testing"):
            olinks.nth(i).click()
            break
    page.wait_for_timeout(2000)