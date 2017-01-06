from .base import compose, bind, series


def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n-1)


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
    @series
    def compute(a, n):
        return (-1 ** n)*(a**(2*n))/fact(2*n)
    return compute()
