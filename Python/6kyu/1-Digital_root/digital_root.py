def digital_root(n):
    sum_of_digits = 0
    number_in_string = str(n)
    if len(number_in_string) == 1:
        return n
    else:
        for number in number_in_string:
            sum_of_digits += int(number)
        return digital_root(sum_of_digits)


number = 493193
print(digital_root(number))


# solution en une seule ligne
# return n if n < 10 else digital_root(sum(map(int,str(n))))
