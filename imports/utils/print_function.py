#!/bin/env python
import functools
import inspect
import os
import time


def display_info(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        inner_frame = inspect.currentframe()
        called_frame = inspect.getouterframes(inner_frame)[1].frame

        try:
            module = inspect.getmodule(called_frame)
            info = inspect.getframeinfo(called_frame)
        finally:
            del inner_frame
            del called_frame

        bind_arguments = inspect.signature(func).bind(*args, **kwargs)
        bind_arguments.apply_defaults()
        arguments = dict(bind_arguments.arguments)

        info_filename = os.path.splitext(os.path.basename(info.filename))[0]

        module_info = [module.__package__, module.__name__]
        frame_info = [info_filename, info.function]
        module_frame_info = module_info + frame_info

        info_path = ".".join([info for info in module_frame_info if info])
        info_path += f":{info.lineno}"

        print(f"{info_path} Executing {func.__qualname__}({arguments})")
        start_time = time.monotonic()

        value = func(*args, **kwargs)

        end_time = time.monotonic()
        elapsed_time = round((end_time - start_time) * 1000, 6)
        print(f"{info_path} Finished {func.__qualname__} in {elapsed_time} miliseconds -> {value}")

        return value

    return inner
