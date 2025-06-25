def binary_array_to_number(arr):
  decimal = 0
  for index, bit in enumerate(reversed(arr)):
    decimal += bit * (2** index)
  return decimal


input = [1, 0, 1, 1]
output = 11
print(binary_array_to_number(input))
print(binary_array_to_number([0,0,1,0]) == 2)
print(binary_array_to_number([0,1,1,0]) == 6)

# Solution en une ligne
# return int("".join(map(str, arr)), 2)

# map(str, arr) - Convertit chaque élément en chaîne
# "".join(...) - Joint tous les éléments sans séparateur
# int(..., 2) - Convertit une chaîne binaire en décimal
