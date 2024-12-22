n = 16**18 + 4**10 - 46 - 16
s = ""  

while n > 0:
    d = n % 4
    s = str(d) + s
    n = n // 4

print(s.count('3'))