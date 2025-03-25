def rule_1(data):
    starter = ["a", "e", "i", "o", "u", "xr", "yt"]

    verdict = None

    for chars in starter:
        if data.lower().startswith(chars):
            verdict = True

    return verdict


def translate(text):
    output = text

    if rule_1(text):
        output += "ay"

    return output
