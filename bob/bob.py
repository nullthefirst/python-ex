def response(hey_bob):
    if hey_bob.isupper() and hey_bob.endswith("?"):
        return "Calm down, I know what I'm doing!"
    elif hey_bob.endswith("?"):
        return "Sure."
    else:
        return "Whatever."
