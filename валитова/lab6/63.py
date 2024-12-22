def get_znam(n):
    znam = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            znam.append(i)
            if i != n // i: 
                znam.append(n // i)
    return znam
count = 0
number = 452022
while count < 5:
    znam = get_znam(number)
    m = sum(znam) if znam else 0
    if m % 7 == 3:
        print(f"Число: {number}, M: {m}")
        count += 1
    number += 1