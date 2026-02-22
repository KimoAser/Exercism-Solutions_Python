import re
def count_words(sentence):
    cleaned_first = re.sub(r"[^\w\s']"," ",sentence)
    cleaned_first = cleaned_first.replace('_', ' ')
    cleaned_second = re.sub(r"'(?![strSTR])", "", cleaned_first)
    lowered=cleaned_second.lower()
    splitted=lowered.split()
    dict_ = {}
    for word in splitted:
        dict_[word] = splitted.count(word)
    return dict_
