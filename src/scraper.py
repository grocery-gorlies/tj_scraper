import requests
from stores.store import Store
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, store: Store = None):
        self.store = store

    def set(self, store: Store):
        if self.store is None:
            raise NotImplementedError # add error statement
            # with config.abbreviavted name
        pass

    def extract_links(self) -> list:
        pass

    def extract_page(self, link) -> list:
        pass

    def extract(self):
        if self.config is None:
            print("no configuration information set - unable to extract")
        links = self.extract_links()
        products = []
        # create object for product
        # list of dict objects
        for link in links:
            products.append(self.extract_page(link))
        return products