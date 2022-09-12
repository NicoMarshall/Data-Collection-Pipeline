from nturl2path import url2pathname
from secrets import choice
import unittest
import os.path
import random
from selenium import webdriver
from waterstones_scraping import Scraper


class ScraperTestCase(unittest.TestCase):
    def setUp(self) -> None:
        global url
        url = "https://www.waterstones.com/category/science-technology-medicine/page/1"
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        driver = webdriver.Chrome(options=options) 
        self.scraper = Scraper(driver, url)   

    def test_data_directory_exists(self):
        expected_value = True
        self.scraper.create_data_directory()
        actual_value = os.path.exists("raw_data")
        self.assertEqual(expected_value, actual_value)
       
        
    #def test_gather_links(self):
        #self.scraper.go_to(url)
        #self.scraper.accept_cookies()
        #self.scraper.gather_links()
        #self.assertGreaterEqual(len(self.scraper.url_list), 5)
        
    def test_scrape_text(self):
        self.scraper.go_to("https://www.waterstones.com/book/a-brief-history-of-time/stephen-hawking/9780857501004")
        self.scraper.accept_cookies()
        self.scraper.scrape_text()    
        book_dictionary = self.scraper.book_data[f"{9780857501004}"]
        expected_title = "A Brief History Of Time: From Big Bang To Black Holes (Paperback)"
        actual_title = book_dictionary["book_title"]
        self.assertEqual(expected_title, actual_title)
        expected_author = "Stephen Hawking"
        actual_author = book_dictionary["book_author"]
        self.assertEqual(expected_author, actual_author)
        
        