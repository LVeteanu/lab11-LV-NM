# https://github.com/LVeteanu/lab11-LV-NM.git
# Partner 1: Luca Veteanu
# Partner 2: Natalie Moore

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math


# First example
def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise ZeroDivisionError

def logarith(a, b):
    try:
        return a * math.log(b)
    except ValueError:
        raise ValueError

def exponent(a):
    return a ** 2


