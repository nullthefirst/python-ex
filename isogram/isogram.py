import re

def is_isogram(string):
    if len(string) == 0:
        return True

    cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', string.lower())

    verdict = False

    string_characters = list()

    for char in cleaned_string:
        string_characters.append(char)

    char_count = dict()

    for el in string_characters:
        char_count[el] = 0

    for key, values in char_count.items():
        for el in string_characters:
            if key == el:
                char_count[el] += 1

    for key, value in char_count.items():
        if value > 1:
            return False
        else:
            verdict = True

    return verdict
