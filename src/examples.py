"""Script to solve some examples."""

from typing import Literal

import time
from src.backtrack import backtrack
from src.sudoku import Sudoku


def main() -> None:
    """Solves an example of a sudoku."""

    sudokus = {
        "easy": Sudoku(
            [
                [5, 3, 0, 0, 7, 0, 0, 0, 0],
                [6, 0, 0, 1, 9, 5, 0, 0, 0],
                [0, 9, 8, 0, 0, 0, 0, 6, 0],
                [8, 0, 0, 0, 6, 0, 0, 0, 3],
                [4, 0, 0, 8, 0, 3, 0, 0, 1],
                [7, 0, 0, 0, 2, 0, 0, 0, 6],
                [0, 6, 0, 0, 0, 0, 2, 8, 0],
                [0, 0, 0, 4, 1, 9, 0, 0, 5],
                [0, 0, 0, 0, 8, 0, 0, 7, 9],
            ]
        ),
        "medium": Sudoku(
            [
                [3, 0, 0, 0, 4, 0, 0, 7, 0],
                [0, 0, 6, 0, 2, 0, 0, 0, 0],
                [5, 0, 0, 7, 0, 6, 0, 0, 9],
                [0, 0, 5, 3, 0, 1, 0, 2, 0],
                [0, 0, 0, 0, 6, 0, 0, 0, 0],
                [9, 0, 0, 0, 0, 0, 8, 0, 0],
                [0, 3, 0, 0, 0, 0, 0, 0, 2],
                [0, 0, 0, 4, 0, 0, 0, 0, 0],
                [0, 0, 1, 5, 0, 7, 0, 3, 0],
            ]
        ),
        "hard": Sudoku(
            [
                [8, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 3, 6, 0, 0, 0, 0, 0],
                [0, 7, 0, 0, 9, 0, 2, 0, 0],
                [0, 5, 0, 0, 0, 7, 0, 0, 0],
                [0, 0, 0, 0, 4, 5, 7, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 3, 0],
                [0, 0, 1, 0, 0, 0, 0, 6, 8],
                [0, 0, 8, 5, 0, 0, 0, 1, 0],
                [0, 9, 0, 0, 0, 0, 4, 0, 0],
            ]
        ),
    }

    difficulty: Literal["easy", "medium", "hard"] = "medium"

    print(f"Solving a Sudoku with {difficulty} difficulty!\n")
    start_time = time.time()
    solutions = backtrack([sudokus[difficulty]])
    end_time = time.time()
    print(f"Elapsed time: {end_time - start_time:.2f} seconds\n")

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
