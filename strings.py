"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """

    return 'un'+word


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """

    first_index = ' :: '+ vocab_words[0]
    return first_index.join(vocab_words)


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """

    last = word[:-4]
    listing = []
    for letter in last:
        listing.append(letter)
    if listing[-1] == 'i':
        listing[-1] = 'y'
        final = ''.join(listing)
        return final
    final = ''.join(listing)
    return final


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """

    splitting = sentence.split()
    listing = []
    word = splitting[index]
    for letter in word:
        listing.append(letter)
    if listing[-1] == '.':
        listing.pop()
        final = ''.join(listing)
        added = final + 'en'
        return added
    final = ''.join(listing)
    added = final + 'en'
    return added
print(adjective_to_verb('It got dark as the sun set.', 2))