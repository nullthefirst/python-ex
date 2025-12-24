import string

def is_valid(isbn):
    raw_input = list()

    validity = None

    for char in isbn:
        raw_input.append(char)

    nums = list()

    for char in raw_input:
        if char == "-":
            pass
        elif char in string.ascii_uppercase and char != "X":
            return False
        elif char == "X" and raw_input.index(char) != len(raw_input) - 1:
            pass
        elif char == "X" and raw_input.index(char) == len(raw_input) - 1:
            nums.append(10)
        else:
            nums.append(int(char))

    print(nums)

    if len(nums) > 10 or len(nums) < 10:
        validity = False
        checker = False
    else:
        validity = True
        checker = (nums[0] * 10 + nums[1] * 9 + nums[2] * 8 + nums[3] * 7 + nums[4] * 6 + nums[5] * 5 + nums[6] * 4 + nums[7] * 3 + nums[8] * 2 + nums[9] * 1) % 11 == 0

    return validity and checker
