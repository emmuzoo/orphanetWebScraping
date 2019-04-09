# -*- coding: utf-8 -*-

from scrapy.exporters import BaseItemExporter
import io
import csv


class CsvItemExporter(BaseItemExporter):
	fieldnames_standard = ['orphan', 'name']
	
	def __init__(self, file, **kwargs):
		self._configure(kwargs)
		if not self.encoding:
			self.encoding = 'utf-8'

		self.file = io.TextIOWrapper(file,
									line_buffering=False,
									write_through=True,
									encoding=self.encoding)
		self.file.truncate(0)
		self.items = []

	def finish_exporting(self):
		writer = csv.DictWriter(self.file,
								fieldnames=self.__get_fieldnames(),
								delimiter=';', 
								quotechar='\"', 
								quoting=csv.QUOTE_ALL,
								lineterminator='\n')
		writer.writeheader()
		for item in self.items:
			writer.writerow(item)
	
	def export_item(self, item):
		new_item = dict(item)
		self.items.append(new_item)
		return item

	def __get_fieldnames(self):
		field_names = set()
		for product in self.items:
			for key in product.keys():
				if key not in self.fieldnames_standard:
					field_names.add(key)
		return self.fieldnames_standard + list(field_names)