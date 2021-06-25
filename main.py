from typing import List

cache = {}


def q(a: List[List], c: List[List], Q: List, n: int, m: int) -> float:  # no normalisation included
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif f'{a, c, Q, n, m}' in cache:  # lets speedup a bit
        return cache[f'{a, c, Q, n, m}']
    else:
        value = (sum(
            a[0][i] * c[0][i] * sigma(n - c[0][i], 0, Q[i]) * q(a, c, Q, n - c[0][i], m) for i in range(0, m)) +
                 sum(
            a[1][i] * c[1][i] * sigma(n - c[1][i], 1, Q[i]) * q(a, c, Q, n - c[1][i], m) for i in range(0, m))
                 ) / n
        cache[f'{a, c, Q,n, m}'] = value
    return value


def p(a: List[List], c: List[List], Q: List, n: int, m: int) -> float:  # normalisation included
    return q(a, c, Q, n, m) / sum(q(a, c, Q, i, m) for i in range(0, n + 1))


def e(a: List[List], c: List[List], Q: List, n: int, m: int, i: int) -> float:
    return sum(p(a, c, Q, j, m) for j in range(n - c[1][i] + 1, n + 1))


def sigma(n, j, qi) -> int:
    if j == 0:
        if n > qi:
            return 0
        else:
            return 1
    elif j == 1:
        if n > qi:
            return 1
        else:
            return 0
    else:
        raise Exception('second value is neither 0 or 1')


if __name__ == '__main__':
    # a = [[15, 1, 4, 2], [15, 1, 4, 2]]
    # c = [[1, 6, 10, 20], [1, 3, 10, 15]]
    # a = [[15, 4.28571429, 2.72727272], [15, 4.28571429, 2.72727272]]
    # c = [[2, 7, 11], [2, 7, 11]]
    # a = [[160, 32, 20, 10.66666666666667, 6.4], [160, 32, 20, 10.66666666666667, 6.4]]
    # c = [[1, 5, 8, 15, 25], [1, 5, 8, 15, 25]]
    a = [[15, 1, 4, 2], [15, 1, 4, 2]]
    c = [[1, 6, 10, 20], [1, 3, 10, 15]]

    Q = [1, 0, 3, 4]  # doesnt change anything ://
    m = 4
    v = 180

    print(f'm: {m}, v: {v}, a: {a}, c: {c}, Q: {Q}')

    for i in range(0, v + 1):
        print(f'q({i}) = {q(a, c, Q, i, m)}, p({i}) = {p(a, c, Q, i, m)}')

    for j in range(0, m):
        print(f'E{j + 1} = {e(a, c, Q, v, m, j)}')

    print('\n')
