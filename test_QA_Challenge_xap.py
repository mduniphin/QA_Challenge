import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class XapTextDuplicate(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_text_input(self):
        driver = self.driver
        driver.get("https://labs.exaptive.city/xap/78c1ece0-c639-11e7-b984-d7a15f6dfbde?version=0.3.0")
        time.sleep(5)
        elem = driver.find_element_by_xpath("//input[1]")
        elem.send_keys("test text")
        assert elem.get_attribute('value') == "test text"


    def test_text_duplication(self):
        driver = self.driver
        driver.get("https://labs.exaptive.city/xap/78c1ece0-c639-11e7-b984-d7a15f6dfbde?version=0.3.0")
        time.sleep(5)
        elem = driver.find_element_by_xpath("//input[1]")
        elem.send_keys("test text")
        elem_dup = driver.find_element_by_xpath("//input[2]")
        assert elem.get_attribute('value') == elem_dup.get_attribute('value')


    def test_clear_button(self):
        driver = self.driver
        driver.get("https://labs.exaptive.city/xap/78c1ece0-c639-11e7-b984-d7a15f6dfbde?version=0.3.0")
        time.sleep(5)
        elem = driver.find_element_by_xpath("//input[1]")
        elem.send_keys("test text")
        assert elem.get_attribute('value') == "test text" 
        driver.find_element_by_xpath("//button").click()
        assert elem.get_attribute('value') == ""


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()