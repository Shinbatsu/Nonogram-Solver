def dp(n, k, black, ll, gl, groups, whites, blacks,
       blacks_filled, prefix_whites, memo_table):
    if (n, k, black) not in memo_table:
        if n > ll:
            return False
        if n == ll:
            return k == gl

        res = False

        if blacks_filled[n]:
            if dp(n + 1, k, False, ll, gl, groups, whites, blacks,
                  blacks_filled, prefix_whites, memo_table):
                whites[n] = True
                res = True

        if k < gl and not black:
            n_ = n + groups[k]
            if n_ <= ll and prefix_whites[n_] - prefix_whites[n] == 0:
                if dp(n_, k + 1, True, ll, gl, groups, whites, blacks,
                      blacks_filled, prefix_whites, memo_table):
                    for i in range(n, n_):
                        blacks[i] = True
                    res = True

        memo_table[(n, k, black)] = res

    return memo_table[(n, k, black)]
