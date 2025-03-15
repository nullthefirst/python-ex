def validate(sides):
    a, b, c = sides

    if a == 0 or b == 0 or c == 0:
        return False

    if a + b >= c or b + c >= a or a + c >= b:
        return True
    else:
        return False


def equilateral(sides):
    return validate(sides) and (True if sides[0] == sides[1] == sides[2] else False)


def isosceles(sides):
    a, b, c = sides

    two_sides = a == b or a == c or b == c

    checker = a + b < c or b + c < a or a + c < b

    return validate(sides) and (True if two_sides and not checker else False)


def scalene(sides):
    a, b, c = sides

    no_sides = a != b and b != c and a != c

    checker = a + b < c or b + c < a or a + c < b

    return validate(sides) and (True if no_sides and not checker else False)
