def f1(x):
    return x**2 + 1


def f2(x):
    return 1 / x**2


def f3(x):
    return x**2 - 1


def f(y):
    if y <= 0:
        return f1(y)
    elif 0 < y < 1:
        return f2(y)
    else:
        return f3(y)
