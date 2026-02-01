def to_rna(dna_strand):
    result =''
    for char in dna_strand:
        if char == 'G':
            result += 'C'
            continue
        if char == 'C':
            result += 'G'
            continue
        if char == 'T':
            result += 'A'
            continue
        if char == 'A':
            result += 'U'
            continue
    return result
