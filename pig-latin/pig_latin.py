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


def rule_4(data):
    verdict = False

    if data[0] != "y" and "y" in data:
        verdict = True

    return verdict

def spacer(data):
    verdict = False

    if " " in data:
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


def prior(data, marker, tuner):
    anchor = data.index(marker) + tuner

    suffix = data[anchor:]

    first_half = data[:anchor]

    prefix = first_half[:anchor - tuner]

    vowel_present = []

    for letter in prefix:
        if letter in vowels:
            vowel_present.append(True)

    return (not any(vowel_present), [suffix, first_half])


def sentence(data):
    feedback = []

    if spacer(data):
        content = data.split(" ")

        for word in content:
            feedback.append(engine(word))

        feedback = " ".join(feedback)

    return feedback


def engine(data):
    output = data

    if rule_1(data):
        output += "ay"
    elif rule_2(data):
        if rule_3(data):
            if prior(output, "qu", 2)[0]:
                suffix, first_half = prior(output, "qu", 2)[1]
                output = suffix + first_half + "ay"
            else:
                output = logic(output)
        elif rule_4(data):
            if prior(output, "y", 0)[0]:
                suffix, first_half = prior(output, "y", 0)[1]
                output = suffix + first_half + "ay"
            else:
                output = logic(output)
        else:
            output = logic(output)

    return output


def translate(text):
    output = ""

    if spacer(text):
        output += sentence(text)
    else:
        output += engine(text)

    return output

