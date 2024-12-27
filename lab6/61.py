import itertools

alp = "НАСТЯ"
ar = itertools.product(alp, repeat=6)
arl = []
for i in ar:
    arl.append(''.join(i))

count = 0
for e in arl:
    if e.count('А') > 1 or e.count('Я') > 1:
        continue
    if e.startswith('А') or e.startswith('Я'):
        continue
    if e.endswith('А') or e.endswith('Я'):
        continue
    flag = True
    for i in range(len(e) - 1):
        if (e[i] == 'А' and e[i + 1] == 'Я') or (e[i + 1] == 'А' and e[i] == 'Я'):
            flag = False
            break
    if flag:
        count += 1

print(count)