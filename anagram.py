def find_anagrams(word, candidates):
    listing = []
    for i in candidates:
        if word.lower() == i.lower():
            continue
        if sorted(word.lower()) == sorted(i.lower()):
            listing.append(i)
    return listing
