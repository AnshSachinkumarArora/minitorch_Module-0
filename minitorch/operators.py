"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

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
def mul(a: float, b: float) -> float:
    return a * b

def id(a: float) -> float:
    return a

def add(a: float, b: float) -> float:
    return a + b

def neg(a: float) -> float:
    return -a

def lt(a: float, b: float) -> float:
    return 1.0 if (a < b) else 0.0

def eq(a: float, b: float) -> float:
    return 1.0 if (a == b) else 0.0

def max(a: float, b: float) -> float:
    return a if (a > b) else b

def is_close(a: float, b: float) -> float:
    return 1.0 if (abs(a - b) < 1e-5) else 0.0

def sigmoid(x: float) -> float:
    return (1.0/(1.0+math.exp(-x))) if (x >= 0) else (math.exp(x)/(1.0+math.exp(x)))

def relu(x: float) -> float:
    return max(0.0, x)

def log(x: float) -> float:
    "$f(x) = log(x)$"
    return math.log(x)

def exp(x: float) -> float:
    "$f(x) = e^{x}$"
    return math.exp(x)

def inv(x: float) -> float:
    return 1/x

def log_back(x: float, d: float) -> float:
    return (1/x)*d 

def inv_back(x: float, d: float) -> float:
    return (-1/pow(x, 2))*d

def relu_back(x: float, d: float) -> float:
    return d if (x > 0) else 0

# TODO: Implement for Task 0.1.


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


# TODO: Implement for Task 0.3.

def map(fn: Callable[[float], float]) -> Callable[[Iterable[float]], Iterable[float]]:
    """
    Higher-order map.

    See https://en.wikipedia.org/wiki/Map_(higher-order_function)

    Args:
        fn: Function from one value to one value.

    Returns:
         A function that takes a list, applies `fn` to each element, and returns a
         new list
    """
    # TODO: Implement for Task 0.3.
    def apply(list: Iterable[float]):
        res = []
        for x in list:
            res.append(fn(x))
        return res
    return apply


def negList(ls: Iterable[float]) -> Iterable[float]:
    "Use `map` and `neg` to negate each element in `ls`"
    # TODO: Implement for Task 0.3.
    negate = map(neg)
    negated = negate(ls)
    return negated
    raise NotImplementedError('Need to implement for Task 0.3')

def zipWith(
    fn: Callable[[float, float], float]
) -> Callable[[Iterable[float], Iterable[float]], Iterable[float]]:
    """
    Higher-order zipwith (or map2).

    See https://en.wikipedia.org/wiki/Map_(higher-order_function)

    Args:
        fn: combine two values

    Returns:
         Function that takes two equally sized lists `ls1` and `ls2`, produce a new list by
         applying fn(x, y) on each pair of elements.

    """
    # TODO: Implement for Task 0.3.
    def apply(l1: Iterable[float], l2: Iterable[float]):
        res = []
        for x, y in zip(l1, l2):
            res.append(fn(x, y))
        return res
    return apply
    raise NotImplementedError('Need to implement for Task 0.3')


def addLists(ls1: Iterable[float], ls2: Iterable[float]) -> Iterable[float]:
    "Add the elements of `ls1` and `ls2` using `zipWith` and `add`"
    # TODO: Implement for Task 0.3.
    zip = zipWith(add)
    zipped = zip(ls1, ls2)
    return zipped
    raise NotImplementedError('Need to implement for Task 0.3')

def reduce(
    fn: Callable[[float, float], float], start: float
) -> Callable[[Iterable[float]], float]:
    r"""
    Higher-order reduce.

    Args:
        fn: combine two values
        start: start value $x_0$

    Returns:
         Function that takes a list `ls` of elements
         $x_1 \ldots x_n$ and computes the reduction :math:`fn(x_3, fn(x_2,
         fn(x_1, x_0)))`
    """
    # TODO: Implement for Task 0.3.
    def apply(list: Iterable[float]):
        res = start
        for x in list:
            res = fn(x, res)
        return res
    return apply
    raise NotImplementedError('Need to implement for Task 0.3')


def sum(ls: Iterable[float]) -> float:
    "Sum up a list using `reduce` and `add`."
    # TODO: Implement for Task 0.3.
    sum_list = reduce(add, 0.0)
    sum_final = sum_list(ls)
    return sum_final
    raise NotImplementedError('Need to implement for Task 0.3')


def prod(ls: Iterable[float]) -> float:
    "Product of a list using `reduce` and `mul`."
    # TODO: Implement for Task 0.3.
    mult = reduce(mul, 1.0)
    return mult(ls)
    raise NotImplementedError('Need to implement for Task 0.3')