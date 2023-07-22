#!/usr/bin/env python3
"""Pagination Backend"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """Get the index range"""
    start_index = (page - 1) * page_size
    end_index = ((page - 1) * page_size)+page_size
    return (start_index, end_index)
