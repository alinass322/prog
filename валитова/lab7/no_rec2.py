def calculate_sequence(n):
    a = [1, 1]
    for i in range(2, n + 1):
        a_i = a[i - 2] + a[i - 1] / (2 ** (i - 1))
        a.append(a_i)
    return a[-1]  

result = calculate_sequence(5)
print(result)