from .base import compose, bind, series


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
