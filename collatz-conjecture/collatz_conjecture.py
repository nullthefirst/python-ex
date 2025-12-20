def steps(number):
    if number <= 0:
        # example when argument is zero or a negative integer
        raise ValueError("Only positive integers are allowed")
    else:
        steps = 0
        value = number

        while value > 1:
            if value % 2 == 0:
                value /= 2
                steps += 1
            else:
                value = value * 3 + 1
                steps += 1

        return steps
