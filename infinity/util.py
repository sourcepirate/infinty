def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n-1)


def ncr(n, r):
    return fact(n)/ (fact(n-r)* fact(r))
