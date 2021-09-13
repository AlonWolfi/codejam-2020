## utils
def int_input():
    return int(input())


def int_list_input():
    return list(map(int, input()))



## MAIN

def test_case():
    dig_list = int_list_input()
    final_str = ''
    last_dig = 0
    for dig in dig_list:
        val = dig - last_dig
        if val > 0:
            final_str += '(' * val + str(dig)
        elif val < 0:
            final_str += ')' * abs(val) + str(dig)
        else:
            final_str += str(dig)
        last_dig = dig
    final_str += ')' * last_dig
    return final_str

## main

def main(input_fnc=input, print_fnc=print):
    global input, print
    input, print = input_fnc, print_fnc
    for case in range(1, int_input() + 1):
        print(f'Case #{case}: {test_case()}')


if __name__ == '__main__':
    main()
