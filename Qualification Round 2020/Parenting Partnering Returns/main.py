## utils
def int_input():
    return int(input())


def int_list_input():
    return list(map(int, input().strip().split()))


## MAIN

def test_case():
    N = int_input()
    l = [(i, int_list_input()) for i in range(N)]
    debug(l)
    Cs = []
    Js = []

    C, J = 0, 0
    l = sorted(l, key=lambda t: t[1][0])
    for i, task in l:
        t1, t2 = task
        if C <= t1:
            Cs.append(i)
            C = t2
        elif J <= t1:
            Js.append(i)
            J = t2
        else:
            return 'IMPOSSIBLE'

    return ''.join(['C' if idx in Cs else 'J' for idx in range(N)])


## main

def main(input_fnc=input, print_fnc=print, debug_fnc=lambda x: None):
    global input, print, debug
    input, print, debug = input_fnc, print_fnc, debug_fnc
    for case in range(1, int_input() + 1):
        print(f'Case #{case}: {test_case()}')


if __name__ == '__main__':
    main()
