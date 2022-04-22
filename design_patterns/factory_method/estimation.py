#!/bin/env python

from __future__ import annotations
from abc import ABC, abstractmethod

class EstimationCalculator(ABC):
    def __init__(self, company_id):
        self.company_id = company_id

    @abstractmethod
    def estimate(self) -> [dict, dict, dict]:
        pass

class EstimationNormal(EstimationCalculator):
    def estimate(self) -> [dict, dict, dict]:
        print(f"Estimate Normal with {self.company_id}")
        a = {'a': 1}
        b = {'b': 2}
        c = {'c': 3}
        return a, b, c

class EstimationOthers(EstimationCalculator):
    def estimate(self) -> [dict, dict, dict]:
        print(f"Estimate Others with {self.company_id}")
        x = {'x': 9}
        y = {'y': 8}
        z = {'z': 7}
        return x, y, z

def get_estimation(company_id: str) -> None:
    if company_id in [None, 'normal_co']:
        EstimationCalculator = EstimationNormal('normal_co')
    else:
        EstimationCalculator = EstimationOthers(company_id)

    return EstimationCalculator.estimate()


if __name__ == "__main__":
    import sys
    try:
        company_id = str(sys.argv[1]).lower()
    except IndexError:
        company_id = None

    a, b, c = get_estimation(company_id)
    from pprint import pprint
    pprint(a)
    pprint(b)
    pprint(c)

