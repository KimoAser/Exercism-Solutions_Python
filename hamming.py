def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    count = 0
    index = 0
    while index < len(strand_a):
        if strand_a[index] == strand_b[index]:
            index += 1
        elif strand_a[index] != strand_b[index]:
            count += 1
            index += 1
    return count