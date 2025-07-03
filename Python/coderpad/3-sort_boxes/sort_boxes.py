import sys
import math
from contextlib import redirect_stdout


def solve(weight_0, weight_1, weight_2):
    dict_of_trays = {1:weight_0, 2:weight_1, 3:weight_2}
    selected_parcel = max(dict_of_trays.items(), key = lambda tray: tray[1])
    print(selected_parcel)
    return selected_parcel[0]


weight_1 = 130
weight_2 = 50
weight_3 = 200

print(solve(weight_1, weight_2, weight_3))


# Ignore and do not change the code below
# def main():
#     # pylint: disable = C, W

#     # game loop
#     while True:
#         weight_0 = int(input())
#         weight_1 = int(input())
#         weight_2 = int(input())
#         with redirect_stdout(sys.stderr):
#             action = solve(weight_0, weight_1, weight_2)
#         print(action)


# if __name__ == "__main__":
#     main()
# Ignore and do not change the code above
