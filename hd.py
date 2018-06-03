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

def test_visualizer_report_tab_navigate_select_asset():
    browser.maximize_window()
    start_time = time.time()
    while True:
        try:
            #click on Reports tab
            browser.find_element_by_css_selector("li.nav-item:nth-child(3) > a:nth-child(1)").click()
            #Click on create report
            browser.find_element_by_xpath("/html/body/app-root/div[1]/app-reports/div/div[1]/div/div[1]/span/span[2]").click()
            #Select asset type
            select_asset_text = browser.find_element_by_xpath("/html/body/app-root/div[1]/app-reports/div/div[2]/div[1]/div[2]/generic-report/div/div/label").text
            assert select_asset_text == "Select asset type"
            browser.close()
            return
        except (AssertionError, WebDriverException) as e:
            if time.time() - start_time > MAX_WAIT:
                raise e
            time.sleep(0.5)
