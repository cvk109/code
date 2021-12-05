'''
Advent of Code
Day3: Binary Diagnostic
'''
import numpy as np

debug = 0


def subset_selection(input, bit=0, criteria='most_common'):
    '''Keep a subset from the list of binary inputs
       based on criteria for bit of choice.
    '''

    input_binary_numbers = np.array(input, dtype=np.int64)
    input_transposed = input_binary_numbers.T
    bin_counts = np.bincount(input_transposed[bit])
    if len(bin_counts) == 1:
        num_zeros = np.bincount(input_transposed[bit])[0]
        num_ones = 0
    elif len(bin_counts) == 2:
        num_zeros, num_ones = np.bincount(input_transposed[bit])

    if debug:
        print(num_zeros, num_ones, bit)

    if num_zeros == 0 or num_ones == 0:
        return input
    else:
        if num_zeros == num_ones:
            most_common_bit = 1
            least_common_bit = 0
        else:
            most_common_bit = 1 if num_ones > num_zeros else 0
            least_common_bit = 1 if num_ones < num_zeros else 0

        if criteria == 'most_common':
            mask = (input_binary_numbers[:, bit] == most_common_bit)
            output = input_binary_numbers[mask, :]
        elif criteria == 'least_common':
            mask = (input_binary_numbers[:, bit] == least_common_bit)
            output = input_binary_numbers[mask, :]

        return output.tolist()


def get_oxygen_generator_rating(input, bit=0):
    '''Fetch the oxygen generator rating by calling the
       subset selection criteria using most common bit
    '''
    if debug:
        print(bit)
        print(input)
    if len(input) == 1:
        return input
    else:
        output = subset_selection(input, bit=bit, criteria='most_common')
        if debug:
            print(output)
        return get_oxygen_generator_rating(output, bit=bit + 1)


def get_co2_scrubber_rating(input, bit=0):
    '''Fetch the co2 scrubber rating by calling the
       subset selection criteria using least common bit
    '''
    if debug:
        print(bit)
        print(input)
    if len(input) == 1:
        return input
    else:
        output = subset_selection(input, bit=bit, criteria='least_common')
        if debug:
            print(output)
        return get_co2_scrubber_rating(output, bit=bit + 1)


if __name__ == "__main__":
    with open('input3.txt') as file:
        input = file.readlines()
        input = [list(line.strip()) for line in input]

    oxygen_generator_rating_code = get_oxygen_generator_rating(input)[0]
    co2_scrubber_rating_code = get_co2_scrubber_rating(input)[0]
    oxygen_generator_rating = int(
        ''.join([str(i) for i in oxygen_generator_rating_code]), 2)
    co2_scrubber_rating = int(
        ''.join([str(i) for i in co2_scrubber_rating_code]), 2)

    print(
        "o2 genr rating: {}\nco2 genr rating: {}\nlife support rating: {}".format(
            oxygen_generator_rating,
            co2_scrubber_rating,
         (oxygen_generator_rating * co2_scrubber_rating)))

    input = np.array(input, dtype=np.int64)
    input_transposed = input.T
    gamma = [np.argmax(np.bincount(row)) for row in input_transposed]
    epsilon = [np.argmin(np.bincount(row)) for row in input_transposed]
    gamma_string = ''.join([str(x) for x in gamma])
    epsilon_string = ''.join([str(x) for x in epsilon])

    gamma_rate = int(gamma_string, 2)
    epsilon_rate = int(epsilon_string, 2)

    print("Power Consumption : {}".format(gamma_rate * epsilon_rate))
    #print(format(''.join(gamma), 'b'))
