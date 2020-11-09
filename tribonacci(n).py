def tribonacci(n):
    if n == 2:
        return 1
    elif n < 2:
        return 0
    else:
        return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)
