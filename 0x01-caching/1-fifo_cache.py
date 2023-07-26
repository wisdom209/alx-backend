#!/usr/bin/env python3
"""Caching module"""
from collections import deque
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching class"""

    def __init__(self):
        """initialize """
        super().__init__()
        self.key_queue = []

    def put(self, key, item):
        """Add an item to cache"""
        if key is not None and item is not None and key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_item = self.key_queue.pop(0)
                del self.cache_data[first_item]
                print(f"DISCARD: {first_item}")
        self.cache_data[key] = item
        self.key_queue.append(key)

    def get(self, key):
        """get from cache"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
