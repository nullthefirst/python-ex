import string, re

def is_pangram(sentence):
    alphabet = {letter: 0 for letter in string.ascii_lowercase}

    print(sentence)

    sentence_lower = sentence.lower()
    sentence_chars = re.sub(r'\s+', '', sentence_lower)

    for char in sentence_chars:
        if char in alphabet.keys():
            alphabet[char] += 1

    print(alphabet)

    verdict = False

    for key, value in alphabet.items():
        if value == 0:
            verdict = False
        else:
            verdict = True

    return verdict


text = "The quick brown fox jumps 019 over the lazy dog."
text_2 = "five boxing wizards jump quickly at it"

print(is_pangram(text_2))
