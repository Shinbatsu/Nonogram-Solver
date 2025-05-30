
from dp import dp


def solve_lines(board, clues, changed_rows, changed_columns, solved_cells, rotate=False):
    for index in changed_rows:
        line = ''.join([board[i][index] for i in range(len(board))]) if rotate else ''.join(board[index])
        delta = solve_line(line, clues[index], changed_columns, board, index, rotate)
        if delta is None:
            return None
        solved_cells += delta
    return solved_cells

def solve_line(line, groups, changed_columns, board, j, rotate=False):
    length, group_count = len(line), len(groups)
    whites = [False] * (length + 1)
    blacks = [False] * (length + 1)
    blacks_filled = [ch != 'X' for ch in line]
    prefix_whites = [0] * (length + 1)

    for i in range(length):
        prefix_whites[i + 1] = prefix_whites[i] + (line[i] == '.')

    memo = {}
    dp(0, 0, False, length, group_count, groups, whites, blacks, blacks_filled, prefix_whites, memo)

    solved_cells = 0
    for i in range(length):
        row, col = (i, j) if rotate else (j, i)
        if whites[i] and blacks[i]:
            board[row][col] = '?'
        elif whites[i]:
            if line[i] == '?':
                solved_cells += 1
                changed_columns.add(i)
            board[row][col] = '.'
        elif blacks[i]:
            if line[i] == '?':
                solved_cells += 1
                changed_columns.add(i)
            board[row][col] = 'X'
        else:
            return None
    return solved_cells
