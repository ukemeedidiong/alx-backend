#!/usr/bin/python3
"""
FIFO caching
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFO cache
    """

    def __init__(self):
        """
        constructor
        """
        self.order = []
        super().__init__()

    def put(self, key, item):
        """
        add to the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard = self.order[0]
            del self.cache_data[discard]
            del self.order[0]
            print("DISCARD: {}".format(discard))

    def get(self, key):
        """
        get the cache item value
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
