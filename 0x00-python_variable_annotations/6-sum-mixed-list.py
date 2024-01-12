#!/usr/bin/env python3
"""
py module
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    mix of float and integers whthin a list
    """
    return sum(mxd_lst)
