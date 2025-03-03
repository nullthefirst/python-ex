def leap_year(year):
    """Determine if input year is a leap year based off the rules below.

    A leap year (in the Gregorian calendar) occurs:
    - In every year that is evenly divisible by 4.
    - Unless the year is evenly divisible by 100, in which case it's only a leap year if the year is also evenly divisible by 400.

    Args:
        year (int): year to be assessed per leap year logic.
    """

    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return True
    else:
        if year % 4 == 0 and year % 100 != 0:
            return True
        else:
            return False
