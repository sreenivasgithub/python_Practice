def max(items, key=lambda x: x):
    current = items[0]
    for item in items:
        if key(item) > key(current):
            current = item
    return current
print(max([1,3,4,5,6]))