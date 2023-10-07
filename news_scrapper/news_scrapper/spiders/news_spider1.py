import scrapy


class NewsSpider1Spider(scrapy.Spider):
    name = 'news_spider1'
    allowed_domains = ['dailyhodl.com/']
    start_urls = ['https://dailyhodl.com/']

    def parse(self, response):
        articles = response.css("article.jeg_post.jeg_pl_lg_2.format-standard")

        for article in articles:
            yield{
                "title" : article.css("h3 a::text").get(),
                "excerpt" : article.css("div.jeg_post_excerpt p::text").get(),
                "thumb" : article.css("img.attachment-jnews-350x250.size-jnews-350x250.wp-post-image ").attrib["src"],
                "date" : article.css("div.jeg_meta_date a::text").get().strip(),
                "src_news_website" : "The Daily Hodl"
            }