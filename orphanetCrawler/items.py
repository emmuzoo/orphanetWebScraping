# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item

class OrphanetCrawlerItem(Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	orphan = Field()
	name   = Field()
	synonyms = Field()
	inheritance = Field()
	prevalence = Field()
	ageOfonset = Field()
	ICD10 = Field()
	OMIM  = Field()
	UMLS  = Field()
	MeSH  = Field()
	GARD  = Field()
	MedDRA = Field()
	pubMed = Field()
	url = Field()
	last_updated = Field(serializer=str)
    