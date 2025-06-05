def leap_year(year):
    verdict = None

    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            verdict = False
        else:
            verdict = True
    else:
        verdict = False

    return verdict
