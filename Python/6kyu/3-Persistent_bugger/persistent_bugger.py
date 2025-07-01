def persistence(n):
   nb_multiplication = 0
   numbers = map(int,str(n))
   nb_digit = len(list(map(int,str(n))))


   while nb_digit > 1:
    product = 1
    for number in numbers:
        product = product * number
        print(number)
    print(product)
    numbers = map(int,str(product))
    nb_digit = len(list(map(int,str(product))))
    nb_multiplication += 1
   return nb_multiplication

print(persistence(999))


# Whithout conversion of string
# def persistence(n):
#     n = str(n)
#     count = 0
#     while len(n) > 1:
#         p = 1
#         for i in n:
#             p *= int(i)
#         n = str(p)
#         count += 1
#     return count
