import numpy as np


def generation(line):
    s = []
    for i in line:
        i = str(i)
        s.append(i)
    m = []
    d = 0
    for i in range(len(s)):
        d += 1
        if d == len(s) - 1:
            m.append(s[d - 1:] + [s[0]])
        elif d == len(s):
            d = 0
            m.insert(0, [s[-1]] + s[d:d + 2])
        else:
            m.append(s[d - 1: d + 2])
    s = []
    for i in m:
        print(i)
        if i == '["1", "1", "1"]':
            s.append('0')
        elif i == '["1", "1", "0"]':
            s.append('0')
        elif i == '["1", "0", "1"]':
            s.append(0)
        elif i == '["1", "0", "0"]':
            s.append(1)
        elif i == '["0", "1", "1"]':
            s.append(1)
        elif i == '["0", "1", "0"]':
            s.append(1)
        elif i == '["0", "0", "1"]':
            s.append(1)
        elif i == '["0", "0", "0"]':
            s.append(0)
    print(m)
    print(s)


print(
    generation("1001000101"))
