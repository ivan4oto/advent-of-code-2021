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


def vertical_arr(input):
    final_res = []
    for x in range(len(input[0])):
        temp_res = []
        for p in range(len(input)):
            temp_res.append(input[p][x])
        final_res.append(temp_res)
    return final_res


# This is only gonna get uglier from here...
def part_two(input):
    mylist = input[:]
    sublists = vertical_arr(input)
    final_result = {
        'oxygen_gen_rating': 0,
        'co2_scrub_rating': 0
    }

    for s in range(len(vertical_arr(input))):
        sublists = vertical_arr(mylist)

        if sublists[s].count('0') == sublists[s].count('1'):
            mylist = popper(mylist[:], '1', s)
            # print('hi')
        elif sublists[s].count('0') > sublists[s].count('1'):
            mylist = popper(mylist[:], '0', s)
        elif sublists[s].count('1') > sublists[s].count('0'):
            mylist = popper(mylist[:], '1', s)

        if len(mylist) == 1:
            break

    final_result['oxygen_gen_rating'] = int(mylist[0], 2)

    mylist = input[:]

    for s in range(len(vertical_arr(input))):
        sublists = vertical_arr(mylist)

        if sublists[s].count('0') == sublists[s].count('1'):
            mylist = popper(mylist[:], '0', s)
        elif sublists[s].count('1') > sublists[s].count('0'):
            mylist = popper(mylist[:], '0', s)
        elif sublists[s].count('0') > sublists[s].count('1'):
            mylist = popper(mylist[:], '1', s)

        if len(mylist) == 1:
            break

    final_result['co2_scrub_rating'] = int(mylist[0], 2)

    return final_result['co2_scrub_rating']*final_result['oxygen_gen_rating']


def popper(arr, j, indx):
    my_arr = arr[:]
    indexes_to_remove = []
    for k in range(len(arr)):
        if arr[k][indx] == j:
            indexes_to_remove.append(k)    
    my_arr = [arr[a] for a in range(len(arr)) if a not in indexes_to_remove]
    return my_arr


if __name__ == '__main__':
    print(part_two(read_input()))
