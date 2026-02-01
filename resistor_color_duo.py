def value(colors):
    result = ''
    count = 0
    for i in colors:
        if count < 2:
            if i == 'black':
                result += str(0)
                count += 1
                continue
            if i == 'brown':
                result += str(1)
                count += 1
                continue
            if i == 'red':
                result += str(2)
                count += 1
                continue
            if i == 'orange':
                result += str(3)
                count += 1
                continue
            if i == 'yellow':
                result += str(4)
                count += 1
                continue
            if i == 'green':
                result += str(5)
                count += 1
                continue
            if i == 'blue':
                result += str(6)
                count += 1
                continue
            if i == 'violet':
                result += str(7)
                count += 1
                continue
            if i == 'grey':
                result += str(8)
                count += 1
                continue
            if i == 'white':
                result += str(9)
                count += 1
                continue
    return int(result)
