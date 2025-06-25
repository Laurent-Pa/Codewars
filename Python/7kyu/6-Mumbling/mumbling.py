def accum(st):
    mumble = []
    for index, letter in enumerate(st):
        repetition  = index + 1
        letter_to_string = letter.lower() * repetition
        mumble.append(letter_to_string.capitalize())

    return "-".join(mumble)


input = "ZpglnRxqenU"
output = "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu"

result = accum(input) == output
print(accum(input))
print(result)


# Solution en une seule ligne
# def accum(s):
#   return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))
