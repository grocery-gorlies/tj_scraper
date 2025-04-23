from stores.store import Store


class Hanpoom(Store, object):
    def __init__(self, url):
        self.url = url


def as_hp(dct):
    return Hanpoom(dct['url'])
    # return Hanpoom(dct['action'], dct['method'], dct['data'])