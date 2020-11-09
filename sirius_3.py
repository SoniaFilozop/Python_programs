n = int(input())
v = {}
d = 0
for i in range(n):
    d += 1
    m = int(input())
    v[m] = (n - d + 1)
list_keys = list(v.keys())
list_keys.sort()
for i in list_keys:
    print(v[i])
