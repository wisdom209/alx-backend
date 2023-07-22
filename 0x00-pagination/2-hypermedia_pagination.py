#!/usr/bin/env python3
"""Pagination Backend"""
import csv
import math
from typing import Tuple, List, Dict


def index_range(page: int, page_size: int) -> Tuple:
    """Get the index range"""
    start_index = (page - 1) * page_size
    end_index = ((page - 1) * page_size)+page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get required page"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page > 0

        page_range = index_range(page, page_size)
        dataset = self.dataset()
        if page * page_size >= len(dataset):
            return []
        return dataset[page_range[0]: page_range[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        page_range = self.get_page(page, page_size)
        return {
            'page_size': len(page_range),
            'page': page,
            'data': page_range,
            'next_page': (page + 1) if len(self.get_page(page, page_size)) > 0 else None,  # nopep8
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': math.ceil(len(self.dataset()) / page_size)
        }
