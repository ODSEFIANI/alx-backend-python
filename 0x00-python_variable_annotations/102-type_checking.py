#!/usr/bin/env python3
'''Task 11's module.
'''
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    sequence
    """
    zoomed_in: List = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in
