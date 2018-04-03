from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import unittest

class PageFlight():
    def __init__(self,myDriver):
        self.driver = myDriver
        self.countryDropDown = (By.NAME,'country')


    def select_country_by_index(self,index):
        Select(self.driver.find_element(*self.countryDropDown)).select_by_index(index)
        

    def select_country_by_value(self,value):
        Select(self.driver.find_element(*self.countryDropDown)).select_by_value(value)


    def select_country_by_name(self,name):
        Select(self.driver.find_element(*self.countryDropDown)).select_by_visible_text(name)

    def verify_country(self,country):
        tc = unittest.TestCase('__init__')
        tc.assertEquals(Select(self.driver.find_element(*self.countryDropDown)).first_selected_option.text.strip(), country)
    def verify_not_country(self,country):
        tc = unittest.TestCase('__init__')
        tc.assertNotEquals(Select(self.driver.find_element(*self.countryDropDown)).first_selected_option.text.strip(), country)
