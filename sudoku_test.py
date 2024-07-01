import sudoku
grid = [
            [7, 8, 0, 4, 0, 0, 1, 2, 0],
            [6, 0, 0, 0, 7, 5, 0, 0, 9],
            [0, 0, 0, 6, 0, 1, 0, 7, 8],
            [0, 0, 7, 0, 4, 0, 2, 6, 0],
            [0, 0, 1, 0, 5, 0, 9, 3, 0],
            [9, 0, 4, 0, 6, 0, 0, 0, 5],
            [0, 7, 0, 3, 0, 0, 0, 1, 2],
            [1, 2, 0, 0, 0, 7, 4, 0, 0],
            [0, 4, 9, 2, 0, 6, 0, 0, 7]
        ]

answer = [
            [7, 8, 5, 4, 3, 9, 1, 2, 6],
            [6, 1, 2, 8, 7, 5, 3, 4, 9],
            [4, 9, 3, 6, 2, 1, 5, 7, 8],
            [8, 5, 7, 9, 4, 3, 2, 6, 1],
            [2, 6, 1, 7, 5, 8, 9, 3, 4],
            [9, 3, 4, 1, 6, 2, 7, 8, 5],
            [5, 7, 8, 3, 9, 4, 6, 1, 2],
            [1, 2, 6, 5, 8, 7, 4, 9, 3],
            [3, 4, 9, 2, 1, 6, 8, 5, 7]
        ]
def test_find_3by3_position():
    assert sudoku.find_3by3_positions(1, 1) == 0
    assert sudoku.find_3by3_positions(3, 1) == 1
    assert sudoku.find_3by3_positions(6, 2) == 2
    assert sudoku.find_3by3_positions(2, 5) == 3
    assert sudoku.find_3by3_positions(3, 3) == 4
    assert sudoku.find_3by3_positions(8, 5) == 5
    assert sudoku.find_3by3_positions(2, 8) == 6
    assert sudoku.find_3by3_positions(5, 8) == 7
    assert sudoku.find_3by3_positions(6, 6) == 8

def test_check_row():
    assert sudoku.check_row(grid, 3, 0, None)
    assert sudoku.check_row(grid, 1, 1, None)
    assert sudoku.check_row(grid, 8, 7, None)
    assert not sudoku.check_row(grid, 8, 0, None)
    assert not sudoku.check_row(grid, 6, 2, None)
    assert not sudoku.check_row(grid, 2, 8, None)

def test_check_col():
    assert sudoku.check_col(grid, 3, None, 0)
    assert sudoku.check_col(grid, 1, None, 1)
    assert sudoku.check_col(grid, 4, None, 8)
    assert not sudoku.check_col(grid, 1, None, 0)
    assert not sudoku.check_col(grid, 7, None, 2)
    assert not sudoku.check_col(grid, 7, None, 8)

def test_check_3by3():
    assert sudoku.check_3by3(grid, 1, 0, 0)
    assert sudoku.check_3by3(grid, 7, 3, 3)
    assert sudoku.check_3by3(grid, 1, 5, 8)
    assert not sudoku.check_3by3(grid, 8, 0, 0)
    assert not sudoku.check_3by3(grid, 6, 3, 3)
    assert not sudoku.check_3by3(grid, 5, 5, 8)

def test_find_possible_numbers():
    assert sudoku.find_possible_numbers(grid, 0, 2) == [3, 5]
    assert sudoku.find_possible_numbers(grid, 6, 6) == [5, 6, 8]
    assert sudoku.find_possible_numbers(grid, 5, 3) == [1, 7, 8]
    assert not sudoku.find_possible_numbers(grid, 0, 1)
    assert not sudoku.find_possible_numbers(grid, 5, 8)

def test_brute_force():
    print(grid)
    new_grid, solved = sudoku.brute_force(grid)
    if solved:
        assert new_grid == answer
    else:
        assert False, "Grid not Solved"
