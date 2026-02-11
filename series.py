def slices(series, length):
    listing = []
    if length < 0:
        raise ValueError("slice length cannot be negative")
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if series == '':
        raise ValueError("series cannot be empty")
    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")
    for num in range(0,len(series)-length+1):
         listing.append(series[num:num+length])
    return listing
