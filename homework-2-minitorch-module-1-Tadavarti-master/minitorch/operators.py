"""
Collection of the core mathematical operators used throughout the code base.
"""


import math

# ## Task 0.1

# Implementation of a prelude of elementary functions.


def mul(x, y):
    ":math:`f(x, y) = x * y`"
    # TODO: Implement for Task 0.1.
    return float(x) * float(y)
    raise NotImplementedError('Need to implement for Task 0.1')


def id(x):
    ":math:`f(x) = x`"
    # TODO: Implement for Task 0.1.
    return x
    raise NotImplementedError('Need to implement for Task 0.1')


def add(x, y):
    ":math:`f(x, y) = x + y`"
    # TODO: Implement for Task 0.1.
    return float(x) + float(y)
    raise NotImplementedError('Need to implement for Task 0.1')


def neg(x):
    ":math:`f(x) = -x`"
    # TODO: Implement for Task 0.1.
    return (-1.0 * float(x))
    raise NotImplementedError('Need to implement for Task 0.1')


def lt(x, y):
    ":math:`f(x) =` 1.0 if x is less than y else 0.0"
    # TODO: Implement for Task 0.1.
    return (1 if x < y else 0)
    raise NotImplementedError('Need to implement for Task 0.1')


def eq(x, y):
    ":math:`f(x) =` 1.0 if x is equal to y else 0.0"
    # TODO: Implement for Task 0.1.
    return(1 if x == y else 0)
    raise NotImplementedError('Need to implement for Task 0.1')


def max(x, y):
    ":math:`f(x) =` x if x is greater than y else y"
    # TODO: Implement for Task 0.1.
    return(x if x > y else y)
    raise NotImplementedError('Need to implement for Task 0.1')


def is_close(x, y):
    ":math:`f(x) = |x - y| < 1e-2` "
    # TODO: Implement for Task 0.1.
    return(abs(x - y) < 1e-2)
    raise NotImplementedError('Need to implement for Task 0.1')


def sigmoid(x):
    # TODO: Implement for Task 0.1.
    return((1.0 / (1.0 + exp(-x))) if x > 0 else (exp(x) / (1 + exp(x))))
    raise NotImplementedError('Need to implement for Task 0.1')


def relu(x):
    return(x if x > 0.0 else 0.0)
    raise NotImplementedError('Need to implement for Task 0.1')


EPS = 1e-6


def log(x):
    ":math:`f(x) = log(x)`"
    return math.log(x + EPS)


def exp(x):
    ":math:`f(x) = e^{x}`"
    return math.exp(x)


def log_back(x, d):
    r"If :math:`f = log` as above, compute d :math:`d \times f'(x)`"
    # TODO: Implement for Task 0.1.
    return(d * (1 / x))
    raise NotImplementedError('Need to implement for Task 0.1')


def inv(x):
    ":math:`f(x) = 1/x`"
    # TODO: Implement for Task 0.1.
    return(1.0 / x)
    raise NotImplementedError('Need to implement for Task 0.1')


def inv_back(x, d):
    r"If :math:`f(x) = 1/x` compute d :math:`d \times f'(x)`"
    # TODO: Implement for Task 0.1.
    return(-d * (1 / (x * x)))
    raise NotImplementedError('Need to implement for Task 0.1')


def relu_back(x, d):
    r"If :math:`f = relu` compute d :math:`d \times f'(x)`"
    # TODO: Implement for Task 0.1.
    return(d if x > 0 else 0)
    raise NotImplementedError('Need to implement for Task 0.1')


# ## Task 0.3

# Small library of elementary higher-order functions for practice.

def map(fn , l):
    for i in range(len(l)):
        if(l[i]) < 0:
            l[i] = fn(str(l[i]))
        else:
            l[i] = fn(str(l[i]))
    return l
    raise NotImplementedError('Need to implement for Task 0.3')


def negList(ls):
    ls = list(map(neg , ls))
    return ls
    raise NotImplementedError('Need to implement for Task 0.3')


def zipWith(fn , l1 , l2):
    for i in range(len(l1)):
        l1[i] = fn(str(l1[i]) , str(l2[i]))
    return l1
    raise NotImplementedError('Need to implement for Task 0.3')


def addLists(ls1, ls2):
    "Add the elements of `ls1` and `ls2` using :func:`zipWith` and :func:`add`"
    # TODO: Implement for Task 0.3.
    result = ls1
    result = list(zipWith(add , ls1 , ls2))
    return result
    raise NotImplementedError('Need to implement for Task 0.3')


def reduce(fn, start):
    if(len(start) == 0):
        if(fn == mul):
            return (str(1))
        return (0)
    if(len(start) != 1):
        return (fn(reduce(fn , start[1:]) , str(start[0])))
    else:
        return (fn(reduce(fn , []) , str(start[0])))


def sum(ls):
    "Sum up a list using :func:`reduce` and :func:`add`."
    # TODO: Implement for Task 0.3.
    return reduce(add , ls)
    raise NotImplementedError('Need to implement for Task 0.3')


def prod(ls):
    "Product of a list using :func:`reduce` and :func:`mul`."
    # TODO: Implement for Task 0.3.
    return reduce(mul , ls)
    raise NotImplementedError('Need to implement for Task 0.3')
