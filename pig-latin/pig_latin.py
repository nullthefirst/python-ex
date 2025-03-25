def rule_1(data):
    starter = ["a", "e", "i", "o", "u", "xr", "yt"]

    verdict = None

    for chars in starter:
        if data.lower().startswith(chars):
            verdict = True

    return verdict


def rule_2(data):
    vowels = ["a", "e", "i", "o", "u"]

    chars = list(data)

    word = []
    verdict = None

    for letter in chars:
        if letter not in vowels:
            pass
        else:
            vowel_start = chars.index(letter)

            # reorder word starting with vowel
            word += chars[vowel_start:]
            # attach constants to word end
            word += chars[:vowel_start]

            verdict = True

    "".join(word)
    word += "ay"
    print(word)

    return [verdict, word]


def translate(text):
    output = text

    if rule_1(text):
        output += "ay"
    elif rule_2(text)[0]:
        output = rule_2(text)[1]

    return output
