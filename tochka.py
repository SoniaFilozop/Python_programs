n = int(input())
al = []
left = ['10000000', '0']
right = ['-1000000', '0']
top = ['0', '-100000']
bottom = ['0', '10000']
for i in range(n):
    t = input().split()
    if int(t[1]) >= 0 and int(t[0]) <= 0:
        if int(t[0]) < int(t[1]):
            al.append('(' + t[0] + ', ' + t[1] + ')')
    elif int(t[1]) >= 0 and int(t[0]) >= 0:
        if int(t[0]) > int(t[1]):
            al.append('(' + t[0] + ', ' + t[1] + ')')
    elif int(t[1]) <= 0 and int(t[0]) <= 0:
        if int(t[0]) < int(t[1]):
            al.append('(' + t[0] + ', ' + t[1] + ')')
    elif int(t[1]) <= 0 and int(t[0]) >= 0:
        if int(t[0]) * -1 < int(t[1]):
            al.append('(' + t[0] + ', ' + t[1] + ')')
    if int(t[0]) < int(left[0]):
        left = t
    if int(t[0]) > int(right[0]):
        right = t
    if int(t[1]) < int(bottom[1]):
        bottom = t
    if int(t[1]) > int(top[1]):
        top = t
if al:
    print('\n'.join(al))
print('left:', '(' + left[0] + ', ' + left[1] + ')')
print('right:', '(' + right[0] + ', ' + right[1] + ')')
print('top:', '(' + top[0] + ', ' + top[1] + ')')
print('bottom:', '(' + bottom[0] + ', ' + bottom[1] + ')')
