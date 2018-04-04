#!/usr/bin/env bash

set e

source venv_pycmd/bin/activate

#py.test --alluredir = "test-results" my_test2.py 


py.test --alluredir=./allure-results my_test2.py

deactivate
