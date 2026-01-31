def leap_year(year):
    if not year % 400 == 0:
        if not year % 100 == 0:
            if year % 4 == 0:
                return True
            return False
        return False
    return True