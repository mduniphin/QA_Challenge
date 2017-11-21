from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import unittest
import time


class XapTextMirror(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
       

    #Tests text input in left textbox
    def test_text_input(self):
        driver = self.driver
        driver.get("https://labs.exaptive.city/xap/78c1ece0-c639-11e7-b984-d7a15f6dfbde?version=0.3.0")
        time.sleep(8)
        elem = driver.find_element_by_xpath("//input[1]")
        elem.send_keys("test text")
        assert elem.get_attribute('value') == "test text"


    #Tests mirroring of text input in left textbox to right textbox
    def test_text_duplication(self):
        driver = self.driver
        driver.get("https://labs.exaptive.city/xap/78c1ece0-c639-11e7-b984-d7a15f6dfbde?version=0.3.0")
        time.sleep(8)
        elem = driver.find_element_by_xpath("//input[1]")
        elem.send_keys("test text")
        elem_right = driver.find_element_by_xpath("//input[2]")
        assert elem.get_attribute('value') == elem_right.get_attribute('value')


    #Tests mirroring of text input and backspace key in left textbox to right textbox  
    def test_text_duplication_backspace(self):
        driver = self.driver
        driver.get("https://labs.exaptive.city/xap/78c1ece0-c639-11e7-b984-d7a15f6dfbde?version=0.3.0")
        time.sleep(8)
        elem = driver.find_element_by_xpath("//input[1]")
        elem.send_keys("test text")
        elem_right = driver.find_element_by_xpath("//input[2]")
        assert elem.get_attribute('value') == elem_right.get_attribute('value')
        elem.send_keys(Keys.BACKSPACE)
        assert elem.get_attribute('value') == "test tex" 
        assert elem.get_attribute('value') == elem_right.get_attribute('value')


    #Confirms that Copy and Paste inputs in left textbox are mirrored to right textbox
    def test_copy_paste_duplication(self):
        driver = self.driver
        driver.get("https://labs.exaptive.city/xap/78c1ece0-c639-11e7-b984-d7a15f6dfbde?version=0.3.0")
        time.sleep(8)
        elem = driver.find_element_by_xpath("//input[1]")
        elem.send_keys(" !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~")
        elem_right = driver.find_element_by_xpath("//input[2]")
        assert elem.get_attribute('value') == " !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~" 
        time.sleep(3)
        assert elem_right.get_attribute('value') == " !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~" 
        elem.send_keys(Keys.CONTROL, 'a')
        elem.send_keys(Keys.CONTROL, 'c')
        elem.send_keys(Keys.CONTROL, 'v')
        elem.send_keys(Keys.CONTROL, 'v')
        time.sleep(5)
        assert elem.get_attribute('value') == " !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~" 
        assert elem_right.get_attribute('value') == " !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~" 


    #Confirms left to right textbox mirroring when the right textbox starts with text in it
    def test_text_right_override(self):
        driver = self.driver
        driver.get("https://labs.exaptive.city/xap/78c1ece0-c639-11e7-b984-d7a15f6dfbde?version=0.3.0")
        time.sleep(8)
        elem = driver.find_element_by_xpath("//input[1]")
        elem_right = driver.find_element_by_xpath("//input[2]")
        elem_right.send_keys("test text")
        elem.send_keys("This should replace")
        time.sleep(3)
        assert elem.get_attribute('value') == elem_right.get_attribute('value')


    #Confirms that Clear button clears left textbox
    def test_clear_button_left(self):
        driver = self.driver
        driver.get("https://labs.exaptive.city/xap/78c1ece0-c639-11e7-b984-d7a15f6dfbde?version=0.3.0")
        time.sleep(8)
        elem = driver.find_element_by_xpath("//input[1]")
        elem.send_keys("test text")
        assert elem.get_attribute('value') == "test text" 
        driver.find_element_by_xpath("//button").click()
        assert elem.get_attribute('value') == ""


    #Confirms that Clear button clears right textbox
    def test_clear_button_right(self):
        driver = self.driver
        driver.get("https://labs.exaptive.city/xap/78c1ece0-c639-11e7-b984-d7a15f6dfbde?version=0.3.0")
        time.sleep(8)
        elem = driver.find_element_by_xpath("//input[1]")
        elem.send_keys("test text")
        elem_right = driver.find_element_by_xpath("//input[2]")
        assert elem_right.get_attribute('value') == "test text" 
        driver.find_element_by_xpath("//button").click()
        assert elem_right.get_attribute('value') == ""
        elem_right.send_keys("test text")
        driver.find_element_by_xpath("//button").click()
        assert elem_right.get_attribute('value') == ""


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(XapTextMirror)
    unittest.TextTestRunner(verbosity=2).run(suite)