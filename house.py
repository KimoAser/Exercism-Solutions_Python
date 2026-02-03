def recite(start_verse, end_verse):
    clauses = [
        "the house that Jack built.",
        "the malt that lay in",
        "the rat that ate",
        "the cat that killed",
        "the dog that worried",
        "the cow with the crumpled horn that tossed",
        "the maiden all forlorn that milked",
        "the man all tattered and torn that kissed",
        "the priest all shaven and shorn that married",
        "the rooster that crowed in the morn that woke",
        "the farmer sowing his corn that kept",
        "the horse and the hound and the horn that belonged to",
    ]
    rhyme = []
    for i in range(start_verse,end_verse+1):
        parts = ['This is ' + clauses[i-1]]
        for j in range(i-2,-1,-1):
            parts.append(clauses[j])
        rhyme.append(' '.join(parts))
    return rhyme
