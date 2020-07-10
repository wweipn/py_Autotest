from selenium import webdriver


class test_key:

    def __init__(self):
        self.driver = webdriver.Chrome()

    def input(self, search_type, text, key):
        if search_type == 'name':
            self.driver.find_element_by_name(self.text).send_keys(self.key)
        if search_type == 'xpath':
            self.driver.find_element_by_xpath(self.text).send_keys(self.key)
        if search_type == 'id':
            self.driver.find_element_by_id(self.text).send_keys(self.key)

    def url(self, text):
        self.driver.get(self.text)
