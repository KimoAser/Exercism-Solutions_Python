def convert(number):
    if number % 3 == 0:
        if number % 5 == 0:
            if number % 7 == 0:
                return 'PlingPlangPlong'
            return 'PlingPlang'
        if number % 7 == 0:
            if number % 5 ==0:
                return 'PlingPlongPlang'
            return 'PlingPlong'
        return 'Pling'
    if number % 5 == 0:
        if number % 3 ==0:
            if number % 7 ==0:
                return 'PlangPlingPlong'
            return 'PlangPling'
        if number % 7 == 0:
            if number % 3 ==0:
                return 'PlangPlongPling'
            return 'PlangPlong'
        return 'Plang'
    if number % 7 == 0:
        if number % 3 == 0:
            if number % 5 ==0:
                return 'PlongPlingPlang'
            return 'PlongPling'
        if number % 5 == 0:
            if number%3==0:
                return 'PlongPlangPling'
            return 'PlongPlang'
        return 'Plong'
    return str(number)
