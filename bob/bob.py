def response(hey_bob):
    question = hey_bob.strip()

    if question.isupper():
        if question.endswith("?"):
            return "Calm down, I know what I'm doing!"
        else:
            return "Whoa, chill out!"
    elif question.endswith("?"):
        return "Sure."
    elif question == "":
        return "Fine. Be that way!"
    else:
        return "Whatever."
