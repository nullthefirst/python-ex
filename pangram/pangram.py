import string, re

def is_pangram(sentence):
    alphabet = {letter: 0 for letter in string.ascii_lowercase}

    sentence_lower = sentence.lower()

    sentence_chars = re.sub(r'\s+', '', sentence_lower)

    for char in sentence_chars:
        if char in alphabet.keys():
            alphabet[char] += 1

    alphabet_list = [[key, value] for key, value in alphabet.items() if value > 0]

    return False if len(alphabet_list) < 26 else True

