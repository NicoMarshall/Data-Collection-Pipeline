# Data-Collection-Pipeline
An implementation of an industry grade data collection pipeline that runs scalably in the cloud.

# Milestone 1
In this first stage I created a Scraper class containing methods to gather data from bestselling science and technology publications listed on the website of Waterstones, a popular book store. This included methods to visit the website, accept cookies, gather book URL's, store them in a list then navigate to the next page.
This is iterated as many times as desired to generate a list of individual book URL's that will be visited and scraped for data in the next milestone.
The class was initialised using Selenium WebDriver as an API with Google Chrome.

# Milestone 2
Data scraping methods created; scrape_text() and scrape_image(). For a given book url generated in milestone 1, scrape_text naviagtes to the page and collects
title, author, price, brief description and isbn into a dictionary. Scrape_image further scrapes a jpg image of the book front cover. All of this data is stored locally, using isbn number to uniquely identify each book. The code for scrape_text is shown below:

```

 def scrape_text(self) :
        book_title = self.driver.find_element(By.CLASS_NAME,"book-title").text 
        book_author = self.driver.find_element(By.CLASS_NAME,"contributors").find_element(By.TAG_NAME,"a").text
        book_price = self.driver.find_element(by=By.XPATH, value='//b[@itemprop="price"]').text
        book_description_1 = self.driver.find_element(by=By.XPATH,value ='//div[@itemprop="description"]/p[1]').get_attribute("textContent")
        book_description_2 = self.driver.find_element(by=By.XPATH,value ='//div[@itemprop="description"]/p[2]').get_attribute("textContent")
        book_description = book_description_1 +  book_description_2
        global isbn
        isbn = self.driver.find_element(by=By.XPATH,value ='//span[@itemprop="isbn"]').get_attribute("textContent")
        book_dict = {"book title" : book_title, "book_author" : book_author, "book_price" : book_price, "book_description" : book_description, "isbn" : isbn, "uuid" : str(uuid.uuid4())}
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
        
```
# Milestone 3
Unit tests created for all the main methods used in the scraper class. These were stored in the test_scraper.py file, which when run will run all the tests within it. 
scrape_text and scrape_image are tested by running on them on an example book ("A Brief History of Time") and checking that the right data is collected and stored.
gather_links is tested by checking that after running, the list of url's is at least 5 long.
create_data_directory is checked simply by seeing if the folder "raw data" exists.

