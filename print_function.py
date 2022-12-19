#!/bin/env python
import functools
import inspect
import os
import time


class CalculatorException(Exception):
    """Exception raised for calculator

    Attr:
        a (Union[int, float]): Numerator of the operation - e.g., 2
        b (Union[int, float]): Denominator of the operation - e.g., 3.3
        op (str): Operation to execute on calculator - e.g., 'addition'
        message (str): Explanation of the error - e.g., 'Missing calculator operation'
    """

    def __init__(self, a, b, operation, message="Missing calculator operation"):
        self.a = a
        self.b = b
        self.operation = operation
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}. Operation {self.operation} with {self.a} and {self.b}"


class EmptyOperation(CalculatorException):
    """Exception raised for missing operation on calculator

    Attr:
        a (Union[int, float]): Numerator of the operation - e.g., 2
        b (Union[int, float]): Denominator of the operation - e.g., 3.3
        op (str): Operation to execute on calculator - e.g., 'addition'
        message (str): Explanation of the error - e.g., 'Missing calculator operation'
    """

    def __init__(self, a, b, operation=None, message="Missing calculator operation"):
        self.a = a
        self.b = b
        self.operation = operation
        self.message = message
        super().__init__(self.message)


class InvalidOperation(CalculatorException):
    """Exception raised for invalid or not yet implemented operation on calculator

    Attr:
        a (Union[int, float]): Numerator of the operation - e.g., 2
        b (Union[int, float]): Denominator of the operation - e.g., 3.3
        op (str): Operation to execute on calculator - e.g., 'addition'
        message (str): Explanation of the error - e.g., 'Invalid or not yet implemented operation'
    """

    def __init__(self, a, b, operation, message="Invalid or not yet implemented operation"):
        self.a = a
        self.b = b
        self.operation = operation
        self.message = message
        super().__init__(self.message)


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
        log.debug(f"{info_path} Finished execution of {func.__name__} in {elapsed_time} miliseconds -> {value}")

        return value

    return inner


@display_info
def printer(person, family, height, age=20):
    print(f"Hello\n{family}, {person} ({age} y.o, {height} m)")


def display_info_with_parameter(dec_arg):
    def display_info(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            log.debug(f"{dec_arg} Executing {func.__name__} function with args: {args}, {kwargs}")
            start_time = time.monotonic()

            value = func(*args, **kwargs)

            end_time = time.monotonic()
            elapsed_time = round((end_time - start_time) * 1000, 6)
            log.debug(f"Finished execution of {func.__name__} in {elapsed_time} miliseconds")

            return value

        return inner

    return display_info


# @display_info_with_parameter("Dec Arg")
@display_info
def printer(person, family, height, age):
    print(f"Hello\n{family}, {person} ({age} y.o, {height} m)")


def some_(a: str, b: int):
    frame = inspect.currentframe()

    try:
        print(frame)

        src_line = inspect.getsourcelines(frame)
        line_no = src_line[1]
        print(line_no)

        src_file = inspect.getsourcefile(frame)
        print(src_file)

        file = inspect.getfile(frame)
        print(file)

        module = inspect.getmodule(frame)
        print(module)

        info = inspect.getframeinfo(frame)
        print(info)
        print(info.filename)
        print(info.lineno)
        print(info.function)

        members = inspect.getmembers(module)
        print("\nmembers:")
        for k, v in members:
            print(f"{k} -> {v}")

    finally:
        del frame

    return a + str(b)


def main():
    printer("Mateus", "Furquim", height=1.80)
    # printer("João", "Euko", age=30, height=1.62)
    # print(some_("1", 2))
    # calculator(2, 4, operation="addition")


if __name__ == "__main__":
    main()
