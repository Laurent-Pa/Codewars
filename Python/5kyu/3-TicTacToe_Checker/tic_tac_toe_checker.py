from collections import Counter

def is_solved(board):
    column1 = []
    column2 = []
    column3 = []

    for line in board:
        # checking the lines
        line_counter = Counter(line)
        del line_counter[0]
        if 3 in line_counter.values():
            return line[0]

        # getting values from the columns
        column1.append(line[0])
        column2.append(line[1])
        column3.append(line[2])
    columned_board = [column1, column2, column3]

    # checking the columns
    for column in columned_board:
        column_counter = Counter(column)
        del column_counter[0]
        if 3 in column_counter.values():
            return column[0]

    # checking the diagonal
    center  = board[1][1]
    if center != 0:
        if center == board[0][0] and center == board[2][2] or center == board[0][2] and center == board[2][0]:
            return center

    # checking if there are still some spot available
    for line in board:
        if 0 in line:
            return -1

    # if there is no winner and no spot available
    return 0

### Tests ###

board = [[0, 0, 1],
         [0, 1, 2],
         [2, 1, 0]]
result = -1
print(is_solved(board) == result)

board = [[1, 1, 1],
         [0, 2, 2],
         [0, 0, 0]]
result = 1
print(is_solved(board) == result)

board = [[2, 1, 2],
         [2, 1, 1],
         [1, 1, 2]]
result = 1
print(is_solved(board) == result)

board = [[2, 1, 2],
         [2, 1, 1],
         [1, 2, 1]]
result = 0
print(is_solved(board) == result)
