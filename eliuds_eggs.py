def egg_count(display_value):
    result = 0
    binary = bin(display_value)
    clean = binary[2:]
    for bit in clean:
        num = int(bit)
        result += num
    return result