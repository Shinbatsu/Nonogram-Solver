
def solve(clues):
    ...
    
def cycle(board, row_clues, column_clues, height, width, total_cells):
    prev_count = -1
    iteration = 0
    solved_cells = 0
    rows_to_update, cols_to_update = [set(range(height)), set(range(width))]

    while prev_count < solved_cells < total_cells:
        updated_rows = set()
        prev_count = solved_cells
        iteration += 1

        solved_cells = solve_lines(board, row_clues, rows_to_update, cols_to_update, solved_cells)
        if solved_cells is None:
            return None

        solved_cells = solve_lines(board, column_clues, cols_to_update, updated_rows, solved_cells, rotate=True)
        if solved_cells is None:
            return None

        rows_to_update, cols_to_update = updated_rows, set()

    return solved_cells, iteration

def show_board(board):
    for row in board:
        print(''.join(row))

if __name__ == "__main__":
    result = solve((
        (
            (1, 1, 3), (3, 2, 1, 3), (2, 2), (3, 6, 3), (3, 8, 2), (15,), (8, 5), (15,),
            (7, 1, 4, 2), (7, 9), (6, 4, 2), (2, 1, 5, 4), (6, 4), (2, 6), (2, 5),
            (5, 2, 1), (6, 1), (3, 1), (1, 4, 2, 1), (2, 2, 2, 2)
        ),
        (
            (2, 1, 1), (3, 4, 2), (4, 4, 2), (8, 3), (7, 2, 2), (7, 5), (9, 4), (8, 2, 3),
            (7, 1, 1), (6, 2), (5, 3), (3, 6, 3), (2, 9, 2), (1, 8), (1, 6, 1), (3, 1, 6),
            (5, 5), (1, 3, 8), (1, 2, 6, 1), (1, 1, 1, 3, 2)
        )
    ))

    show_board(result)