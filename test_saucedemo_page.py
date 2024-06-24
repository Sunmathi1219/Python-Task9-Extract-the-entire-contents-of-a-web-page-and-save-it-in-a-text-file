""""
Test Sauce demo page.py
"""


from saucedemo_page import Sauce_demo
import pytest

url = "https://www.saucedemo.com/"
sauce_demo = Sauce_demo(url)

#Test the login  and get the current url and title of the current page
def test_login():

    assert sauce_demo.login() == True
    print("SUCCESS: Test url passes")



#Extract the web content into the text file
def test_extract_content():
    assert sauce_demo.extract_content() == True
    print("SUCCESS :Web Page Contents Saved in Text File ")

#close the python selenium automation
def test_close():
    assert sauce_demo.shut_down() == None
    print("SUCCESS:Python selenium automation was success")
