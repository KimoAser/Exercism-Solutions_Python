import re
def abbreviate(words):
    listing = []
    spaced = re.sub(r"[^a-zA-Z0-9']",' ',words)
    splitted = spaced.split()
    for word in splitted:
        listing.append(word[0].upper())
    return ''.join(listing)
