#!/usr/bin/env python3
"""py module
"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''creates a task(object) '_asyncio.Task'
    from an couroutine'''
    task = asyncio.ensure_future(wait_random(max_delay))
    return task
