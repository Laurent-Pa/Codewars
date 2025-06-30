def product_fib(_prod):
    fibonacci = [0,1]
    n = 0
    product_fib = 0

    while product_fib <= _prod :
        product_fib = fibonacci[n] * fibonacci[n+1]
        if product_fib == _prod:
            return [fibonacci[n], fibonacci[n+1], True]
        elif product_fib > _prod:
            return [fibonacci[n], fibonacci[n+1], False]
        else:
            fibonacci.append(fibonacci[n] + fibonacci[n+1])
            n += 1


# print(product_fib(714) == [21, 34, True])
print(product_fib(800) == [34, 55, False])

# Solutions compacte:
#   a, b = 0, 1
#   while prod > a * b:
#     a, b = b, a + b
#   return [a, b, prod == a * b]
