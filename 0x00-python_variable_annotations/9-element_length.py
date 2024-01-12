#!/usr/bin/env python3
"""
py module
"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    matrix elements lenght
    """
    return [(i, len(i)) for i in lst]
