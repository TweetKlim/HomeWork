a = [1, 2, 3]
b = len(a) - 1
while b > 0:
    t = a[b]
    a[b] = a[b-1]
    a[b-1] = t
    b -= 1
print(a)