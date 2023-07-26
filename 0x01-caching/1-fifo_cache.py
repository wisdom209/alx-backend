#!/usr/bin/env python3
"""Caching module"""
from collections import deque
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching class"""

    def __init__(self):
        """initialize """
        super().__init__()
        self.key_queue = deque()

    def put(self, key, item):
        """Add an item to cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS\
                    and key not in self.cache_data:
                    deleted_key = self.key_queue.popleft()
                    del self.cache_data[deleted_key]
                    print(f"DISCARD {deleted_key}")

            self.cache_data[key] = item
            self.key_queue.append(key)

    def get(self, key):
        """get from cache"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
