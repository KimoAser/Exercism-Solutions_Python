def decode(string):
    count = ''
    result = ''
    if string == '':
        return result
    for letter in range(0,len(string)):
        if string[letter].isdigit():
            count += string[letter]
        elif string[letter].isalpha() or string[letter].isspace():
            if count == '':
                result += string[letter]
            else:
                result += int(count) * string[letter]
            count = ''
    return result


def encode(string):
    result = ''
    count = 1
    if string == '':
        return result
    for i in range(1,len(string)):
        if string[i] == string[i-1]:
            count += 1
        else:
            if count == 1:
                result += string[i-1]
            else:
                result += str(count) + string[i-1]
            count = 1
    if count == 1:
        result += string[-1]
    elif count > 1:
        result += str(count) + string[-1]
    return result
