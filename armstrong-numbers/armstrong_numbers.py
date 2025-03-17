def is_armstrong_number(number):
    num_string = "{}".format(number)

    checker = 0

    for char in num_string:
        checker += int(char) ** len(num_string)

    return True if checker == int(number) else False

