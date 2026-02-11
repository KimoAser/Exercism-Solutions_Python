def factors(value):
    index = 2
    listing = []
    while value != 1:
        if value % index == 0:
            value = value / index
            listing.append(index)
            continue
        elif value % index != 0:
            index += 1
            continue
    return listing
