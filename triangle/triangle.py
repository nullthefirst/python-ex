def validate(sides):
    a, b, c = sides

    valid = None

    if a == 0 or b == 0 or c == 0:
        valid = False
    else:
        valid = True

    return valid


def equilateral(sides):
    return validate(sides) and (True if sides[0] == sides[1] == sides[2] else False)


def isosceles(sides):
    pass


def scalene(sides):
    pass
