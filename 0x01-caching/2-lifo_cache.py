#!/usr/bin/python3
"""
LIFO Caching
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFO class
    """

    def __init__(self):
        """
        constructor
        """
        self.discard = None
        super().__init__()

    def put(self, key, item):
        """
        add to the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            del self.cache_data[self.discard]
            print("DISCARD: {}".format(self.discard))

        if key is not None:
            self.discard = key

    def get(self, key):
        """
        get the cache item value
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
