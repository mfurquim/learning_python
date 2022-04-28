#!/bin/env python
import functools
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
        print(f"Executing {func.__name__} function with args: {args}, {kwargs}")
        print(f"function annotations: {func.__annotations__}")
        print(f"function closure: {func.__closure__}")
        print(f"function code: {func.__code__}")
        print(f"function defaults: {func.__defaults__}")
        print(f"function dict: {func.__dict__}")
        print(f"function dir: {func.__dir__()}")
        print(f"function doc: {func.__doc__}")
        print(f"function globals: {func.__globals__}")
        print(f"function hash: {func.__hash__()}")
        print(f"function init: {func.__init__()}")
        print(f"function init_subclass: {func.__init_subclass__()}")
        print(f"function kwdefaults: {func.__kwdefaults__}")
        print(f"function module: {func.__module__}")
        print(f"function name: {func.__name__}")
        print(f"function qualname: {func.__qualname__}")
        print(f"function repr: {func.__repr__()}")
        print(f"function sizeof: {func.__sizeof__()}")
        print(f"function str: {func.__str__()}")
        print(f"function subclasshook: {func.__subclasshook__()}")
        start_time = time.monotonic()

        value = func(*args, **kwargs)

        end_time = time.monotonic()
        elapsed_time = round((end_time - start_time) * 1000, 6)
        print(f"Finished execution of {func.__name__} in {elapsed_time} miliseconds")
        return value

    return inner


@display_info
def printer(person, family, height, age):
    print(f"Hello\n{family}, {person} ({age} y.o, {height} m)")


@display_info
def calculator(a, b, operation=None):
    if not operation:
        raise (EmptyOperation(a, b))

    if operation not in ["addition"]:
        raise (InvalidOperation(a, b, operation=operation))

    if operation == "addition":
        return a + b


def some_(a: str, b: int):
    myframe = inspect.currentframe()
    args, _, _, values = inspect.getargvalues(myframe)
    print([values[arg] for arg in args])
    print(inspect.getargvalues(myframe).locals)
    return a + str(b)


def main():
    printer("Mateus", "Furquim", age=29, height=1.80)
    # some_("1", 2)
    # calculator(2, 4, operation="addition")


import inspect


if __name__ == "__main__":
    main()
