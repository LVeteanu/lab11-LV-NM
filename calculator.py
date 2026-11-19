# https://github.com/LVeteanu/lab11-LV-NM.git
# Partner 1: Luca Veteanu
# Partner 2: Natalie Moore

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)


# First example
def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def mul(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise ZeroDivisionError

def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise ZeroDivisionError

def logarithm(a, b):
    try:
        return a * math.log(b)
    except ValueError:
        raise ValueError

def exponent(a):
    return a ** b

def exp(a):
    return a ** b


