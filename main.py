from typing import List

cache = {}


def p():
    pass


def q(a: List[List], c: List[List], n: int):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif f'{a, c, n}' in cache:
        return cache[f'{a, c, n}']
    else:
        value = (sum(
            a[0][i] * c[0][i] * delta(n - c[0][i], 0, len(a[0])) * q(a, c, n - c[0][i]) for i in range(0, len(a[0]))) +
                 sum(a[1][i] * c[1][i] * delta(n - c[1][i], 1, len(a[1])) * q(a, c, n - c[1][i]) for i in
                     range(0, len(a[1])))) / n
        cache[f'{a, c, n}'] = value
        return value


def delta(i, j, qi):
    if j == 0:
        if i > qi:
            return 0
        else:
            return 1
    elif j == 1:
        if i > qi:
            return 1
        else:
            return 0
    else:
        raise Exception('second value is neither 0 or 1')
    pass


def main():
    pass


if __name__ == '__main__':
    a = [[15, 1, 4, 2], [15, 1, 4, 2]]
    c = [[1, 6, 10, 20], [1, 3, 10, 15]]
    m = 4

    for i in range(0, m + 1):
        print(f'q({i}) = {q(a, c, i)}')

