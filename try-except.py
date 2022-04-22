#!/bin/env python


print("antes do try")

try:
    print("dentro do try e antes do raise")
    raise Exception("This is an exception")
    print("depois do raise")
except Exception as ex:
    print(f"dentro do extept: {str(ex)}")

print("depois do try")
