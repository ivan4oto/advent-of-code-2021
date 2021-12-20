def main():
    pass


def read_input():
    with open('input.txt') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        return lines


def part_one(input):
    dict_of_numbers = dict()
    for i in range(len(input[0])):
        dict_of_numbers[i] = []
    for seq in input:
        for s in range(len(seq)):
            dict_of_numbers[s].append(seq[s])
    gamma_rate_binary = []
    epsilon_rate_binary = []

    for value in dict_of_numbers.values():
        ones = value.count('1')
        zeroes = value.count('0')
        if ones > zeroes:
            gamma_rate_binary.append('1')
            epsilon_rate_binary.append('0')
        elif zeroes > ones:
            gamma_rate_binary.append('0')
            epsilon_rate_binary.append('1')

    gamma_rate_binary = ''.join(gamma_rate_binary)
    epsilon_rate_binary = ''.join(epsilon_rate_binary)

    return int(gamma_rate_binary, 2)*int(epsilon_rate_binary, 2)


if __name__ == '__main__':
    print(part_one(read_input()))
