def validate(sides):
    a, b, c = sides

    valid = None

    if a == 0 or b == 0 or c == 0:
        valid = False
    elif a + b >= c or b + c >= a or a + c >= b:
        valid = True
    else:
        valid = True

    return valid


def equilateral(sides):
    return validate(sides) and (True if sides[0] == sides[1] == sides[2] else False)


def isosceles(sides):
    pass


def scalene(sides):
    a, b, c = sides

    return validate(sides) and (True if a != b and b != c and a != c else False)
