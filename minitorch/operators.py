"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import List, Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.
def mul(x: float, y: float):
    return x * y

def id(x: float):
    return x

def add(x: float, y: float):
    return x + y

def neg(x: float):
    return -x

def lt(x: float, y: float):
    return float(x < y)

def eq(x: float, y: float):
    return float(x == y)

def max(x: float, y: float):
    return x if x > y else y

def is_close(x: float, y: float):
    return float(abs(x - y) < 1e-2)

def sigmoid(x: float):
    if x >= 0:
        return 1 / (1 + math.exp(-x))
    else:
        return math.exp(x) / (1 + math.exp(x))

def relu(x: float):
    return max(x, 0)

def log(x: float):
    return math.log(x)

def exp(x: float):
    return math.exp(x)

def inv(x: float):
    return 1 / x

def log_back(x: float, y: float):
    return y / x

def inv_back(x: float, y: float):
    return -y / (x ** 2)

def relu_back(x: float, y: float):
    return float(x > 0) * y


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


def map(x: List[float], f: Callable[[float], float]):
    return [f(i) for i in x]

def zipWith(x: List[float], y: List[float], f: Callable[[float, float], float]):
    return [f(x[i], y[i]) for i in range(min(len(x), len(y)))]

def reduce(x: List[float], f: Callable[[float, float], float]):
    res = x[0]
    for i in range(1, len(x)):
        res = f(res, x[i])
    return res

def negList(x: List[float]):
    return map(x, neg)

def addLists(x: List[float], y: List[float]):
    return zipWith(x, y, add)

def sum(x: List[float]):
    return reduce(x, add)

def prod(x: List[float]):
    return reduce(x, mul)
