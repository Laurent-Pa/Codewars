def solution(input_number):
    multiples = []
    if input_number < 0:
        return 0
    range_of_below_numbers = range(input_number)
    # print(range_of_below_numbers)
    for number in range_of_below_numbers:
        if number%3 == 0 or number%5 == 0:
            multiples.append(number)
    return sum(multiples)

print (solution(4) == 3)
print(solution(16) == 60)

# solution en une seule ligne
# return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)
