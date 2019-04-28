from UI_Helper.Browser_helper import browser_helper

from Reporting_helper.write_results import write_results
from Util import Configparser

TCname = Configparser.parser("General","TC_dir") + "TestCase1-.txt"
status = Configparser.parser("General","constant_status")

with open(TCname) as testfile:
    for line in testfile.readlines():
        if line.split("|")[1].upper() == "OPEN BROWSER":
            driver  = browser_helper.open_browser(line.split("|")[2])

status = "PASS"

write_results.write_data(TCname + ",|" + status)

