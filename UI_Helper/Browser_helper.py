from selenium import  webdriver


class browser_helper(object):
    driver = webdriver.Chrome()
    @classmethod
    def open_browser(self,browser_type):
        driver = webdriver.Chrome()
        if browser_type.upper() == "CHROME":
            driver = webdriver.Chrome()
        if browser_type.upper() == "IE":
            driver = webdriver.ie()
        if browser_type.upper() == "firefox":
            driver = webdriver.firefox()
        return driver