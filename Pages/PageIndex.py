import time
from selenium.webdriver.common.by import By

class PageIndex(object):
    def __init__(self,myDriver):
        self.driver = myDriver
        self.user_box = (By.NAME,'userName')
        self.pass_box = (By.NAME, 'password')
        self.register_link = (By.LINK_TEXT, 'REGISTER')
        self.submit_button = (By.NAME,'login')

    def click_register(self):
        self.driver.find_element(*self.register_link).click()

    def login(self,user_name, password):
        self.driver.find_element(*self.user_box).send_keys(user_name)
        self.driver.find_element(*self.pass_box).send_keys(password)
        self.driver.find_element(*self.submit_button).click()
        time.sleep(3)
