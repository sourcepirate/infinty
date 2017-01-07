from .base import compose, bind, series
import math


@series()
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci._original(n-1) + fibonacci._original(n-2)


def AP(a, d):
    @series(a, d)
    def compute(a, d, n):
        return a + n*d
    return compute()


def GP(a, r):
    @series(a, r)
    def compute(a, r, n):
        return a*(r**n)
    return compute()

@series()
def sum_linear(n):
    if n == 0:
        return 0
    return (n * (n-1))/2

@series()
def sum_square(n):
    if n == 0:
        return 0
    return (n * (n+1) * (2*n+1))/6

@series()
def sum_cube(n):
    if n == 0:
        return 0
    return (n * (n+1))**2/4

@series()
def partions(n):
    if n == 0:
        return 0
    kernal = 1/(4*n*math.sqrt(3))
    degree = math.pi * math.sqrt((2*n)/3)
    return kernal * math.exp(degree)
