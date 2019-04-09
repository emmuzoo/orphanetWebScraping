# orphanetWebScraping
Consgrucion de un dataset de enfermedades raras


pip install scrapy

scrapy startproject orphanetCrawler
cd orphanetCrawler
scrapy genspider -t crawl orphanet www.orpha.net

scrapy crawl orphanet -o report.csv -t csv -s LOG_FILE=orphanCrawl.log
