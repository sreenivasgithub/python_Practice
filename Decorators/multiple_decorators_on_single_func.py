def str_upper(func):
    def inner():
        str1 = func()
        return str1.upper()
    return inner
def str_split(func):
    def inner():
        str2 = func()
        return str2.split()
    return inner

@str_split
@str_upper
def upper():
    return 'hi, this is sreenivas'
print(upper())