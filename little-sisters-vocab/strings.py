"""Functions for creating, transforming, and adding prefixes to strings."""

import re


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """

    return "un" + word


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

    prefix = vocab_words[0]

    prefixed_words = []

    for word in vocab_words:
        prefixed_words.append("{0}{1}".format(prefix, word))

    prefixed_words = prefixed_words[1:]

    prefixed_words.reverse()

    prefixed_words.append(prefix)

    prefixed_words.reverse()

    word_groups = " :: ".join(prefixed_words)

    return word_groups


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """

    word_content = word.split("ness")

    word_root = word_content[0]

    if word_root[-1] == "i":
        word_root_chars = word_root.split()[0]
        word_root_chars = word_root_chars[:-1]
        word_root_chars += "y"
        word_root = word_root_chars

    return word_root


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """

    word = sentence.split()[index]
    word += "en"

    return re.sub("[^\w\s]", "", word) # removes any special characters near the former adjective

print(adjective_to_verb('It got dark as the sun set.', 2))
