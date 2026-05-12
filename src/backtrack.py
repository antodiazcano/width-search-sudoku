"""Script to implement the backtrack algorithm"""

from copy import deepcopy

from src.sudoku import Sudoku


def _find_first_empty_cell(sudoku: Sudoku) -> tuple[int, int]:
    """Returns the first empty cell of the board.

    Args:
        sudoku: Sudoku.

    Returns:
        X and Y positions of the first empty cell.
    """

    flag = False
    for x in range(sudoku.n):
        for y in range(sudoku.n):
            if sudoku.board[x][y] == 0:
                coord_x = x
                coord_y = y
                flag = True
                break
        if flag:
            break

    return coord_x, coord_y


def _generate_all_new_sudokus(
    sudokus: list[Sudoku], coord_x: int, coord_y: int
) -> list[Sudoku]:
    """Generates all the new possible sudokus based on the previous backtrack step.

    Args:
        sudokus: List with the sudokus of the previous backtrack step.
        coord_x: X position of the first empty cell.
        coord_y: Y position of the first empty cell.

    Returns:
        New possible sudokus.
    """

    new_sudokus = []

    for sudoku in sudokus:
        for num in range(1, 10):
            if sudoku.possible_move(coord_x, coord_y, num):
                new_sudoku = Sudoku(deepcopy(sudoku.board))
                new_sudoku.add_number(coord_x, coord_y, num)
                new_sudokus.append(new_sudoku)

    return new_sudokus


def _print_progress(new_sudokus: list[Sudoku], n_zeros: int) -> None:
    """Prints the status of the current backtrack step.

    Args:
        new_sudokus: List with the new sudokus for this iteration.
        n_zeros: Number of cells to still fill.
    """

    if n_zeros == 1:
        print(f"{n_zeros} cell left")
    else:
        print(f"{n_zeros} cells left")

    print("Current sudokus:", len(new_sudokus))

    possible_sudokus = len(new_sudokus) * 9**n_zeros
    threshold = 1e6
    if possible_sudokus > threshold:
        print(f"Possible sudokus: {possible_sudokus:.2e}\n")
    else:
        print(f"Possible sudokus: {possible_sudokus}\n")


def backtrack(sudokus: list[Sudoku]) -> list[Sudoku]:
    """Backtrack algorithm.

    Args:
        boards: List of sudokus.

    Returns:
        Winning sudokus (empty list if there is no solution).
    """

    if len(sudokus) == 0:
        print("No solutions found!")
        return []

    coord_x, coord_y = _find_first_empty_cell(sudokus[0])
    new_sudokus = _generate_all_new_sudokus(sudokus, coord_x, coord_y)
    if len(new_sudokus) == 0:
        print("No solutions found!")
        return []
    n_zeros = sum(
        1 for row in new_sudokus[0].board for cell in row if cell == 0
    )  # number of cells to still fill
    _print_progress(new_sudokus, n_zeros)

    # Return solutions in case all cells are filled
    if n_zeros == 0:
        solutions = []
        for sudoku in new_sudokus:
            if sudoku.win():
                solutions.append(sudoku)
        return solutions

    return backtrack(new_sudokus)
