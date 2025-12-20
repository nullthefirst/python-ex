def translate(text):
    vowels = ["a", "e", "i", "o", "u"]

    value = text.split()
    output = ""

    def base(text_string):
        statement = ""

        if text_string[0] in vowels or text_string.startswith(("xr", "yt")):
            statement += text_string + "ay"
        else:
            if "qu" in text_string:
                holder = text_string.split("qu")
                vowel_check = any(char in vowels for char in holder[0])

                if vowel_check:
                    bucket = list(text_string)

                    rotate_count = 0
                    for char in bucket:
                        if char in vowels:
                            break
                        rotate_count += 1

                    for _ in range(rotate_count):
                        item = bucket.pop(0)
                        bucket.append(item)

                    statement = "".join(bucket) + "ay"
                else:
                    start = holder.pop(0)
                    holder.append(start)
                    word = "".join(holder)
                    statement += word + "qu" + "ay"
            else:
                bucket = list(text_string)

                if "y" in bucket and not any(el in vowels for el in bucket):
                    rotate_count = 0
                    for char in bucket:
                        if char == "y":
                            break
                        rotate_count += 1

                    for _ in range(rotate_count):
                        item = bucket.pop(0)
                        bucket.append(item)

                    statement = "".join(bucket) + "ay"
                else:
                    rotate_count = 0
                    for char in bucket:
                        if char in vowels:
                            break
                        rotate_count += 1

                    for _ in range(rotate_count):
                        item = bucket.pop(0)
                        bucket.append(item)

                    statement = "".join(bucket) + "ay"

        return statement

    if len(value) > 1:
        for word in value:
            output += base(word) + " "
        output = output.strip()
    else:
        output += base(text)

    return output
