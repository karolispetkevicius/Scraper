import sys
import os

'''
# Get the path to the directory containing this script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Get the path to the parent directory (project root)
project_directory = os.path.dirname(script_directory)

# Add the project directory to the system path
sys.path.append(project_directory)
'''

import json
import scrapy
from scrapy_splash import SplashRequest
from Slack_Scraper.data_parsing import parse_app_page
import time
from scrapy.crawler import CrawlerProcess
from Slack_Scraper.pipelines import MongoDBPipeline


class MySpider(scrapy.Spider):
    name = 'slack_apps'
    allowed_domains = ['slack.com']
    start_urls = ['https://slack.com/apps']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.follow_categories, args={'wait': 2}, endpoint='render.html')


    def follow_categories(self, response):
        categories = response.css('a.sidebar_menu_list_item::attr(href)').getall()[15:16]
        for category in categories:
            yield SplashRequest(response.urljoin(category), callback=self.parse_category, args={'wait': 2},
                                 endpoint='render.html')

  
    def parse_category(self, response):

        apps = response.css('li.app_row.interactive')
 
        for app in apps:
            category = response.xpath('//h1[@class="page_title_text"]/text()').get()
            ranking = app.css('li.interactive::attr(data-position)').get()
            link = app.css('a.media_list_inner::attr(href)').get()
            yield SplashRequest(response.urljoin(link), callback=self.app_data, args={'wait': 2},
                                 meta={'category':category, 'ranking':ranking}, endpoint='render.html')

        next_page = response.css('a.btn_small.btn.float_right::attr(href)').get()
        if next_page is not None:
            yield SplashRequest(response.urljoin(next_page), args={'wait': 2}, callback=self.parse_category)




    def app_data(self, response):
        full_html = response.text
        category = response.meta.get('category')
        ranking = response.meta.get('ranking')
        app_data = parse_app_page(full_html, category, ranking)
        
        yield app_data



'''
if __name__ == "__main__":
    # Start the timer for the whole script
    total_start_time = time.time()

    # Create a Scrapy process and start the spider
    settings = {}
    process = CrawlerProcess(settings)
    process.crawl(MySpider)
    process.start()

    # End the timer
    total_end_time = time.time()

    # Calculate the elapsed time
    total_elapsed_time = total_end_time - total_start_time
    print(f"Total script execution time: {total_elapsed_time:.2f} seconds")

    '''