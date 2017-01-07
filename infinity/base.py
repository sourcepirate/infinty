from functools import partial, wraps

try:
    from itertools import imap, count
except ImportError:
    imap = map


def compose(f, g):
    return lambda x: f(g(x))


def bind(f, *args, **kwargs):
    return partial(f, *args, **kwargs)


def amplify(f, g):
    return lambda x: f(x)*g(x)


def damp(f, g):
    return lambda x: f(x)/g(x)


def series(*args):
    def wrapper(func):
        @wraps(func)
        def func_wrapper():
            return imap(lambda x: bind(func, *args)(x), count(0))
        func_wrapper._original = func
        return func_wrapper
    return wrapper
