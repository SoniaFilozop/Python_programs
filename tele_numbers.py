m = input()


def number(a):
    a = a.strip(' ')
    if a[0:2] != '+7' and a[0] != '8':
        return 'error'
    if a.count('(') != 0 or a.count(')') != 0:
        if a.count('(') != a.count(')'):
            return 'error'
        n = 0
        b = 0
        for i in a:
            if i == '(':
                n += 1
            elif i == ')':
                b += 1
            if b > 1 or n > 1:
                return 'error'
    if a[0] == '-' or a[-1] == '-':
        return 'error'
    if a.count('-') != 0:
        n = 1
        for i in a[2:]:
            n += 1
            if i == '-' and a[n - 1] == '-':
                return 'error'
    if a.startswith('8'):
        a = '+7' + a[1:]
    a = a.replace('\t', '').replace(' ', '').replace('-', '').replace('(', '').replace(')', '')
    if not a[1:].isdigit():
        return 'error'
    if len(a) != 12:
        return 'error'
    return a


print(number(m))
