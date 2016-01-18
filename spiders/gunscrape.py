from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

class gunscrapecode(BaseSpider):
	name = "gunscrape"
	allowed_domains = ['http://gunbroker.com']
	start_urls = [
	"http://www.gunbroker.com/Semi-Auto-Pistols/BI.aspx?Keywords=glock&mfg=1000120&mo=3000845"
	]

	def parse(self, response):
		for x in response.xpath('//tr'):
			print x.xpath('a[@class="BItmTLnk"]/text()').extract()




	# gun titles: response.xpath('//a[@class="BItmTLnk"]/text()').extract()
	# gun price: response.xpath('//td[@class="lrt"]/text()').extract()
	# time left: response.xpath('//td[@class="lrt nw"]/text()').extract()

		