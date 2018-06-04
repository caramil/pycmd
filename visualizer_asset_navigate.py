import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

browser = webdriver.Firefox()
MAX_WAIT=30


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
            assert select_asset_text == "1Select asset type"
            browser.close()
            return
        except (AssertionError, WebDriverException) as e:
            if time.time() - start_time > MAX_WAIT:
                raise e
            time.sleep(0.5)
