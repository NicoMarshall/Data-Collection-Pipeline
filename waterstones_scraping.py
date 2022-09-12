from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import uuid
import json
import os
import urllib.request
from urllib.request import Request, urlopen



class Scraper:
    """
    This class is used to build a webscraper to crawl the Waterstones website and gather book data.
    
    Attributes:
        Driver: The software that will take control of the browser to navigate webpages. Here we use Selenium Webdriver.
        URL: The main page to be visited first containing a list of books.
        URL list: A list of individual book URL's that will later be scraped for data.
        Book Data: A dictionary of dictionaries, where each element is a dictionary of data for one book. ISBN number
        used as a unique identifier for each book.
    
    """
    def __init__(self, driver, url) :
        self.driver = driver
        self.url = url
        self.url_list = []
        self.book_data = { "0" : 0}
        
    def create_data_directory(self):
        """
        Sets up the directory where data will be stored locally.
        
        """
        try:
            os.mkdir("raw_data")
            print("Directory raw_data created ") 
        except FileExistsError:
            print("Directory raw_data already exists")
            
    
    def go_to(self,url)  :
        """
        Navigates the webdriver to a url.
        
        """
        self.driver.get(url)
        
        
    def next_page(self) :
        
        """
        Finds the "next page" button and clicks it.
        
        """
        time.sleep(4)
        next_button = self.driver.find_element(By.CLASS_NAME,"next")
        next_button.click()    
    
    def accept_cookies(self) :
        """
        Finds the "accept cookies" button and clicks it.
        
        """
        time.sleep(4)
        accept_cookies_button = self.driver.find_element(by=By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
        accept_cookies_button.click()
  
    def gather_links(self) :
        """
        Iterates through all the books displayed on the "Science and Technology - Bestsellers" 
        page and adds the URL of each to url_list.
        
        """
        page_results = self.driver.find_element(by=By.XPATH, value='//div[@class="search-results-list"]')
        book_list = page_results.find_elements(by=By.XPATH, value='./div')
        for book in book_list:
            book_image = book.find_element(By.CLASS_NAME,"image-wrap")
            a_tag = book_image.find_element(By.TAG_NAME,"a")
            link = a_tag.get_attribute("href")
            self.url_list.append(link)
    
    def scrape_text(self) :
        """
        Scrapes all useful book data from webpage text and stores in dictionary, which is then saved locally.
        
        """
        book_title = self.driver.find_element(By.CLASS_NAME,"book-title").text 
        book_author = self.driver.find_element(By.CLASS_NAME,"contributors").find_element(By.TAG_NAME,"a").text
        book_price = self.driver.find_element(by=By.XPATH, value='//b[@itemprop="price"]').text
        book_description_1 = self.driver.find_element(by=By.XPATH,value ='//div[@itemprop="description"]/p[1]').get_attribute("textContent")
        book_description_2 = self.driver.find_element(by=By.XPATH,value ='//div[@itemprop="description"]/p[2]').get_attribute("textContent")
        book_description = book_description_1 +  book_description_2
        global isbn
        isbn = self.driver.find_element(by=By.XPATH,value ='//span[@itemprop="isbn"]').get_attribute("textContent")
        book_dict = {"book_title" : book_title, "book_author" : book_author, "book_price" : book_price, "book_description" : book_description, "isbn" : isbn, "uuid" : str(uuid.uuid4())}
        self.book_data[f"{isbn}"] = book_dict
        os.chdir("C:/Users/Home/Data Collection Pipeline/Data-Collection-Pipeline/raw_data")
        try:
            os.mkdir(f"{isbn}")
        except FileExistsError:
            pass
        os.chdir(f"C:/Users/Home/Data Collection Pipeline/Data-Collection-Pipeline/raw_data/{isbn}")
        with open('data.json', 'w') as convert_file:
            convert_file.write(json.dumps(book_dict))
        os.chdir("C:/Users/Home/Data Collection Pipeline/Data-Collection-Pipeline")  
        
    def scrape_image(self):
        """
        Downloads image of book front cover using urllib. Saved locally in same folder as dictionary of text data 
        from scrape_text.
        
        """
        page_image = self.driver.find_element(By.CLASS_NAME,"book-image-main")
        image_url = page_image.find_element(by=By.XPATH, value='./img').get_attribute("src") 
        req = Request(image_url, headers={'User-Agent': 'XYZ/3.0'})
        image_data = urlopen(req, timeout=10).read()
        os.chdir(f"C:/Users/Home/Data Collection Pipeline/Data-Collection-Pipeline/raw_data/{isbn}")
        with open('image.jpg', 'wb') as handler:
            handler.write(image_data)
        os.chdir("C:/Users/Home/Data Collection Pipeline/Data-Collection-Pipeline")  
        
        
if __name__ == '__main__':
    url = "https://www.waterstones.com/category/science-technology-medicine/page/1"
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(options=options)        
    waterstones_scraper = Scraper(driver,url)
    waterstones_scraper.create_data_directory()    
    waterstones_scraper.go_to(url)
    waterstones_scraper.accept_cookies()
    for _ in range(1):
        waterstones_scraper.gather_links()
        waterstones_scraper.next_page()
    for book_url in waterstones_scraper.url_list :
        waterstones_scraper.go_to(book_url)    
        waterstones_scraper.scrape_text()
        waterstones_scraper.scrape_image()
        
 
    driver.quit()    
    
        