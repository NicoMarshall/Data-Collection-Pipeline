from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Scraper:
    def __init__(self, driver, url) :
        self.driver = driver
        self.url = url
        
        