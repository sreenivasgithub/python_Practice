def addition(a, b):
    if isinstance(a, int) and isinstance(b, int):
        if a > 0 and b> 0:
            return (a + b)
        return "nonnn"
    return "enter integer"


addition(10,20)