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
        time.sleep(4)
        self.driver.get(url)
        
        
    def next_page() :
       time.sleep(4)
       next_button = self.driver.find_element(By.CLASS_NAME,"next")
       next_button.click()    
    
    def accept_cookies() :
        accept_cookies_button = driver.find_element(by=By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
        accept_cookies_button.click()
  
    def gather_links() :
        global url_list
        page_results = self.driver.find_element(by=By.XPATH, value='//div[@class="search-results-list"]')
        book_list = page_results.find_elements(by=By.XPATH, value='./div')
        for book in book_list:
            book_image = book.find_element(By.CLASS_NAME,"image-wrap")
            a_tag = book_image.find_element(By.TAG_NAME,"a")
            link = a_tag.get_attribute("href")
            url_list.append(link)
        