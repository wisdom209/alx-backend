#!/usr/bin/env python3
"""FIFO caching"""
from collections import deque
Base = __import__('base_caching').BaseCaching


class FIFOCache(Base):
    """FIFO Cache implementation"""

    def __init__(self):
        """initialise the init class"""
        super().__init__()
        self.queue = deque()

    def put(self, key, item):
        """method that puts the key-value pairs in the FIFO algo"""
        if key is not None and item is not None and key not in self.cache_data:
            if len(self.cache_data) >= Base.MAX_ITEMS:
                oldest_item = self.queue.popleft()
                self.cache_data.pop(oldest_item)
                print("DISCARD: {}".format(oldest_item))
        self.cache_data[key] = item
        self.queue.append(key)

    def get(self, key):
        """get the values in the FIFO algorithm"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
