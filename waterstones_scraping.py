from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Scraper:
    def __init__(self, driver, url) :
        self.driver = driver
        self.url = url
        url_list = []
    
    def go_to(url)  :
        driver.get(url)
        time.sleep(2)
        
    def next_page() :
       time.sleep(2)
       next_button = driver.find_element(By.CLASS_NAME,"next")
       next_button.click()    
    
    def accept_cookies() :
        accept_cookies_button = driver.find_element(by=By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
        accept_cookies_button.click()
  
        
        