#!/usr/bin/env bash

set e

source venv_pycmd/bin/activate

py.test my_test2.py  --junit-xml=test-results.xml

deactivate
