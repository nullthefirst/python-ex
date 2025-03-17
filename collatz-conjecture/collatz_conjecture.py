def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    if number % 2 == 0:
        number = number / 2
    else:
        number = (number * 3) + 1

    if number > 1:
        steps(number)
