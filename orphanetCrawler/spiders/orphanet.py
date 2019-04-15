# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


from orphanetCrawler.items import OrphanetCrawlerItem

attr2fields = {
	'Synonym(s)': 'synonyms',
    'Inheritance': 'inheritance',
	'Prevalence': 'prevalence',
	'Age of onset': 'ageOfonset',
	'ICD-10': 'ICD10',
	'OMIM': 'OMIM',
	'UMLS': 'UMLS',
	'MeSH': 'MeSH',
	'GARD': 'GARD',
	'MedDRA': 'MedDRA'
}

class OrphanetSpider(CrawlSpider):
	name = 'orphanet'
	allowed_domains = ['www.orpha.net']
	start_urls = ['https://www.orpha.net/consor/cgi-bin/Disease_Search.php?lng=EN&search=Disease_Search_List']
    
	rules = (
		Rule(LinkExtractor(allow=(), restrict_xpaths=("//ul[@class='alphabet']/li/a")), follow=True),
		Rule(LinkExtractor(allow=(), restrict_xpaths=('//div[@id="result-box"]/ul/li/a')), callback='parse_item', follow=True),
	)
	
	def parse_item(self, response):
		item = {}
		# Information
		item = OrphanetCrawlerItem()
		info = response.css("div.idcard")
		item["name"] = response.xpath("//title/text()").get()
		item["orphan"] = info.xpath("./h3/text()").get()
		item["url"] = response.url
		for property in info.css("ul.idData li"):
			#print(property)
			attr = property.xpath("./em/text()").get()
			if attr:
				attr = attr.strip().replace(':', '')
				#xprint(attr)
				attr = attr2fields.get(attr)
				#print(attr)
				
				#val = property.xpath("./em/following-sibling::*");
				#print(val)
				
				values = property.xpath("./ul/li/strong/text()").getall()
				if values:
					item[attr] = ', '.join(values)
					#print("{} => {}", attr, item[attr])
					continue
				
				values = property.xpath("./strong/a/text()").getall()
				if values:
					item[attr] = ', '.join(values)
					#print("{} => {}", attr, item[attr])
					continue
				
				values = property.xpath("./strong/text()").getall()
				if values:
					item[attr] = ' '.join(values)
					#print("{} => {}", attr, item[attr])
					continue
				
		
		item["last_updated"] = response.xpath('//div[@class="articleInfo"]/p[@class="author"]/strong[2]/text()').get()
		
		
		# Additional Information
		addinfo = response.css("div.articleAdd")
		#print(addinfo.get())
		
		pubmed = addinfo.xpath('./ul/li/a[contains(text(),"Publications in PubMed")]')
		
		if pubmed is not None:
			item["pubMed"] = pubmed.css("::text").get()
		#print(item)
        
		
		yield item
	