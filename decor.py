import functools

import sys


trace_enabled = False
def trace(func = None, *, handle = sys.stdout):
    # со скобочками
    if func is None:
        return lambda func: trace(func, handle=handle)

    #без скобок
    @functools.wraps(func)
    def inner(*args,**kwargs):
        print(func.__name__, args, kwargs)
        return func(*args,**kwargs)
    return inner

@trace
def indetify(x):
    """
    I do nothing useful.
    :param x:
    :return x:
    """
    return x

indetify(2)
# запуск программы один раз
def once(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        if not inner.called:
            func(*args, **kwargs)
            inner.called = True
        inner.called = False
        return inner


@once
def iin():
    print("initialisation complete")


iin()
