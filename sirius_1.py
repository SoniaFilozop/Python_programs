k = int(input())
n = int(input())
m = n % k
if m <= k / 2:
    print(m)
else:
    print(k - m)
