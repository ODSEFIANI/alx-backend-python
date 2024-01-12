#!/usr/bin/env python3
"""
py module
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    accespts k as int or float and returns a tuple
    """
    return (k, v * v)
