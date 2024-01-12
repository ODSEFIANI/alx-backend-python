#!/usr/bin/env python3
"""
py module
odsefiani
"""
from typing import List, Tuple, Sequence, Iterable, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    sequence
    """
    if lst:
        return lst[0]
    else:
        return None