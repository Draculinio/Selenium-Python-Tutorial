import time

class PageIndex:
    def __init__(self,myDriver):
        self.driver = myDriver
        self.user_box = self.driver.find_element_by_name('userName')
        self.pass_box = self.driver.find_element_by_name('password')
        self.register_link = self.driver.find_element_by_link_text("REGISTER")
        submit_button = self.driver.find_element_by_name('login')

    def click_register(self):
        self.register_link.click()

    def login(self,user_name, password):
        self.user_box.send_keys(user_name)
        self.pass_box.send_keys(password)
        self.submit_button.click()
        time.sleep(3)
