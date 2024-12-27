def unique_values_closure():
    unique_values = set()

    def inner(*args):
        nonlocal unique_values
        unique_values.update(args)
        return list(unique_values)

    return inner
#пример
unique_values = unique_values_closure()
print(unique_values(1, 2, 3, 2, 4, 5, 3, 6))
print(unique_values(5, 6, 7, 8, 1, 2, 3, 4))