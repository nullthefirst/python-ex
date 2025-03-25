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



def translate(text):
    output = text

    if rule_1(text):
        output += "ay"
    elif rule_3(text):
        anchor = output.index("qu") + 2

        # include logic to split string differently if any vowels exist before "qu"

        suffix = output[anchor:]

        first_half = output[:anchor]

        prefix = first_half[:anchor - 2]

        print(":::", prefix)

        vowel_present = []

        for letter in prefix:
            if letter in vowels:
                vowel_present.append(True)

        if not any(vowel_present):
            output = suffix + first_half + "ay"
        else:
            output = logic(output)
    elif rule_2(text):
        output = logic(output)

    return output


print(translate("liquid"))
