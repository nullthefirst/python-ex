def is_armstrong_number(number):
    str_digits = "{}".format(number)
    num_digits = len(str_digits)

    value = 0

    for num in str_digits:
        value += int(num) ** num_digits

    return True if value == number else False
