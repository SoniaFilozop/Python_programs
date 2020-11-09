n = int(input())
mail = []
fine = []
for i in range(n):
    a = input()
    b = a.find('@')
    mail.append(a[:b])
n1 = int(input())
for i in range(n1):
    name = input()
    m = 0
    for j in mail:
        if name in j:
            m += 1
    if m > 0:
        fine.append(name + str(m) + '@untitled.py')
        mail.append(name + str(m))
    else:
        fine.append(name + '@untitled.py')
        mail.append(name)
print('\n'.join(fine))
