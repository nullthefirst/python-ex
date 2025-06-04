def grains():
    output = [1]

    for index in range(1, 65):
        output.append(output[index - 1] * 2)

    return output


def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")

    return grains()[number - 1]


def total():
    pass
