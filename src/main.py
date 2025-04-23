# from urllib.request import urlopen
import boto3
from store_extractor import StoreExtractor
from constants import Constants as cs

from scraper import Scraper
from tj_scraper import TraderJoesScraper
from hp_scraper import HanpoomScraper


class LambdaWrapper:
    def __init__(self, event, context):
        self.event = event
        self.context = context

    def main(self):
        store = self.event['store'].replace(" ","").lower()
        scraper = None
        if cs.TJ_NAME == store or cs.TJ_ABBREV == store:
            store = cs.TJ_ABBREV
            scraper = TraderJoesScraper()
        elif cs.HP_NAME == store or cs.HP_NAME == store:
            store = cs.HP_ABBREV
            scraper = HanpoomScraper()
        else:
            raise NotImplementedError
        # should I make config an instance var?
        config = StoreExtractor(store).get_store()
        scraper.set(config)

        return scraper.extract()


# if __name__ == "__main__":
#     main()
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html_doc, 'html.parser')
#
# for link in soup.find_all('a'):
#     print(link.get('href'))
# # http://example.com/elsie
# # http://example.com/lacie
# # http://example.com/tillie
