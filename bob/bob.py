import re


def response(hey_bob):
    if len(hey_bob.strip()) == 0:
        return "Fine. Be that way!"
    elif len(hey_bob) > 1:
        if hey_bob.isupper():
            if hey_bob.endswith("?"):
                return "Calm down, I know what I'm doing!"
            else:
                return "Whoa, chill out!"
        else:
            if hey_bob[0] == " ":
                return "Whatever."
            else:
                return "Sure."


response("SDSVDV")
