from json import dumps, loads
import sys
from typing import List


def count_peaks(values: List[float]) -> int:
    '''

    Args:

        - values (List[float]): Les valeurs mesurées par le capteur de radioactivité

    Returns:

        Le nombre total de pics inférieurs et de pics supérieurs
    '''
    nb_data = len(values)
    list_peaks = []
    # Write your code here
    for index, value in enumerate(values):
        if index > 0 and index < nb_data - 1:
            prev_val = values[index - 1]
            current_val = values[index]
            next_val = values[index + 1]
            if (prev_val - current_val) >= 5 and (next_val - current_val) >= 5:
                list_peaks.append([index, "lower_peak"])
            elif (current_val - prev_val) >= 5 and (current_val - next_val) >= 5:
                list_peaks.append([index, "upper_peak"])
    print(list_peaks)
    nb_peaks = len(list_peaks)

    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    return nb_peaks

input = [8, 10.7, 17.1, 11.2, 13.5, 9.9, 14.9, 9.4, 9.4, 3.1, 12.7]
output = 3
print(count_peaks(input) == output)

# Ignore and do not change the code below


# def try_solution(nb_peaks: int):
#     '''
#     Try a solution

#     Args:

#         - int (int): Le nombre total de pics inférieurs et de pics supérieurs
#     '''
#     json = nb_peaks
#     print("" + dumps(json, separators=(',', ':')))

# def main():
#     res = count_peaks(
#         loads(input())
#     )
#     try_solution(res)


# if __name__ == "__main__":
    # main()
# Ignore and do not change the code above
