import functools

import sys


trace_enabled = False
def tracee(func = None, *, handle = sys.stdout):
    # со скобочками
    if func is None:
        return lambda func: trace(func, handle=handle)

    #без скобок
    @functools.wraps(func)
    def inner(*args,**kwargs):
        print(func.__name__, args, kwargs)
        return func(*args,**kwargs)
    return inner

@tracee
def indetify(x):
    """
    I do nothing useful.
    :param x:
    :return x:
    """
    return x

print(indetify(3))
# запуск программы один раз


def trace(func = None, *, handle=sys.stdout):
    if func is None:
        return lambda func: trace(func, handle=handle)

    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs)
        return func(*args, *kwargs)
    return inner


@trace
def foo(x):
    return x

print(foo(2))