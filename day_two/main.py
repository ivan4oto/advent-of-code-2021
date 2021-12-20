def main():
    pass


def read_input():
    with open('input.txt') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        return lines


def part_one(input):
    x = 0
    y = 0
    course = [i.split(' ') for i in read_input()]
    for i in course:
        if i[0] == 'up':
            y += int(i[1])

        if i[0] == 'down':
            y -= int(i[1])

        if i[0] == 'forward':
            x += int(i[1])

    depth = y*-1
    horizontal_position = x

    return depth*horizontal_position


def part_two(input):
    x = 0
    y = 0
    aim = 0
    course = [i.split(' ') for i in read_input()]
    for i in course:
        if i[0] == 'up':
            aim -= int(i[1])

        if i[0] == 'down':
            aim += int(i[1])

        if i[0] == 'forward':
            x += int(i[1])
            y -= aim*int(i[1])

    depth = y*-1
    horizontal_position = x

    return depth*horizontal_position


if __name__ == '__main__':
    print(part_two(read_input()))
