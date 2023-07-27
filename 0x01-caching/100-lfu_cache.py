#!/usr/bin/env python3
"""LFU caching"""
from collections import defaultdict, deque
Base = __import__('base_caching').BaseCaching


class LFUCache(Base):
    """LFU Cache implementation"""

    def __init__(self):
        """initialise the init class"""
        super().__init__()
        self.freq = defaultdict(int)
        self.freq_items = defaultdict(deque)

    def put(self, key, item):
        """method that puts the key-value pairs in the LFU algo"""
        if key is not None and item is not None:
            if key in self.cache_data:
                curr_freq = self.freq[key]
                self.freq_items[curr_freq].remove(key)
                self.freq[key] += 1
            else:
                if len(self.cache_data) >= Base.MAX_ITEMS and key not in self.cache_data:  # nopep8
                    min_freq = min(self.freq.values())

                    while self.freq_items[min_freq] and len(self.cache_data) >= Base.MAX_ITEMS:  # nopep8
                        key_to_pop = self.freq_items[min_freq].popleft()
                        print("DISCARD: {}".format(key_to_pop))
                        del self.cache_data[key_to_pop]
                        del self.freq[key_to_pop]

                self.cache_data[key] = item
                self.freq[key] += 1
            self.freq_items[self.freq[key]].append(key)
            self.cache_data[key] = item

    def get(self, key):
        """get the values in the LFU algorithm"""
        if key is not None and key in self.cache_data:
            curr_freq = self.freq[key]
            next_freq = curr_freq + 1
            self.freq[key] = next_freq

            self.freq_items[curr_freq].remove(key)
            self.freq_items[next_freq].append(key)
            return self.cache_data[key]
        return None
