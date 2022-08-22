from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Scraper:
    def __init__(self, driver, url) :
        self.driver = driver
        self.url = url
        self.url_list = []
    
    def go_to(self,url)  :
        self.driver.get(url)
        
        
    def next_page(self) :
       time.sleep(4)
       next_button = self.driver.find_element(By.CLASS_NAME,"next")
       next_button.click()    
    
    def accept_cookies(self) :
        time.sleep(4)
        accept_cookies_button = self.driver.find_element(by=By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
        accept_cookies_button.click()
  
    def gather_links(self) :
        page_results = self.driver.find_element(by=By.XPATH, value='//div[@class="search-results-list"]')
        book_list = page_results.find_elements(by=By.XPATH, value='./div')
        for book in book_list:
            book_image = book.find_element(By.CLASS_NAME,"image-wrap")
            a_tag = book_image.find_element(By.TAG_NAME,"a")
            link = a_tag.get_attribute("href")
            self.url_list.append(link)
    
    def scrape_text(self) :
        book_title = self.driver.find_element(By.CLASS_NAME,"book-title").text 
        book_author = self.driver.find_element(By.CLASS_NAME,"contributors").find_element(By.TAG_NAME,"a").text
        book_price = self.driver.find_element(by=By.XPATH, value='//b[@itemprop="price"]').text
        book_description_1 = self.driver.find_element(by=By.XPATH,value ='//div[@itemprop="description"]/p[1]').get_attribute("textContent")
        book_description_2 = self.driver.find_element(by=By.XPATH,value ='//div[@itemprop="description"]/p[2]').get_attribute("textContent")
        book_description = book_description_1 + book_description_2
        print(book_description)    
    
            
            
if __name__ == '__main__':
    url = "https://www.waterstones.com/category/science-technology-medicine/page/1"
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(options=options)        
    waterstones_scraper = Scraper(driver,url)    
    waterstones_scraper.go_to(url)
    waterstones_scraper.accept_cookies()
    for _ in range(1):
        waterstones_scraper.gather_links()
        waterstones_scraper.next_page()
    for book_url in waterstones_scraper.url_list :
        waterstones_scraper.go_to(book_url)    
        waterstones_scraper.scrape_text()
    driver.quit()    
    
        