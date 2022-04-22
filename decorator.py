#!/bin/env python

import time
import functools

class CalculatorException(Exception):
    """ Exception raised for calculator

    Attr:
        a (Union[int, float]): Numerator of the operation - e.g., 2
        b (Union[int, float]): Denominator of the operation - e.g., 3.3
        op (str): Operation to execute on calculator - e.g., 'addition'
        message (str): Explanation of the error - e.g., 'Missing calculator operation'
    """

    def __init__(self, a, b, operation, message='Missing calculator operation'):
        self.a = a
        self.b = b
        self.operation = operation
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}. Operation {self.operation} with {self.a} and {self.b}"


class EmptyOperation(CalculatorException):
    """ Exception raised for missing operation on calculator

    Attr:
        a (Union[int, float]): Numerator of the operation - e.g., 2
        b (Union[int, float]): Denominator of the operation - e.g., 3.3
        op (str): Operation to execute on calculator - e.g., 'addition'
        message (str): Explanation of the error - e.g., 'Missing calculator operation'
    """

    def __init__(self, a, b, operation=None, message='Missing calculator operation'):
        self.a = a
        self.b = b
        self.operation = operation
        self.message = message
        super().__init__(self.message)


class InvalidOperation(CalculatorException):
    """ Exception raised for invalid or not yet implemented operation on calculator

    Attr:
        a (Union[int, float]): Numerator of the operation - e.g., 2
        b (Union[int, float]): Denominator of the operation - e.g., 3.3
        op (str): Operation to execute on calculator - e.g., 'addition'
        message (str): Explanation of the error - e.g., 'Invalid or not yet implemented operation'
    """

    def __init__(self, a, b, operation, message='Invalid or not yet implemented operation'):
        self.a = a
        self.b = b
        self.operation = operation
        self.message = message
        super().__init__(self.message)

def display_info(func):

    @functools.wraps(func)
    def inner(*args, **kwargs):
        print("Executing", func.__name__, "function with args:", args, kwargs)
        start_time = time.monotonic()

        value = func(*args, **kwargs)

        end_time = time.monotonic()
        elapsed_time = round((end_time - start_time)*1000, 6)
        print("Finished execution in", elapsed_time, "miliseconds")
        return value

    return inner

@display_info
def printer(person, family, height, age):
    print(f"Hello\n{family}, {person} ({age} y.o, {height} m)")

@display_info
def calculator(a, b, operation=None):
    if not operation:
        raise(EmptyOperation(a,b))

    if operation not in ['addition']:
        raise(InvalidOperation(a,b,operation=operation))

    if operation == 'addition':
        return a+b

def main():
    printer('Mateus', 'Furquim', age=29, height=1.80)
    calculator(2, 4, operation='ddition')

if __name__ == '__main__':
    main()
