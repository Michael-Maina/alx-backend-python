#!/usr/bin/env python3
"""async comprehensions"""
import asyncio
import random
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    coroutine that returns a list of 10 random numbers from async_generator
    """
    num_list = [i async for i in async_generator()]
    return num_list
