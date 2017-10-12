from selenium import webdriver
import unittest

class PageRegister(unittest.TestCase):
    def __init__(self,myDriver):
        self.driver = myDriver

    def verify_registration_form(self):
        link_registration_form = self.driver.find_element_by_link_text("registration form")
        self.assertEqual(link_registration_form.text, "registration form")
