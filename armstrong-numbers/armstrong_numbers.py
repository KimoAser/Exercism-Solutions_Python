def is_armstrong_number(number):
    b =str(number)
    c = list(b)
    listing = []
    result = 0
    for i in c:
        con = int(i)
        listing.append(con)
    for j in listing:
        result += j**len(c)
    if result == number:
        return True
    return False