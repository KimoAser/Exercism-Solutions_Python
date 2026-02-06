def transform(legacy_data):
    dict_ = dict()
    for integer,letters in legacy_data.items():
        for letter in letters:
            dict_[letter.lower()] = integer
    dict_sorted = dict(sorted(dict_.items()))
    return dict_sorted
