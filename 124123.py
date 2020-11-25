def tic_tac_toe(field):
    if (['x', 'x', 'x'] in field) or (
            field[0][0] == 'x' and field[1][0] == 'x' and field[2][0] == 'x') or (
            field[0][2] == 'x' and field[1][2] == 'x' and field[2][2] == 'x'):
        print('x win')
    elif (['0', '0', '0'] in field) or (
            field[0][0] == '0' and field[1][0] == '0' and field[2][0] == '0') or (
            field[0][2] == '0' and field[1][2] == '0' and field[2][2] == '0'):
        print('0 win')
    elif (field[1][1]) == 'x' and (((field[0][0] == 'x') and (
            field[2][2] == 'x')) or ((field[0][2] == 'x') and (
            field[2][0] == 'x')) or ((field[0][1] == 'x') and (
            field[2][1] == 'x'))):
        print('x win')
    elif (field[1][1]) == '0' and (((field[0][0] == '0') and (
            field[2][2] == '0')) or ((field[0][2] == '0') and (
            field[2][0] == '0')) or ((field[0][1] == '0') and (
            field[2][1] == '0'))):
        print('0 win')
    else:
        print('draw')
print()
