#!/usr/bin/env python3
"""py module"""

import random
import asyncio
from typing import Union


async def wait_random(max_delay: Union[float, int] = 10):

    """waits befores ruturning random valuue"""
    await asyncio.sleep(max_delay)
    return random.randint(0, max_delay)
