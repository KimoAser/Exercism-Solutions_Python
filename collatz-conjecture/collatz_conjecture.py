def steps(number):
    counts = 0
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    else:
        while number > 1:
            if number % 2 == 0:
                number = number / 2
                counts += 1
                continue
            if number % 2 != 0:
                number = (number*3)+1
                counts += 1
                continue
        if number == 1:
            return counts
print(steps(124))