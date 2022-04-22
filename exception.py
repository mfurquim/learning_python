#!/bin/env python


def main():
    dictionary = {
        "hello": "world",
    }
    number = 25

    try:
        number = number + dictionary["hello"]
        print(number)
    except TypeError as e:
        raise AttributeError("Dicionário não retornou um número") from e


if __name__ == "__main__":
    main()
