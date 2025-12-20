def translate(text):
    vowels = ["a", "e", "i", "o", "u"]

    statement = ""

    if text[0] in vowels:
        if text[0] in vowels:
            statement += text + "ay"
        elif "xr" in text or "yt" in text:
            statement += text + "ay"
    else:

        if "qu" in text:
            holder = text.split("qu")
            start = holder.pop(0)
            holder.append(start)
            word = "".join(holder)

            statement += "qu" + "ay"
            print(word)
        else:
            holder = []

            for char in text:
                holder.append(char)

            while holder[0] not in vowels:
                item = holder.pop(0)
                holder.append(item)

            statement = "".join(holder)
            statement += "ay"

    return statement

# translate("pig")
# translate("chair")
# translate("thrush")

translate("quick")
translate("square")
