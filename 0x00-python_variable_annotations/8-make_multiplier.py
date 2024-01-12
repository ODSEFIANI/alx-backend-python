#!/usr/bin/env python3
'''py module.
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''multiplier callable.
    '''
    return lambda v: v * multiplier