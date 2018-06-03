#!/usr/bin/env bash

set e

source venv_pycmd/bin/activate

py.test hd.py  --junit-xml=test-results.xml

deactivate
