import requests

from scraper import Scraper
from bs4 import BeautifulSoup
from stores.trader_joes import TraderJoes
from store_extractor import StoreExtractor

class TraderJoesScraper(Scraper):
    def set(self, config: TraderJoes):
        if config is None:
            raise NotImplementedError # say config not properly set for tj's
        self.config = config

    def extract_links(self):
        pass

    def extract(self):
        print(self.config.url)
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(self.config.url, headers=headers).content
        soup = BeautifulSoup(response, "lxml")
        #response = requests.get(self.config.url)
        #soup = BeautifulSoup(response.text, "lxml")
        sample = soup.find_all('ul', class_ = "ProductList_productList__list__3-dGs")
        print(len(sample))
        print("____________________________________________________________________________")
        print(sample)
        return "implement get links"

    #/html/body/div[1]/div[1]/div[1]/div/div[1]/div/div[2]/main/div/div/div/div[1]/div/div/div[1]
    #<div class="ProductCategory_productCategory__2duGJ margin-bottom-xl">
    #<ul class="ProductList_productList__list__3-dGs"><li class="ProductList_productList__item__1EIvq"><section class="ProductCard_card__4WAOg ProductCard_card_verticalCard__1qP8Z ProductCard_card_mobile__2Au8n"><a class="Link_link__1AZfr ProductCard_card__img_link__2bBqA" tabindex="-1" href="/home/products/pdp/kerrygold-irish-cheddar-with-chili-peppers-071631">