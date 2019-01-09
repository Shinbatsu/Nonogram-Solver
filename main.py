
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