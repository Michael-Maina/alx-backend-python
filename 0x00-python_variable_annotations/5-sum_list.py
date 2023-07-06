#!/usr/bin/env python3
"""
Type annotated sum_list function module
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns a sum of the float type numbers in the list arg"""
    sum: float = 0
    for num in input_list:
        sum = sum + num
    return sum
