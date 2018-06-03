#!/usr/bin/env bash

set e

source venv_pycmd/bin/activate

py.test visualizer_login.py --junit-xml=test-results.xml

deactivate
