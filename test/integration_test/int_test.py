from store_extractor import StoreExtractor
from constants import Constants as cs

from tj_scraper import TraderJoesScraper
from hp_scraper import HanpoomScraper
from unittest import TestCase


class TestIntegration(TestCase):
    def test_tj(self):
        store = cs.TJ_ABBREV
        scraper = TraderJoesScraper()
        config = StoreExtractor(store).get_store()
        scraper.set(config)
        extracted = scraper.extract()
        assert True


    def test_hp(self):
        store = cs.HP_ABBREV
        scraper = HanpoomScraper()
        config = StoreExtractor(store).get_store()
        scraper.set(config)
        extracted = scraper.extract()
        assert True