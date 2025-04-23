from stores.store import Store


class TraderJoes(Store):
    def __init__(self, url): #(self, url, method, data):
        self.url = url
        # self.method = method
        # self.data = data


def as_tj(dct):
    # object_hook has trouble parsing nested json - research for future
    print(f"reading in as_tj {dct}")
    return TraderJoes(dct['url'])
#    return TraderJoes(dct['action'], dct['method'], dct['data'])
