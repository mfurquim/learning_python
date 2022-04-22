#!/bin/env python
from datetime import date
from datetime import timedelta


class Person:
    def __init__(self, name="Nome"):
        self._name = name

    def pega_nome(self, timestamp: date = date.today()):
        print(timestamp)

    def pega_pega(self):
        self.pega_nome()


if __name__ == "__main__":
    pessoa = Person("Um Nome")
    print(pessoa)
    print(pessoa._name)
    pessoa.pega_pega()
