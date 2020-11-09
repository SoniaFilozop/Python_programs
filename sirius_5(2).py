n = int(input())
s = []
x = []
for i in range(n):
    s.append(int(input()))
for i in s:
    m = i
    for j in s:
        if j < m:
            m += j
    x.append(m - i)
answer = []
for i in x:
    if i == max(x):
        answer.append('1')
    else:
        answer.append('0')
print('\n'.join(answer))
