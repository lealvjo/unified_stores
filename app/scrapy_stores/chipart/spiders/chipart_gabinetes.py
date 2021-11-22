import scrapy


class ChipartGabinetesSpider(scrapy.Spider):
    name = 'chipart_gabinetes'
    allowed_domains = ['chipart.com.br']
    start_urls = ['https://www.chipart.com.br/gabinete/']

    custom_settings = {
        "FEED_URI": "chipart_gabinetes_%(time)s.json",
        "FEED_FORMAT": "json"
    }

    def parse(self, response):
        print("procesing:" + response.url)

        # data extraction
        product_name = response.xpath("//h2[@class='text']/text()").extract()
        price_total = response.xpath(
            '//div[@class="creditcard"]/div[@class="product-price-final"]/div[@class="installments"]/span[@class="price total"]/text()').extract()
        product_url = response.css('div::attr(data-product-url)').getall()
        row_data = zip(product_url, product_name, price_total)

        # Making extracted data row wise
        for item in row_data:
            # create a dictionary to store the scraped info
            scraped_info = {
                'source': item[0],
                'product_name': item[1].strip(),
                # item[0] means product in the list and so on, index tells what value to assign
                'price_total': item[2]
            }
            print(row_data)
            # yield or give the scraped info to scrapy
            yield scraped_info


"""
            NEXT_PAGE_SELECTOR = '.paginate__item paginate__item--next + a::attr(href)'
            next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
            if next_page:
                yield scrapy.Request(
                    response.urljoin(next_page),
                    callback=self.parse)
"""
