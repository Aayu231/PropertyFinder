import scrapy

class QuotesSpider(scrapy.Spider):
    name = "real"
    allowed_domains = ["olx.in"]
    start_urls = [
    'https://www.olx.in/items/q-properties?filter=lang_eq_en%2Cplatform_eq_web-desktop%2Cquery_eq_properties%2Cspellcheck_eq_true&facet_limit=100&location_facet_limit=20&sorting=desc-creation&user=1759e799156x270bfcaa',
    'https://www.olx.in/kerala_g2001160/q-properties?isSearchCall=true',
    'https://www.olx.in/maharashtra_g2001163/q-properties?isSearchCall=true',
    'https://www.olx.in/uttar-pradesh_g2001176/q-properties?isSearchCall=true',
    'https://www.olx.in/tamil-nadu_g2001173/q-properties?isSearchCall=true',
    ]

    def parse(self, response):
        quotes = response.xpath('//*[@class="EIR5N"]')
        for quote in quotes:
            url = "www.olx.in" + quote.xpath('.//a/@href').extract_first()
            price = quote.xpath('.//*[@class="_89yzn"]/text()').extract_first()
            price = price[1:]
            price = price.replace(',','')
            price = price.strip()
            price = int(price)

            title = quote.xpath('.//*[@class="_2tW1I"]/text()').extract_first()
            details = quote.xpath('.//*[@class="_2TVI3"]/text()').extract_first()
            if(details is None):
                details = 'No Information Provided'
            location = quote.xpath('.//*[@class="tjgMj"]/text()').extract_first()
            when = quote.xpath('.//*[@class="zLvFQ"]/span/text()').extract_first()
            if(when == 'Today'):
                when = 'Nov 08'

            yield{'Url':url,
                  'Price':price,
                  'Details':details,
                  'Location':location,
                  'Posted On':when,
                  'Extra-Information':title}

        next_page_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield scrapy.Request(absolute_next_page_url)
