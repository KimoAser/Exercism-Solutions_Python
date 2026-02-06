def flatten(iterable):
    listing = []
    for item in iterable:
        if type(item) == int:
            listing.append(item)
        elif type(item) == list:
            listing.extend(flatten(item))
        elif item == None:
            continue
    return listing
