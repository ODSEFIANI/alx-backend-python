#! /usr/bin/env python3
"""py module"""
import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """waits n time and returns a list of waited time(float)"""

    flist = []
    for time in list(range(n)):
        flist.append(await wait_random(max_delay))
    return sorted(flist)
