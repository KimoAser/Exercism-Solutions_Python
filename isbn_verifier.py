def is_valid(isbn):
    result = 0
    counter = 0
    for digit in isbn:
        if digit.isnumeric():
            result += int(digit) * (10 - counter)
            counter += 1
            continue
        if digit == '-':
            continue
        if digit == 'X' and counter == 9:
            result += 10 * (10 - counter)
            counter += 1
            continue
        if digit != "-" and counter != 9:
            return False
    if counter != 10:
        return False
    if result % 11 == 0:
        return True
    return False
        