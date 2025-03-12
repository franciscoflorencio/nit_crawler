import scrapy
import re

class CnpqSpider(scrapy.Spider):
    name = "cnpq"
    allowed_domains = ["memoria2.cnpq.br"]
    start_urls = ["http://memoria2.cnpq.br/web/guest/chamadas-publicas"]


    def parse(self, response):
        notices = response.css('div.content')
        titles = notices.css('h4::text').getall()

        description = notices.css('p::text').getall()
        transformed_description = []
        for item in description:
            if item.startswith('\n'):
                transformed_description[-1] += item
            else:
                transformed_description.append(item)
        description = transformed_description

        inscriptions = notices.css('div.inscricao')
        deadline = inscriptions.css('li::text').getall()

        bottoms = response.css('div.bottom-content')
        row_fluid = bottoms.css('div.row-fluid')


        for i in range(len(notices)):
            yield {
                'title': titles[i],
                'description': description[i],
                'deadline': deadline[i],
                'link': row_fluid.css('a.btn')[i].attrib['href']

            }

        

        