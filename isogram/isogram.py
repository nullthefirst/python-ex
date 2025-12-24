import string

def is_isogram(string_input):
    # perform data cleaning on string input

    alphabet_list = list(string.ascii_lowercase)

    lower_sentence = string_input.lower()

    punctuation_remover = str.maketrans("", "", string.punctuation)
    sentence_cleaned = lower_sentence.translate(punctuation_remover)

    # create dictionary with string char frequency

    count = dict()

    for char in sentence_cleaned:
        if char in alphabet_list:
            count[char] = 0

    for char in sentence_cleaned:
        if char in alphabet_list:
            count[char] += 1

    # assess the repetition frequency of characters

    verdict = list()

    for key, value in count.items():
        if value > 1:
            verdict.append(False)
        else:
            verdict.append(True)

    # return False if valid characters less than number of unique string characters

    if sum(verdict) != len(count.keys()):
        return False
    else:
        return True
