#!/bin/env python
from pprint import pprint


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        print(f"\nSingleton.__call__({cls}, {args}, {kwargs})")

        if cls not in cls._instances:
            print(f"{cls} not in cls._instances")
            cls._instances[cls] = super().__call__(*args, **kwargs)

        print(f"returning {cls._instances[cls]} of class {cls}")
        return cls._instances[cls]


class UniqueInstance(metaclass=Singleton):
    """This is an example of Singleton Class

    Args:
        name(str): Name of the person."""

    _type = "pessoa"

    def __init__(self, name=None):
        print(f"UniqueInstance(name={name})")

        self._name = name
        print(f"self._name= {self._name}")


if __name__ == "__main__":
    print("This is an example of the implementation of the Design Pattern Singleton")

    first_inst = UniqueInstance("Larissa")
    second_inst = UniqueInstance("Mateus")

    print("\nFirst Inst (Larissa)")
    print(first_inst.__dict__)

    print("\nSecond Inst (Mateus)")
    print(second_inst.__dict__)

    print("\nUniqueInstance Class")
    pprint(UniqueInstance.__dict__)

    print("\nSingleton Class")
    pprint(Singleton.__dict__)
