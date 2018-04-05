#!/usr/bin/env bash

# Explanation of the shebang
# #!/usr/bin/env bash #lends you some flexibility on different systems
# #!/usr/bin/bash     #gives you explicit control on a given system of what executable is called


# set -e stops the execution of a script if a command or pipeline has an error - which is the opposite of the default shell behaviour, which is to ignore errors in scripts.
set e

# Activate the Python environment
source venv_pycmd/bin/activate


#Pytest command to run tests in my_test2.py file with allure results enabled. Note that in order to enable allure switch, Python allure package must be installed
py.test --alluredir=allure-results my_test2.py

# Dectivate the environemnt once the tests are finished
deactivate
