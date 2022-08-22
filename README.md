# Data-Collection-Pipeline
An implementation of an industry grade data collection pipeline that runs scalably in the cloud.

# Milestone 1
In this first stage I created a Scraper class containing methods to gather data from bestselling science and technology publications listed on the website of Waterstones, a popular book store. This included methods to visit the website, accept cookies, gather book URL's, store them in a list then navigate to the next page.
This is iterated as many times as desired to generate a list of individual book URL's that will be visited and scraped for data in the next milestone.
The class was initialised using Selenium WebDriver as an API with Google Chrome.

