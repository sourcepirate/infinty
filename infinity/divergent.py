from .base import compose, bind, series
from .util import fact, ncr

def exponential(a):
    @series(a)
    def compute(a, n):
        return a**n/fact(n)
    return compute()


def sine(a):
    @series(a)
    def compute(a, n):
        return (-1 ** n)*(a**(2*n+1))/fact(2*n+1)
    return compute()


def cosine(a):
    @series(a)
    def compute(a, n):
        return (-1 ** n)*(a**(2*n))/fact(2*n)
    return compute()


def harmonics(a):
    @series(a)
    def compute(a, n):
        return (-1**n)/n
    return compute()
