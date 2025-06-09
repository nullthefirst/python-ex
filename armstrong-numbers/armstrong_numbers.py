def is_armstrong_number(number):
    num_string = str(number)

    num_list = []

    for digit in num_string:
        num_list.append(digit)

    armstrong_value = 0

    for num in num_list:
        armstrong_value += int(num) ** len(num_list)

    return True if armstrong_value == number else False
