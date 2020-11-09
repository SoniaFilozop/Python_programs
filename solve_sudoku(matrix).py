def solve_sudoku(matrix):
    import sys
    matrix = []
    for i in sys.stdin:
        matrix.append([i.rstrip('\n')])
    if not matrix:
        return matrix
    else:
         
