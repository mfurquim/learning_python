#!/bin/env python

from dataclasses import dataclass


@dataclass(repr=True)
class Options:
    calc_nominal: bool = True
    calc_tan: bool = True


if __name__ == '__main__':
    options = Options()
