import string

def is_pangram(sentence):
    alphabet_list = list(string.ascii_lowercase)

    lower_sentence = sentence.lower()

    punctuation_remover = str.maketrans("", "", string.punctuation)
    sentence_cleaned = lower_sentence.translate(punctuation_remover)

    count = dict()

    for char in sentence_cleaned:
        if char in alphabet_list:
            count[char] = 0

    for char in sentence_cleaned:
        if char in alphabet_list:
            count[char] += 1

    if sorted(count.keys()) == alphabet_list:
        return True
    else:
        return False

x = is_pangram("The quick brown fox jumps over the lazy dog.")
print(x)
