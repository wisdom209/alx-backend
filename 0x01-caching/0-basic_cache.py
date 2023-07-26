#!/usr/bin/env python3
"""basic caching"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Basic Cache class"""

    def put(self, key, item):
        """add to cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """get from cache"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
