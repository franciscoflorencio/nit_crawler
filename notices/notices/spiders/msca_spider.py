import scrapy
from scrapy_splash import SplashRequest
from notices.items import MarieCurieItem

class MscaSpider(scrapy.Spider):
    name = "msca"
    
    lua_script = """
    function main(splash, args)
      splash.images_enabled = false
      splash.private_mode_enabled = false
      splash:set_user_agent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")
      assert(splash:go(args.url))
      assert(splash:wait(3))
      return {
        html = splash:html(),
      }
    end
    """
    
    def start_requests(self):
        url = 'https://marie-sklodowska-curie-actions.ec.europa.eu/funding'
        yield SplashRequest(
            url=url, 
            callback=self.parse,
            endpoint='execute',
            args={'lua_source': self.lua_script},
        )

    def parse(self, response):
        for funding in response.css('article.eac-calls-teaser'):
            item = MarieCurieItem()
            item['title'] = funding.css('h3::text').get()
            item['status'] = funding.css('span.deadline-time::text').get()
            item['link'] = funding.css('a::attr(href)').get()
            yield item
