def outer(expr):
    def upper_d(func):
        def inner():
            return func() + expr
        return inner
    return upper_d


@outer('sreenivas')
def str_decorator():
    return 'this is '
print(str_decorator())