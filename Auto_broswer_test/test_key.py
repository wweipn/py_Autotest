from selenium import webdriver


def open_browser(self, name, url):
    if name == 'Chrome':
        self.driver.webdriver.Chrome()
    if name == 'ie':
        self.driver.webdriver.IE()


class test_keys:

    def __init__(self, url):
        self.driver = open(self.name, url)

    def input(self, locator_type, locator, key):
        if locator_type == 'name':
            self.driver.find_element_by_name(locator).send_keys(key)
        if locator_type == 'xpath':
            self.driver.find_element_by_xpath(locator).send_keys(key)
        if locator_type == 'id':
            self.driver.find_element_by_id(locator).send_keys(key)

