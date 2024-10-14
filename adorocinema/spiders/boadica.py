from scrapy import Request, Spider


class BoadicaSpider(Spider):
    name = 'boadica'
    # start_urls = ['htts://boadica.com.br/WebApi/api/pesquisa/precos']
    url = 'https://boadica.com.br/WebApi/api/pesquisa/precos'
    curPage = 1
    headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json, text/plain, */*',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
        }
    body = ('{"Slug":"mem_cpu","CodProduto":null,"Regiao":null,'
            '"PrecoMin":null,"PrecoMax":null,"CodLoja":null,'
            '"EmBox":null,"ClasseProdutoX":3,"CodCategoriaX":14,'
            f'"XT":9,"XK":11,"CurPage":{curPage}'
            '}'
    )
    

    def start_requests(self):
        
        yield Request(
            self.url, 
            method="POST",
            headers=self.headers,
            body=self.body, 
            callback=self.parse, 
        )


    def parse(self, response):
        data = response.json()
        for product in data['precos']:
            yield {
                'name': product['especificacao'],
                'price': product['preco'],
            }

        pages = data['paginas']
        if self.curPage < pages:
            self.curPage = self.curPage + 1
            body = ('{"Slug":"mem_cpu","CodProduto":null,"Regiao":null,'
            '"PrecoMin":null,"PrecoMax":null,"CodLoja":null,'
            '"EmBox":null,"ClasseProdutoX":3,"CodCategoriaX":14,'
            f'"XT":9,"XK":11,"CurPage":{self.curPage}'
            '}'
    )
        
            yield Request(
            self.url, 
            method="POST",
            headers=self.headers,
            body=body, 
            callback=self.parse, 
        )