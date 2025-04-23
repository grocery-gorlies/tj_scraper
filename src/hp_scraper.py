import requests

from scraper import Scraper
from bs4 import BeautifulSoup
from stores.hanpoom import Hanpoom
from store_extractor import StoreExtractor

class HanpoomScraper(Scraper):
    def set(self, config: Hanpoom):
        self.config = config