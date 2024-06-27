#!/usr/bin/python3
"""
LRU Caching
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRU class
    """

    def __init__(self):
        """
        constructor
        """
        self.timesKey = {}
        self.time = 0
        super().__init__()

    def put(self, key, item):
        """
        add to the cache
        """
        if key is not None and item is not None:
            # modify the time and change the next newer value
            self.timesKey[key] = self.time
            self.time += 1

            # add the new item
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard_key = None
            older = self.time

            for _key, _value in self.timesKey.items():
                if older > _value:
                    older = _value
                    discard_key = _key

            # del key in time and cache data
            del self.cache_data[discard_key]
            del self.timesKey[discard_key]

            print("DISCARD: {}".format(discard_key))

    def get(self, key):
        """
        get the cache item value
        """
        if key is None or key not in self.cache_data:
            return None

        # modify the time and change the next newer value
        self.timesKey[key] = self.time
        self.time += 1

        return self.cache_data[key]
