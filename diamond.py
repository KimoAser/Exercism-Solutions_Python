def rows(letter):
    listing =[]
    index = ord(letter) - ord('A')
    for i in range(index+1):
        letter = chr(ord('A')+i)
        spaces = index - i
        if letter == 'A':
            listing.append(' '*spaces+letter+' '*spaces)
        else:
            inner_spaces = 2*i -1
            listing.append(' '*spaces+letter+' '*inner_spaces+letter+' '*spaces)
    bottom = listing[:-1][::-1]
    listing.extend(bottom)
    return listing
