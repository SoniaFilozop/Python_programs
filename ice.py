n = int(input())
sorte = {}
zakaz = {}
nom = 1
m = 0
for i in range(n):
    name = input()
    if '\t' in name:
        name.replace('\t', ' ')
    name = name.split()
    x = name[-1].lstrip(' ')
    del name[-1]
    sorte[' '.join(name)] = x
line = input()
while line != '.':
    if line != '------------------------':
        if '\t' in line:
            line = line.replace('\t', ' ')
        if not line:
            m += 1
        elif line and m > 0:
            m = 0
            nom += 1
            line = line.split()
            k = int(line[-1])
            del line[-1]
            line = ' '.join(line)
            line = line.rstrip(' ').rstrip('\t')
            if str(nom) + ')' not in zakaz:
                zakaz[str(nom) + ')'] = k * int(sorte[line])
            else:
                zakaz[str(nom) + ')'] += k * int(sorte[line])
        elif line and m == 0:
            line = line.split()
            k = int(line[-1])
            del line[-1]
            line = ' '.join(line)
            line = line.rstrip(' ').rstrip('\t')
            if str(nom) + ')' not in zakaz:
                zakaz[str(nom) + ')'] = k * int(sorte[line])
            else:
                zakaz[str(nom) + ')'] += k * int(sorte[line])
    line = input()
itog = 0
for i in zakaz:
    print(i, zakaz[i])
    itog += zakaz[i]
print('Итого:', itog)