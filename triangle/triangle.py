def istriangle(sides):
    a, b, c = sides

    if a <= 0 or b <= 0 or c <= 0:
        return False
    elif (a + b < c) or (b + c < a) or (c + a < b):
        return False
    else:
        return True


def equilateral(sides):
    a, b, c = sides

    if istriangle(sides):
        if a == b and b == c and a == c:
            return True
        else:
            return False
    else:
        return False


def isosceles(sides):
    pass


def scalene(sides):
    pass
