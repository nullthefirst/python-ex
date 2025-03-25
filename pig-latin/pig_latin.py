vowels = ["a", "e", "i", "o", "u"]

def rule_1(data):
    starter = vowels + ["xr", "yt"]

    verdict = False

    for chars in starter:
        if data.lower().startswith(chars):
            verdict = True

    return verdict


def rule_2(data):
    verdict = False

    if data[0] not in vowels:
        verdict = True

    return verdict


def translate(text):
    output = text

    if rule_1(text):
        output += "ay"
    elif rule_2(text):
        output = list(output)

        while output[0] not in vowels:
            non_vowel = output.pop(0)

            output.append(non_vowel)

        output = "".join(output)
        output += "ay"

    return output

