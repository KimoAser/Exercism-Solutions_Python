def recite(start_verse, end_verse):
    days = ["first", "second", "third", "fourth", "fifth",
            "sixth", "seventh", "eighth", "ninth",
            "tenth", "eleventh", "twelfth"]
    gifts = ['a Partridge in a Pear Tree.',
             'two Turtle Doves,',
             'three French Hens,',
             'four Calling Birds,',
             'five Gold Rings,',
             'six Geese-a-Laying,',
             'seven Swans-a-Swimming,',
             'eight Maids-a-Milking,',
             'nine Ladies Dancing,',
             'ten Lords-a-Leaping,',
             'eleven Pipers Piping,',
             'twelve Drummers Drumming,']
    listing = []
    for i in range(start_verse,end_verse+1):
        verse = f'On the {days[i-1]} day of Christmas my true love gave to me: '
        gifts_part = []
        for j in range(i,0,-1):
            if j == 1 and i != 1:
                gifts_part.append(f'and {gifts[j-1]}')
            else:
                gifts_part.append(gifts[j-1])
        verse += " ".join(gifts_part)
        listing.append(verse)
        if i != end_verse:
            listing.append("")
    return listing
