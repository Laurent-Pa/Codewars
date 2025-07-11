import itertools

def get_pins(observed):

    def combine_list_of_combinations(list_of_lists):
        """Combine les listes entre elles"""
        if not list_of_lists:
            return []

        return list(itertools.product(*list_of_lists))

    list_of_combinations = []
    possible_combinations = []
    possible_digits = []
    adjacent_digits = {"1":["1","2","4"],
                       "2":["1","2","3","5"],
                       "3":["2","3","6"],
                       "4":["1","4","5","7"],
                       "5":["2","4","5","6","8"],
                       "6":["3","5","6","9"],
                       "7":["4","7","8"],
                       "8":["5","7","8","9","0"],
                       "9":["6","8",'9'],
                       "0":["0","8"]}
    nb_digits = len(observed)

    for index in range(nb_digits):
        possible_digits = adjacent_digits[observed[index]]
        possible_combinations.append(possible_digits)

    combinations = combine_list_of_combinations(possible_combinations)
    for combination in combinations:
        list_of_combinations.append("".join(combination))

    return list_of_combinations

# input = "8"
# output =['5','7','8','9','0']
# get_pins(input)

input = '11'
output = ["11", "22", "44", "12", "21", "14", "41", "24", "42"]
print(get_pins(input))


### Solution en une ligne du kata"

from itertools import product


PIN = {'1': ('1', '2', '4'),
       '2': ('1', '2', '3', '5'),
       '3': ('2', '3', '6'),
       '4': ('1', '4', '5', '7'),
       '5': ('2', '4', '5', '6', '8'),
       '6': ('5', '6', '9', '3'),
       '7': ('4', '7', '8'),
       '8': ('7', '5', '8', '9', '0'),
       '9': ('6', '8', '9'), '0': ('0', '8')}


def get_pins_solution(observed):
    return [''.join(a) for a in product(*(PIN[b] for b in observed))]
