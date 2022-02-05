# This module includes the basics of Selenium framework.

import os
from selenium import webdriver

# Here we register the Chrome driver as an environment variable in our code
# And not in the system level. We did that here in code because...
# Because if we decide to run this script on any other machine
# We have to do it again in the system level
# That's why we did that in the code level
os.environ['PATH'] += r"C://SeleniumDrivers"

driver = webdriver.Chrome()
