from scrapy import Spider


class QuotesSpipder(Spider):
    name = 'quotes'
    start_urls = ['https://quotes.toscrape.com/api/quotes?page=1']

    def parse(self, response):
        data = response.json()
        for quote in data['quotes']:
            yield {
                'author': quote['author']['name'],
                'text': quote['text'],
            }

        next_page = data['has_next']
        if next_page:
            next_page_number = data['page'] + 1
            yield response.follow(f'https://quotes.toscrape.com/api/quotes?page={next_page_number}')