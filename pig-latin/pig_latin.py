def translate(text):
    vowels = ["a", "e", "i", "o", "u"]

    statement = ""

    if text[0] in vowels:
        statement += text + "ay"
    elif "xr" in text or "yt" in text:
        statement += text + "ay"

    return statement
