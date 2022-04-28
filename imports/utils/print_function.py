#!/bin/env python
import functools
import time


def display_info(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(f"{func.__module__} Executing {func.__qualname__} function with args: {args}, {kwargs}")
        start_time = time.monotonic()

        value = func(*args, **kwargs)

        end_time = time.monotonic()
        elapsed_time = round((end_time - start_time) * 1000, 6)
        print(f"{func.__module__} Finished execution of {func.__qualname__} in {elapsed_time} miliseconds")
        return value

    return inner
