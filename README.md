# Sudoku Solver

Solves Sudoku puzzles using a **width search** (breadth-first) algorithm. Given a board with empty cells (represented as `0`), it explores all valid number placements level by level until a solution is found.

## How it works

At each step, the algorithm:
1. Finds the first empty cell on the board.
2. Tries every number from 1 to 9, skipping those that violate Sudoku rules (duplicate in row, column, or 3×3 square).
3. For each valid number, creates a new board with that number placed and recurses.
4. Returns all boards where every cell is correctly filled.

## Sequence diagram

```mermaid
sequenceDiagram
    participant C as Caller
    participant WS as width_search()
    participant GEN as _generate_all_new_sudokus()
    participant S as Sudoku

    C->>WS: width_search([initial_sudoku])

    loop until all cells filled
        alt sudokus is empty
            WS-->>C: [] (no solution)
        end

        WS->>S: _find_first_empty_cell(sudokus[0])
        S-->>WS: (coord_x, coord_y)

        WS->>GEN: _generate_all_new_sudokus(sudokus, coord_x, coord_y)
        loop for each sudoku × each num 1..9
            GEN->>S: possible_move(coord_x, coord_y, num)
            S-->>GEN: True / False
            alt move is valid
                GEN->>S: Sudoku(deepcopy(board))
                GEN->>S: add_number(coord_x, coord_y, num)
                GEN->>GEN: append new sudoku
            end
        end
        GEN-->>WS: new_sudokus

        WS->>WS: count remaining empty cells
        WS->>WS: _print_progress(new_sudokus, n_cells_left)

        alt cells left == 0
            loop for each sudoku in new_sudokus
                WS->>S: win()
                S-->>WS: True / False
            end
            WS-->>C: [solutions]
        else cells left > 0
            WS->>WS: width_search(new_sudokus)
        end
    end
```

## Project structure

```
src/
├── sudoku.py       # Sudoku class: board representation and validation logic
├── width_search.py # Width search (breadth-first) algorithm
└── examples.py     # Ready-to-run examples (easy, medium, hard)
```

## Usage

Run the example script:

```bash
uv run python -m src.examples
```

To change the difficulty, edit the `difficulty` variable in `src/examples.py`:

```python
difficulty: Literal["easy", "medium", "hard"] = "easy"
```

Note that you can also include your own Sudokus!
