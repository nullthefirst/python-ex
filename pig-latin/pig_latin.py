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

def rule_3(data):
    verdict = False

    if "qu" in data:
        verdict = True

    return verdict

def logic(data):
    output = list(data)
    original = output[:]  # Keep track of original sequence

    while output and output[0] not in vowels:
        non_vowel = output.pop(0)
        output.append(non_vowel)

        # If we rotated back to the original sequence, stop to prevent infinite loop
        if output == original:
            break

    output = "".join(output)
    output += "ay"

    return output


def prior(data, marker):
    anchor = data.index(marker) + 2

    suffix = data[anchor:]

    first_half = data[:anchor]

    prefix = first_half[:anchor - 2]

    vowel_present = []

    for letter in prefix:
        if letter in vowels:
            vowel_present.append(True)

    return (not any(vowel_present), [suffix, first_half])


def translate(text):
    output = text

    if rule_1(text):
        output += "ay"
    elif rule_2(text):
        if rule_3(text):
            if prior(output, "qu")[0]:
                suffix, first_half = prior(output, "qu")[1]
                output = suffix + first_half + "ay"
            else:
                output = logic(output)
        else:
            output = logic(output)

    return output

