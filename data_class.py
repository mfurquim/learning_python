#!/bin/env python
from dataclasses import dataclass


@dataclass(repr=True)
class Options:
    calc_nominal: bool = True
    calc_tan: bool = True

    def set_calc_tan(self, source: str):
        self.calc_tan = source == "use"


def update():
    return {"calc_nominal": False, "calc_tan": True}


if __name__ == "__main__":
    options = Options()
    print(options)

    options.set_calc_tan("dont")
    print(options)

    options = update()
    print(options)
