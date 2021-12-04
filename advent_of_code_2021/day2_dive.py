'''
Advent of Code
Day 2 - Dive!
'''

debug = 1


def get_final_position(input):
    '''
    Given a series of up, down and forward instructions,
    this function generates the final position.
    '''
    horizontal_position = 0
    depth_position = 0
    aim = 0

    for i in range(len(input)):
        if debug:
            input[i]
        motion, distance = input[i].split(' ')
        distance = int(distance)
        if motion == 'forward':
            horizontal_position += distance
            depth_position = depth_position + (aim * distance)
        elif motion == 'up':
            aim -= distance
        elif motion == 'down':
            aim += distance

    return((horizontal_position, depth_position, aim))


if __name__ == '__main__':
    with open('input2.txt') as file:
        input = file.readlines()
        input = [line.strip() for line in input]
    final_position = get_final_position(input)
    print(
        "Final Position: {}.\nProduct: {}.".format(
            final_position,
            final_position[0] *
            final_position[1]))
