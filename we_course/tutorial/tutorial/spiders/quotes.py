# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
	name = 'quotes'
	allowed_domains = ['quotes.toscrape.com']

	def start_requests(self):
		urls = [
			'http://quotes.toscrape.com/page/1/',
			'http://quotes.toscrape.com/page/2/']

		for url in urls:
			yield scrapy.Request(url = url,callback = self.parse)

	def parse(self, response):
		page = response.url.split('/')[-2]
		file_name = 'quotes-{}.html'.format(page)
		with open(file_name,'wb') as f:
			f.writer(response.body)
		self.log('Saved file {}'.format(file_name))

