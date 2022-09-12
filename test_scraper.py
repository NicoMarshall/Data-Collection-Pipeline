from nturl2path import url2pathname
import unittest
import os.path
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
        
    def test_gather_links(self):
        self.scraper.go_to(url)
        self.scraper.accept_cookies()
        self.scraper.gather_links()
        self.assertGreaterEqual(len(self.scraper.url_list), 5)
        
        