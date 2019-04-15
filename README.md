# orphanetWebScraping
Construcción de un dataset de enfermedades raras

## Instalación de dependencias
Para realizar este proyecto se ha utilizado python 3.7 y Scrapy. Scrapy es un framework de código abierto y colaborativo para extraer datos de sitios web. Para instalar scrapy abrimos una ventana de línea de comandos y ejecutamos el siguiente comando.

pip install scrapy

## Creación de Proyecto
Para crear un proyecto con scrapy en la línea de comandos ejecutamos lo siguiente.

scrapy startproject orphanetCrawler

Renombramos el directorio "orphanetCrawler" a "orphanetWebScraping".

## Creación de Spider
Para crear el spider en la línea de comandos ejecutamos lo siguiente.

cd orphanetWebScraping

scrapy genspider -t crawl orphanet www.orpha.net

## Ejecución del Spider
Para crear el dataset ejecutamos en la línea de comandos ejecutamos lo siguiente

scrapy crawl orphanet -o report.csv -t csv -s LOG_FILE=orphanCrawl.log

## Descripción de los ficheros
| Nombre del Fichero | Decripción |
|--------------------|------------|
| orphanetCrawler <ul><li>&#95;&#95;pycache&#95;&#95;</li><li>spiders</li><li>&#95;&#95;init&#95;&#95;.py</li><li>exporters.py</li><li>items.py</li><li>middlewares.py</li><li>pipelines.py</li><li>settings.py</li></ul> | Carpeta con el código del crawler <ul><li>Carpeta con la cache autogenerada por scrappy</li><li>Carpeta con la lógica de navegación y extracción</li><li>Fichero autogenerado por Scrapy</li><li>Fichero con lógica de exportación (separadores) </li><li>Fichero con la estructura del objeto a recolectar incluyendo los campos (Abstracción de la ER)</li><li>Fichero con la configuración generada por scrapy</li><li>Definición del proceso de iteración de los elementos, generado por scrapy</li><li>Configuraciones importantes como la de seguir o no las reglas del fichero robots.txt</li></ul> |
| README.md	| Fichero que contiene información del proyecto y de los ficheros|
| aditional_information.PNG | Captura de pantalla del recuadro de información adicional de la ER|
| alphabetical_list.PNG	| Captura de pantalla del listado alfabetico de las ER|
| disease.PNG	| Captura de pantalla de la ER |
| orphanCrawl.log | Fichero con los logs de la ejecución del crawler |
| rared_diseases_zebra.png | Imagen representativa del dataset |
| report.csv | Dataset generado que contiene todas las ER con su información recolectadas de www.orpha.net|
| scrapy.cfg | Fichero de configuración de scrapy|
| PRACTICA1.pdf | Fichero PDF con el informe de la práctica|
