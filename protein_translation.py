def proteins(strand):
    listing = []
    items = {'AUG':'Methionine',
             'UUU':'Phenylalanine','UUC':'Phenylalanine',
             'UUA':'Leucine','UUG':'Leucine',
             'UCU':'Serine','UCC':'Serine','UCA':'Serine','UCG':'Serine',
             'UAU':'Tyrosine','UAC':'Tyrosine',
             'UGU':'Cysteine','UGC':'Cysteine',
             'UGG':'Tryptophan',
             'UAA':'STOP',
             'UAG':'STOP',
             'UGA':'STOP'}
    for i in range(0,len(strand),3):
        seperated = strand[i:i+3]
        if items[seperated] == 'STOP':
            break
        else:
            listing.append(items[seperated])
        
    return listing
