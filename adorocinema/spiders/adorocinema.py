from scrapy import Spider
from adorocinema.items import MovieItem, MovieItemLoader


class AdoroCinemaSpider(Spider):
    name = "adorocinema"
    start_urls = ["https://www.adorocinema.com/filmes/melhores/",]

    page = 1
    def parse(self, response):
        movies = response.xpath("//div[contains(@class,'card-list')]")
        for movie in movies:
            title = movie.css("a.meta-title-link::text").get()
            duration = movie.css("div.meta-body-item.meta-body-info::text").get()
            original_title = movie.xpath("div[1]//div[@class='meta-body-item']/span[2]/text()").getall()
            

            if len(original_title) == 0:
                original_title = title

            item_loader = MovieItemLoader(item=MovieItem(), selector=movie)
            item_loader.add_value("title", title)
            item_loader.add_value("duration", duration)
            item_loader.add_value("original_title", original_title)
    
            yield item_loader.load_item()
        self.page += 1
        next_page = f"https://www.adorocinema.com/filmes/melhores/?page={self.page}"
        yield response.follow(next_page, callback=self.parse)