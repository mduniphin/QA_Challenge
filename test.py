from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()
driver.get("https://labs.exaptive.city/xap/78c1ece0-c639-11e7-b984-d7a15f6dfbde?version=0.3.0")
# driver.implicitly_wait(30)
time.sleep(5)
# driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/div[2]/div[2]/button").click()
#elem = driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/div[2]/div[1]/input[1]")
elem = driver.find_element_by_xpath("//input[1]")
elem.send_keys("test text")
