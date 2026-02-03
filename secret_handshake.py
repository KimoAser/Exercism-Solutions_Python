def commands(binary_str):
    listing = []
    if binary_str[-1] == '1':
        listing.append('wink')
    if binary_str[-2] == '1':
        listing.append('double blink')
    if binary_str[-3] == '1':
        listing.append('close your eyes')
    if binary_str[-4] == '1':
        listing.append('jump') 
    if binary_str[-5] == '1':
        listing.reverse()
    return listing