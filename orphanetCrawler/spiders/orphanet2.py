# -*- coding: utf-8 -*-
from scrapy.spiders import CSVFeedSpider


class Orphanet2Spider(CSVFeedSpider):
    name = 'orphanet2'
    allowed_domains = ['www.orpha.net']
    start_urls = ['http://www.orpha.net/feed.csv']
    # headers = ['id', 'name', 'description', 'image_link']
    # delimiter = '\t'

    # Do any adaptations you need here
    #def adapt_response(self, response):
    #    return response

    def parse_row(self, response, row):
        i = {}
        #i['url'] = row['url']
        #i['name'] = row['name']
        #i['description'] = row['description']
        return i
