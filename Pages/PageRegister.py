from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By

class PageRegister():
    def __init__(self,myDriver):
        self.driver = myDriver
        self.link_registration_form = (By.LINK_TEXT,"registration form")

    def verify_registration_form(self):

        tc = unittest.TestCase('__init__')
        self.driver.implicitly_wait(5)
        registration_link = self.driver.find_element(*self.link_registration_form)
        tc.assertEqual(registration_link.text, "registration form")
