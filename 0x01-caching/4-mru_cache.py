#!/usr/bin/env python3
"""Caching module"""
from collections import deque
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """LRU caching class"""

    def __init__(self):
        """initialize """
        super().__init__()
        self.key_queue = []

    def put(self, key, item):
        """Add an item to cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS\
                    and key not in self.cache_data:
                mr_key = self.key_queue.pop()
                self.cache_data.pop(mr_key)
                print(f"DISCARD: {mr_key}")
        if key in self.cache_data:
            self.key_queue.remove(key)
        self.cache_data[key] = item
        self.key_queue.append(key)

    def get(self, key):
        """get from cache"""
        if key is not None and key in self.cache_data:
            self.key_queue.remove(key)
            self.key_queue.append(key)
            return self.cache_data[key]
        return None
