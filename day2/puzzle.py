def solve_puzzle_1():
    total = 0
    for line in get_lines():
        total += max(line) - min(line)

    print('Result of puzzle 1: %s' % total)


def solve_puzzle_2():
    total = 0
    for line in get_lines():
        for number1 in line:
            for number2 in line:
                if(number1 != number2 and not (number1 % number2)):
                    total += (number1 / number2)

    print('Result of puzzle 2: %s' % total)


def get_lines():
    lines = []
    with open('puzzle_input', 'r') as input_file:
        content = input_file.readlines()
        for line in content:
            lines.append([int(x) for x in line.split()])

    return lines


if __name__ == '__main__':
    solve_puzzle_1()
    solve_puzzle_2()
