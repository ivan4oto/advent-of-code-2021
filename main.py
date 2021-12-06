def main():
    with open('input.txt') as file:
        lines = file.readlines()
        lines = [int(line.rstrip()) for line in lines]
    result = [i for i in range(1, len(lines)) if lines[i] > lines[i-1]] 

    return len(result)


if __name__ == '__main__':
    print(main())
