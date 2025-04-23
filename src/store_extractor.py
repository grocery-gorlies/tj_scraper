import json
import os
from stores.trader_joes import *
from stores.hanpoom import *
#from gc import get_threshold

from constants import Constants as cs
from typing import Self


class StoreExtractor:
    def __init__(self, store: str):
        self.store = store

    def store(self):
        return self.store

    def get_tj(self) -> TraderJoes:
        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))
        path = os.path.join(__location__, cs.TJ_CONFIG)
        tj = None
        # with open(path) as f1:
        #     print(f"reading: \"{f1.read()}\"")
        # with open(path) as f2:
        #     print(f"reading 2: \"{f2.read()}\"")
        with open(path) as f:
            print("reading main: ")
            tj = json.load(f, object_hook=as_tj)
        return tj

    def get_hp(self) -> Hanpoom:
        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))
        path = os.path.join(__location__, cs.HP_CONFIG)
        hp = None
        with open(path) as f:
            hp = json.load(f, object_hook=as_hp)
        return hp

    def get_store(self) -> Store:
        storeConfig = None
        if self.store == cs.TJ_ABBREV:
            storeConfig = self.get_tj()
        elif self.store == cs.HP_ABBREV:
            storeConfig = self.get_hp()
        return storeConfig

"""
class Dict(dict):
    dot.notation access to dictionary attributes
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    @staticmethod
    def load_json(path: str) -> dict:
        with open(path, "r") as f:
            result = Configuration.__load__(json.loads(f.read()))
        return result

    @staticmethod
    def __load__(data):
        if type(data) is dict:
            return Configuration.load_dict(data)
        elif type(data) is list:
            return Configuration.load_list(data)
        else:
            return data

    @staticmethod
    def load_dict(data: dict):
        result = dict()
        for key, value in data.items():
            result[key] = Configuration.__load__(value)
        return result

    # is this necessary?? test out
    @staticmethod
    def load_list(data: list):
        result = [Configuration.__load__(item) for item in data]
        return result
"""