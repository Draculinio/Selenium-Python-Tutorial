import sys

from Helpers.data import *
from Helpers.xmlReader import *
from Pages.PageFlight import *
from Pages.PageIndex import *
from Pages.PageRegister import *


class newTours(unittest.TestCase):
    def setUp(self):
        self.configuration = xmlReader()
        
        self.driver = webdriver.Chrome('chromedriver.exe')
        #self.driver = webdriver.PhantomJS()
        #self.driver.get('http://newtours.demoaut.com/')
        self.driver.get(self.configuration.obtener_datos('url'))
        self.page_index = PageIndex(self.driver)
        self.page_flight = PageFlight(self.driver)
        self.page_register = PageRegister(self.driver)


    def test_dropdown(self):
        my_data = test_data()
        self.page_index.click_register()
        self.page_flight.select_country_by_index(5)
        self.page_flight.select_country_by_value("11")
        self.page_flight.select_country_by_name(my_data.country)
        self.page_flight.verify_country("CONGO")
        self.page_flight.verify_not_country("ITALY")

    @unittest.skipIf(2>1,"Quiero que 1 sea más que 2")
    def test_register(self):
        self.page_index.login('test','tesqt')
        self.page_register.verify_registration_form()

    @unittest.skipUnless(sys.platform.startswith("linux"), "Solo es para linux")
    def test_login_by_tabs(self):
        self.page_index.login_by_tab('test','test')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='myreport'))
    unittest.main()