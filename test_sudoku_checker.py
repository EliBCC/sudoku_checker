import pytest

from sudoku_checker import Solution

@pytest.fixture()
def solution():
    return Solution()

@pytest.mark.parametrize("valid_regions", [\
        ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
        [".", "2", ".", "4", "5", "6", "7", "8", "9"],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
    ])
def test_valid_regions(solution, valid_regions):
    assert solution.isValidRegion(valid_regions) == True

@pytest.mark.parametrize("invalid_regions", [\
        ["9", "2", "3", "4", "5", "6", "7", "8", "9"],
        [".", "2", ".", "4", "5", "6", "7", "8", "10"],
    ])
def test_invalid_regions(solution, invalid_regions):
    assert solution.isValidRegion(invalid_regions) == False

# Test valid sudoku board
def test_valid_sudoku(solution):
    board = \
        [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
    assert solution.isValidSudoku(board) == True

# Test invalid sudoku board
def test_invalid_sudoku(solution):
    board = \
        [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
    assert solution.isValidSudoku(board) == False

