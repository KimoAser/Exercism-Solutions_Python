import re
def encode(plain_text):
    listing = []
    result = ''
    no_space = re.sub(r'[^a-zA-Z0-9]','',plain_text)
    lowered = no_space.lower()
    for j in range(0,len(lowered),5):
        group =lowered[j:j+5]
        listing.append(group)
    cleaned = ' '.join(listing)
    for i in cleaned:
        if i == ' ':
            result += i
        elif i.isdigit():
            result += i
        elif i.isalpha():
            pos = ord(i)
            number = pos - ord('a')
            letter = chr(ord('z')-number)
            result += letter
    return result


def decode(ciphered_text):
    result = ''
    no_space = re.sub(r'[^a-zA-Z0-9]','',ciphered_text)
    for i in no_space:
        if i.isdigit():
            result += i
        elif i.isalpha():
            pos = ord(i)
            number = pos - ord('a')
            letter = chr(ord('z')-number)
            result += letter
    return result
