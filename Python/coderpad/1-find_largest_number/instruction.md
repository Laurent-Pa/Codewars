Implémentez la fonction find_largest(Numbers) afin qu'elle retourne le plus grand nombre dans le tableau d'entier Numbers.
Note: le tableau contient toujours au moins un élément.

# Python code below
# Use print("messages...") to debug your solution.

def find_largest(numbers):
    numbers.sort()
    return numbers[-1]


CODE DE TEST:
print(Answer.find_largest([7, 17, 13, 19, 5]))  # 19
