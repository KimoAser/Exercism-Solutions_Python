def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    listing = []
    if number <= 0 :
        raise ValueError("Classification is only possible for positive integers.")
    for i in range(1,number):
        if number % i == 0:
            listing.append(i)
    result = sum(listing)
    if result == number:
        return 'perfect'
    if result < number:
        return 'deficient'
    return 'abundant'
