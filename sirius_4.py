import math

n = int(input())
k = math.sqrt(n)
y = 0
x = 0
if k % 1 != 0:
    k = int(k // 1 + 1)
    if n == k ** 2 - k + 1:
        print(k, k)
    elif n > k ** 2 - k + 1:
        y = k
        x = k
        m = k ** 2 - k + 1
        while n != m:
            m += 1
            x -= 1
        if k ** 2 % 2 == 0:
            print(y, x)
        else:
            print(x, y)
    elif n < k ** 2 - k + 1:
        y = k
        x = k
        m = k ** 2 - k + 1
        while n != m:
            m -= 1
            y -= 1
        if k ** 2 % 2 == 0:
            print(y, x)
        else:
            print(x, y)
elif k % 2 == 0:
    x = 1
    y = int(k)
    print(x, y)
else:
    y = 1
    x = int(k)
    print(x, y)
