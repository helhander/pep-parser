import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        all_peps = response.xpath(
            "//tr[descendant::abbr]//td[descendant::a][1]/a"
        )
        for pep_link in all_peps:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        title_parts = (
            response.xpath('//h1[@class="page-title"]//text()').get().split()
        )
        yield PepParseItem(
            {
                'number': int(title_parts[1]),
                'name': ' '.join(title_parts[3:]),
                'status': response.xpath(
                    "//dt[text()='Status']/following-sibling::dd[1]//text()"
                ).get(),
            }
        )
