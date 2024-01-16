#!/usr/bin/env python3
"""py module"""
import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''generates an async output each
    second'''
    async_gen = [i async for i in async_generator()]
    return async_gen
