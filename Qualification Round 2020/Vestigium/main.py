import numpy as np

## utils

def int_input():
    return int(input())

## main

def test_case():
    N = int_input()
    M = np.array([list(map(int, input().strip().split())) for _ in range(N)])

    return "{} {} {}".format(
        sum(M[i][i] for i in range(N)),
        sum([len(set(x)) != N for x in M]),
        sum([len(set(x)) != N for x in M.T])
    )


def main():
    for case in range(1, int_input() + 1):
        print(f'Case #{case}: {test_case()}')


if __name__ == '__main__':
    main()