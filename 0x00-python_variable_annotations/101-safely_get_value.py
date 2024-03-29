#!/usr/bin/env python3
'''Task 11's module.
'''
from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, T], key: Any, default: Union[T, None] = None) -> Union[T, Any]:
    """safety"""

    if key in dct:
        return dct[key]
    else:
        return default
