# orphanetWebScraping
Construcción de un dataset de enfermedades raras

## Intalación de dependencias
Para realizar este proyecto se ha utilizado python 3.7 y Scrapy. Scrapy es un framework de código abierto y colaborativo para extraer datos de sitios web. Para instalar scrapy abrimos una ventana de línea de comandos y ejecutamos el siguiente comando.

pip install scrapy

## Creación de Proyecto
Para crear un proyecto con scrapy en la línea de comandos ejecutamos lo siguiente.

scrapy startproject orphanetCrawler

Rebombramos el directorio "orphanetCrawler" a "orphanetWebScraping".

## Creación de Spider
Para crear el spider en la línea de comandos ejecutamos lo siguiente.

cd orphanetWebScraping
scrapy genspider -t crawl orphanet www.orpha.net

## Ejecución del Spider
Para crear el dataset ejecutamos en la línea de comandos ejecutamos lo siguiente

scrapy crawl orphanet -o report.csv -t csv -s LOG_FILE=orphanCrawl.log
