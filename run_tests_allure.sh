#!/usr/bin/env bash

set e
# Activate the Python environment
source venv_pycmd/bin/activate


#Pytest command to run tests in my_test2.py file with allure results enabled. Note that in order to enable allure switch, Python allure package must be installed
py.test --alluredir=allure-results my_test2.py

# Dectivate the environemnt once the tests are finished
deactivate
