"""Script to define a Sudoku board."""

type Row = list[int]
type Board = list[Row]


class Sudoku:
    """Class to create a Sudoku board. 0 means an empty cell."""

    def __init__(self, board: Board) -> None:
        """Constructor of the class.

        Args:
            board: Initial board.
        """

        self.board = board
        self.n = len(board)

    def __str__(self) -> str:
        """Str method to print the board.

        Returns:
            board_string: String representation of the board.
        """

        board_string = ""

        for x in range(self.n):
            for y in range(self.n):
                board_string += "[ " + str(self.board[x][y]) + " ]"
            board_string += "\n"

        return board_string

    def add_number(self, x: int, y: int, number: int) -> None:
        """Adds a number to the sudoku.

        Args:
            x: X-coordinate where we introduce the number.
            y: Y-coordinate where we introduce the number.
            number: Number we introduce.
        """

        self.board[x][y] = number

    def _square_has_different_numbers(self, center_x: int, center_y: int) -> bool:
        """Checks that the current square has different numbers (0 is not taken into
        account, as it's an empty cell).

        Args:
            center_x: X coordinate of the center of the square.
            center_y: Y coordinate of the center of the square.

        Returns:
            True if the square has different numbers, False otherwise.
        """

        nums = []
        for xx in range(3):
            for yy in range(3):
                coord_x = center_x - 1 + xx
                coord_y = center_y - 1 + yy
                num = self.board[coord_x][coord_y]
                if num != 0:
                    nums.append(num)

        if len(set(nums)) < len(nums):
            return False

        return True

    def possible_move(self, x: int, y: int, num: int) -> bool:
        """Tells if a movement is possible.

        Args:
            x: X-coordinate of the cell we want to put the number.
            y: Y-coordinate of the cell we want to put the number.
            num: Number we want to put.

        Returns:
            True if the movement is possible, False otherwise.
        """

        # The number is not already in the same row or column
        for i in range(self.n):
            if num in [self.board[x][i], self.board[i][y]]:
                return False

        # The value 'num' was not previously 3x3 square with center (center_x, center_y)
        if x % 3 == 0:
            center_x = x + 1
        elif x % 3 == 1:
            center_x = x
        else:
            center_x = x - 1
        if y % 3 == 0:
            center_y = y + 1
        elif y % 3 == 1:
            center_y = y
        else:
            center_y = y - 1
        for xx in range(3):
            for yy in range(3):
                if self.board[center_x - 1 + xx][center_y - 1 + yy] == num:
                    return False
        # Check all numbers are different in the square.
        # Note: This is redundant because of the recursion and the way we are solving
        # the problem, but it may seem clearer.
        # if not self._square_has_different_numbers(center_x, center_y):
        #     return False

        return True

    def win(self) -> bool:
        """Tells if the game is finished.

        Returns:
            True if the game is finished, False otherwise.
        """

        # All rows and columns have 9 different numbers
        for i in range(self.n):
            row = [self.board[i][x] for x in range(self.n)]
            column = [self.board[x][i] for x in range(self.n)]
            zero_in_row = (0 in row) or (0 in column)
            not_enough_numbers = len(set(row)) < self.n or len(set(column)) < self.n
            if zero_in_row or not_enough_numbers:
                return False

        # Each square has 9 different numbers (there are 9 squares)
        for x in range(3):
            for y in range(3):
                center_x = 3 * x + 1
                center_y = 3 * y + 1
                if not self._square_has_different_numbers(center_x, center_y):
                    return False

        return True
