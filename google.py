import time
from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://www.google.com/')
time.sleep(2)
#search_box = driver.find_element_by_id("lst-ib")
search_box = driver.find_element_by_name("q")
search_box.send_keys("Draculinio")
