import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

browser = webdriver.Firefox()
MAX_WAIT=30


#Login
# xpath username /html/body/app-root/div[1]/app-geps-login/div/div[3]/div[2]/div/div[2]/form/div[1]/input
# xpath password /html/body/app-root/div[1]/app-geps-login/div/div[3]/div[2]/div/div[2]/form/div[2]/input
# xpath Sign In button /html/body/app-root/div[1]/app-geps-login/div/div[3]/div[2]/div/div[2]/form/button[2]

def test_visualizer_login():
    url = "https://abvspoc-staging.azurewebsites.net/"
    browser.get(url)
    assert browser.current_url == url+'login'
    browser.find_element_by_xpath("/html/body/app-root/div[1]/app-geps-login/div/div[3]/div[2]/div/div[2]/form/div[1]/input")
    browser.find_element_by_xpath("/html/body/app-root/div[1]/app-geps-login/div/div[3]/div[2]/div/div[2]/form/div[1]/input").clear()
    browser.find_element_by_xpath("/html/body/app-root/div[1]/app-geps-login/div/div[3]/div[2]/div/div[2]/form/div[1]/input").send_keys("muhammad.adnan@hd-wireless.se")
    browser.find_element_by_xpath("/html/body/app-root/div[1]/app-geps-login/div/div[3]/div[2]/div/div[2]/form/div[2]/input")
    browser.find_element_by_xpath("/html/body/app-root/div[1]/app-geps-login/div/div[3]/div[2]/div/div[2]/form/div[2]/input").clear()
    browser.find_element_by_xpath("/html/body/app-root/div[1]/app-geps-login/div/div[3]/div[2]/div/div[2]/form/div[2]/input").send_keys("")
    browser.find_element_by_xpath("/html/body/app-root/div[1]/app-geps-login/div/div[3]/div[2]/div/div[2]/form/button[2]").click()
    time.sleep(2)
    print(browser.current_url)
    assert browser.current_url == "https://abvspoc-staging.azurewebsites.net/map"
    browser.close()

