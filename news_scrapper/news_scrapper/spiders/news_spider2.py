import scrapy


class NewsSpider2Spider(scrapy.Spider):
    name = 'news_spider2'
    allowed_domains = ['finbold.com']
    start_urls = ['https://finbold.com/category/cryptocurrency-news/']

    def parse(self, response):
        articles = response.css("div.flex.gap-x-4")
        relative_url = response.css("a.relative[aria-label='pagination.next']::attr(href)").get()
        print(f"relative url: {relative_url}")

        for article in articles:

            article_url = article.css("h3 a").attrib["href"]
            yield response.follow(article_url, callback = self.parse_article_page)

        if relative_url is not None:
            next_page = "https://finbold.com" + relative_url
            print(f"\n\n{next_page}\n\n")
        yield response.follow(next_page, callback = self.parse)


    def parse_article_page(self, response):
        print("this function is entered")

        yield{
            "title" : response.css("h1.entry-title::text").get(),
            "excerpt" : response.css("p.paragraph").get(),
            "thumb" : response.css("img.attachment-large::attr(src)").get(),
            "date" : response.css("time.updated::text").get(),
            "src_news_website" : "Finbold"
        }
