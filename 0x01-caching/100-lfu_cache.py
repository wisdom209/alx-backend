#!/usr/bin/env python3
"""LFU caching"""
from collections import defaultdict, deque
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """LFU Caching"""

    def __init__(self):
        """initialise class"""
        super().__init__()
        self.freq = defaultdict(int)
        self.freq_deque_dict = defaultdict(deque)

    def put(self, key, item):
        """add item"""
        if key is not None and item is not None:
            if key in self.cache_data:
                curr_freq = self.freq[key]
                self.freq_deque_dict[curr_freq].remove(key)
                self.freq[key] += 1
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS\
                        and key not in self.cache_data:
                    min_freq = min(self.freq.values())

                    while self.freq_deque_dict[min_freq] and\
                            len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                        for_removal_key = self.freq_deque_dict[min_freq].popleft()  # nopep8
                        print(f"DISCARD: {for_removal_key}")
                        self.cache_data.pop(for_removal_key)
                        self.freq.pop(for_removal_key)

                self.cache_data[key] = item
                self.freq[key] += 1
            self.freq_deque_dict[self.freq[key]].append(key)
            self.cache_data[key] = item

    def get(self, key):
        """get item
        """
        if key is not None and key in self.cache_data:
            curr = self.freq[key]
            next = curr + 1
            self.freq[key] = next

            self.freq_deque_dict[curr].remove(key)
            self.freq_deque_dict[next].append(key)

            # Return the value associated with the key
            return self.cache_data[key]

        # Key is not in the cache, return None
        return None
