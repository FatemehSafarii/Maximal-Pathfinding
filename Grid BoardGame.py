def valid(board, row, column, cc, lc):
    x, y = cc
    output = []
    if x - 1 >= 0 and board[x - 1][y] == 1 and (x - 1, y) != lc:
        output.append((x - 1, y))
    if y - 1 >= 0 and board[x][y - 1] == 1 and (x, y - 1) != lc:
        output.append((x, y - 1))
    if x + 1 < row and board[x + 1][y] == 1 and (x + 1, y) != lc:
        output.append((x + 1, y))
    if y + 1 < column and board[x][y + 1] == 1 and (x, y + 1) != lc:
        output.append((x, y + 1))
    return output


def move(board, row, column):
    if board[0][0] == 0:
        return 0
    branches = [1, [(0, 0)]]
    first_time = True
    while len(branches) != 1:
        if first_time:
            valid_move = valid(board, row, column, branches[1][-1], (-2, -2))
            first_time = False
        else:
            valid_move = valid(board, row, column, branches[1][-1], branches[1][-2])
        length = len(valid_move)
        while length != 0:
            branches[1].append(valid_move[0])
            temp = branches[1][:-1]
            for i in range(1, length):
                branches.append(temp + [valid_move[i]])
            valid_move = valid(board, row, column, branches[1][-1], branches[1][-2])
            length = len(valid_move)
        branches[0] = max(branches[0], len(branches[1]))
        del branches[1]
    return branches[0]


_row = input().split(' ')
_column = int(_row[1])
_row = int(_row[0])
_board = []
for _i in range(_row):
    _board.append(list(map(int, list(input()))))
print(move(_board, _row, _column))
