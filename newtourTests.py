import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

class newTours(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.get('http://newtours.demoaut.com/')
        time.sleep(5)

    def test_dropdown(self):
        self.driver.find_element_by_link_text("REGISTER").click()
        countryDropDown = Select(self.driver.find_element_by_name("country"))
        countryDropDown.select_by_index(5)
        countryDropDown.select_by_value("11")
        countryDropDown.select_by_visible_text("CONGO")
        self.assertEquals(countryDropDown.first_selected_option.text.strip(),"CONGO")
        self.assertNotEquals(countryDropDown.first_selected_option.text.strip(),"ITALY")
        self.assertTrue(countryDropDown.first_selected_option.text.strip()=="CONGO")
        self.assertFalse(countryDropDown.first_selected_option.text.strip() == "ARGENTINA")
        self.assertFalse(countryDropDown.first_selected_option.text.strip()!="CONGO")
    def test_register(self):
        user_box = self.driver.find_element_by_name('userName')
        pass_box = self.driver.find_element_by_name('password')
        submit_button = self.driver.find_element_by_name('login')
        user_box.send_keys('test')
        pass_box.send_keys('test')
        submit_button.click()
        time.sleep(3)
        link_registration_form = self.driver.find_element_by_link_text("registration form")
        self.assertEquals(link_registration_form.text,"registration form")

    def tearDown(self):
        self.driver.quit()