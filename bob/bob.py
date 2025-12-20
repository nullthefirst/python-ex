def response(hey_bob):
    question = hey_bob.strip()

    if len(question) == 0:
        return "Fine. Be that way!"
    else:
        if question.isupper():
            if question[-1] == "?":
                return "Calm down, I know what I'm doing!"
            else:
                return "Whoa, chill out!"
        else:
            if question[-1] == "?":
                return "Sure."
            else:
                return "Whatever."
