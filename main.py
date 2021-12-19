def main():
    pass


def read_input():
    with open('input.txt') as file:
        lines = file.readlines()
        lines = [int(line.rstrip()) for line in lines]
        return lines


def part_one(input):
    result = [i for i in range(1, len(input)) if input[i] > input[i-1]] 
    return len(result)


def part_two(input):
    total = []

    for i in range(len(input)-2):
        total.append(sum(input[i:i+3]))

    return part_one(total)


if __name__ == '__main__':
    print(part_two(read_input()))
