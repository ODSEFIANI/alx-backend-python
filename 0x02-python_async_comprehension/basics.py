#! /usr/bin/env python3
"""py module"""
import asyncio
import random
from typing import List

async def async_generator():
    for i in range(5):
        await asyncio.sleep(1)  # Simulating asynchronous operation
        yield i
    async for value in async_generator():
        print(value)



asyncio.run(async_generator())