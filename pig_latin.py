def translate(text):
    vowels = ('a','e','i','o','u')
    spliited = text.split()
    final = []
    for word in spliited:
        index = 0
        if word.startswith(vowels) or word.startswith('xr') or word.startswith('yt'):
            final.append(word +'ay') 
            break
        while index < len(word):
            if word[index:index+2] == 'qu':
                index += 2
                break
            elif word[index] in vowels:
                break
            elif word[index] == 'y' and index != 0 :
                break
            index += 1
        final.append(word[index:] + word[:index] + 'ay')
    return ' '.join(final) 