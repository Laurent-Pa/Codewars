from collections import Counter

def find_uniq(arr):
    print(len(set(arr)))
    a, b = set(arr)
    counter_numb = Counter(arr)
    unique_numb = [numb for numb, value in counter_numb.items() if value == 1]
    return unique_numb[0]   # n: unique number in the array

input = [ 1, 1, 1, 2, 1, 1 ]
output = 2
print(find_uniq(input) == output)

input = [ 0, 0, 0.55, 0, 0 ]
output = 0.55
print(find_uniq(input) == output)


# solution Codewars
# def find_uniq(arr):
    # a, b = set(arr)
    # return a if arr.count(a) == 1 else b
