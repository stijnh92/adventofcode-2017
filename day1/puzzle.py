def solve_puzzle():
    total1, total2 = 0, 0

    with open('puzzle_input', 'r') as input_file:
        content = input_file.read()
        value = content.strip()
    length = len(value)

    for index, digit in enumerate(value):
        index1 = (index + 1) % length
        index2 = (index + (length / 2)) % length

        if (digit == value[index1]):
            total1 += int(digit)
        if (digit == value[index2]):
            total2 += int(digit)

    print('Result of puzzle 1: %s' % total1)
    print('Result of puzzle 2: %s' % total2)


if __name__ == '__main__':
    solve_puzzle()
