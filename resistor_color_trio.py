def label(colors):
    result = ''
    count = 0
    for i in colors:
        if count < 2:
            if i == 'black':
                result += str(0)
                count +=1
                continue
            if i == 'brown':
                result += str(1)
                count +=1
                continue
            if i == 'red':
                result += str(2)
                count +=1
                continue
            if i == 'orange':
                result += str(3)
                count +=1
                continue
            if i == 'yellow':
                result += str(4)
                count +=1
                continue
            if i == 'green':
                result += str(5)
                count +=1
                continue
            if i == 'blue':
                result += str(6)
                count +=1
                continue
            if i == 'violet':
                result += str(7)
                count +=1
                continue
            if i == 'grey':
                result += str(8)
                count +=1
                continue
            if i == 'white':
                result += str(9)
                count +=1
                continue
    if colors[2] == 'black':
        result += ''
    if colors[2] == 'brown':
        result += '0'
    if colors[2] == 'red':
        result += '00'
    if colors[2] == 'orange':
        result += '000'
    if colors[2] == 'yellow':
        result += '0000'
    if colors[2] == 'green':
        result += '00000'
    if colors[2] == 'blue':
        result += '000000'
    if colors [2] == 'violet':
        result += '0000000'
    if colors[2] == 'grey':
        result += '00000000'
    if colors[2] == 'white':
        result += '000000000'
    
    result = int(result)
    prefixes = [
        (1_000_000_000, 'gigaohms'),
        (1_000_000, 'megaohms'),
        (1_000, 'kiloohms'),
    ]
    if result == 0:
        return '0 ohms'
    for factor, name in prefixes:
        if result % factor == 0:
            return f"{result // factor} {name}"

    return f"{result} ohms"
