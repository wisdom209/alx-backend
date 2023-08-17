#!/usr/bin/env python3
import numpy as np


def rotate_2d_matrix(matrix):
    """rotate 2d matrix"""
    new = np.rot90(matrix, 3)
    for index, item in enumerate(new):
        matrix[index] = item.tolist()
