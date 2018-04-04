import pytest
from selenium import webdriver

#create chrome instance
browser = webdriver.Chrome()

#First test
def test_open_url():
    url = "http://blazedemo.com/"
    browser.get(url)
    assert browser.current_url == url

#Close Chrome instance
def test_close_browser():
    browser.close()
    browser.quit()

#Commit succeeded, hurry
#test 3
