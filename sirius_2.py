a = int(input())
b = int(input())
m = 0
n = 0
while (b > 0) and (a > 0):
    if (a + b) % 3 != 0:
        break
    elif (a >= b) and (a - 2 >= 0) and (b - 1 >= 0):
        m += 1
        b -= 1
        a -= 2
    elif (b > a) and (a - 1 >= 0) and (b - 2 >= 0):
        n += 1
        b -= 2
        a -= 1
if a == 0 and b == 0:
    print(m, n)
else:
    print(-1)
