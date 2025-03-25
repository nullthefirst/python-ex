def rule_1(data):
    starter = ["a", "e", "i", "o", "u", "xr", "yt"]

    verdict = False

    for chars in starter:
        if data.lower().startswith(chars):
            verdict = True

    return verdict


def rule_2(data):
    vowels = ["a", "e", "i", "o", "u"]

    chars = list(data)

    word = chars[:]
    verdict = False

    if data[0] not in vowels:
        verdict = True

    while word[0] not in vowels:
        non_vowel = word.pop(0)

        word.append(non_vowel)

    return [verdict, word]


def translate(text):
    output = text

    if rule_1(text):
        output += "ay"
    elif rule_2(text)[0]:
        output = rule_2(text)[1]
        output = "".join(output)
        output += "ay"

    return output

