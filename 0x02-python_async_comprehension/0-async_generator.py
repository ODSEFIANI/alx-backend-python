#!/usr/bin/env python3
"""py module"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    '''generates an async output each
    second'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
