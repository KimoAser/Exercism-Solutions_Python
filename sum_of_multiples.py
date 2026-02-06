def sum_of_multiples(limit, multiples):
    numbers = set()
    for i in multiples:
        for j in range(0,limit,1):
            result = i * j
            if result < limit:
                numbers.add(result)
    return sum(numbers)
