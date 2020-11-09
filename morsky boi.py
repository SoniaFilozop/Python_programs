import sys

matrix = []
for i in sys.stdin:
    i = i.rstrip('\n')
    r = []
    for j in i:
        if j != ' ':
            r.append(j)
    matrix.append(r)


def goriz(matrix):
    matrix1 = []
    for i in matrix:
        res = []
        for j in i[::-1]:
            res.append(j)
        matrix1.append(res)
    return matrix1


def vertical(matrix):
    matrix2 = []
    for i in matrix[::-1]:
        matrix2.append(i)
    return matrix2


def transpose(matrix):
    matrix3 = []
    for col in range(len(matrix[0])):
        res = []
        for row in matrix:
            res.append(row[col])
        matrix3.append(res)
    return matrix3


def main():
    for i in matrix:
        print(''.join(i))
    print()
    m1 = goriz(matrix)
    for i in m1:
        print(''.join(i))
    print()
    m2 = vertical(matrix)
    for i in m2:
        print(''.join(i))
    print()
    m3 = transpose(matrix)
    for i in m3:
        print(''.join(i))
    print()
    m4 = vertical(m1)
    for i in m4:
        print(''.join(i))
    print()
    m5 = transpose(m1)
    for i in m5:
        print(''.join(i))
    print()
    m6 = transpose(m2)
    for i in m6:
        print(''.join(i))
    print()
    m7 = transpose(m4)
    for i in m7:
        print(''.join(i))
    print()


main()
