def square_of_sum(number):
    listing = []
    for num in range(number):
        listing.append(num+1)
    total = sum(listing)
    sq_of_sum = total ** 2
    return sq_of_sum


def sum_of_squares(number):
    listing = []
    for num in range(1,number+1):
        sq = num ** 2
        listing.append(sq)
    total = sum(listing)
    return total
    

def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
