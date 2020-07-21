from selenium import webdriver


def open_browser(name):
    if name == 'Chrome':
        driver = webdriver.Chrome()


class test_keys:

    def __init__(self, name='https://www.baidu.com'):
        self.driver = open(name)

    def input(self, locator_type, locator, key):
        if locator_type == 'name':
            self.driver.find_element_by_name(locator).send_keys(key)
        if locator_type == 'xpath':
            self.driver.find_element_by_xpath(locator).send_keys(key)
        if locator_type == 'id':
            self.driver.find_element_by_id(locator).send_keys(key)


open_browser('Chrome')

