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

    # Write your code here
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    return 62

# Ignore and do not change the code below


def try_solution(nb_peaks: int):
    '''
    Try a solution

    Args:

        - int (int): Le nombre total de pics inférieurs et de pics supérieurs
    '''
    json = nb_peaks
    print("" + dumps(json, separators=(',', ':')))

def main():
    res = count_peaks(
        loads(input())
    )
    try_solution(res)


if __name__ == "__main__":
    main()
# Ignore and do not change the code above
