def div_decorator(func):
    def inner(a,b):
        if b == 0:
            return 'give proper input'
        else:
            return func(a,b)
    return inner

@div_decorator
def div(a,b):
    return a/b
print(div(2,1))