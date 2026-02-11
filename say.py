def say(number):
    first_numbers = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',
                     7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',
                     14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',
                     20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',
                     }
    if number == 0:
        return 'zero'
    if number > 999999999999 or number < 0:
            raise ValueError("input out of range")
    def under_1000(n):
        first_digit = n%10
        tens = (n%100)-first_digit
        hundreds = n // 100
        if n <= 20:
            return first_numbers[n]
        elif n > 20 and n < 100:
            if n%10 != 0:
                return f'{first_numbers[tens]}-{first_numbers[first_digit]}' 
            elif n%10 == 0:
                return f'{first_numbers[tens]}'
        elif 100 <= n < 1000:
            if n%100 == 0:
                return f'{first_numbers[hundreds]} hundred'
            elif n%100 != 0:
                if n%10 == 0:
                    return f'{first_numbers[hundreds]} hundred {first_numbers[tens]}'
                elif n%10 != 0:
                    special = n%100
                    if 11<=special<=19:
                        return f'{first_numbers[hundreds]} hundred {first_numbers[special]}'
                    return f'{first_numbers[hundreds]} hundred {first_numbers[tens]}-{first_numbers[first_digit]}'
    billions = number // 1000000000
    millions = (number//1000000)%1000
    thousands = (number//1000)%1000
    units = number%1000
    result = []
    if billions>0:
        result.append(under_1000(billions)+' billion')
    if millions>0:
        result.append(under_1000(millions)+' million')
    if thousands>0:
        result.append(under_1000(thousands)+' thousand')
    if units>0:
        result.append(under_1000(units))
    return ' '.join(result)
