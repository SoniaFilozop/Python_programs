def rec_linear_sum(some_list):
    d = 0
    n = 0
    if not some_list:
        return 0
    else:
        n += 1
        d += some_list[0]
        return d + rec_linear_sum(some_list[n:])
