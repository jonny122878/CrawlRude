from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
def DriverFilter(driver):

    time.sleep(10)  
    driver.find_element_by_link_text('台北市全區').click()
    driver.find_element_by_link_text('台北市').click()
    time.sleep(2) 
    driver.find_element_by_xpath("//input[@index=9]").click()
    driver.find_element_by_class_name('search-text-query').click()

