import copy
from collections import Counter
POSITIONS = {
    0:[(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)],
    1:[(3, 0), (4, 0), (5, 0), (3, 1), (4, 1), (5, 1), (3, 2), (4, 2), (5, 2)],
    2:[(6, 0), (7, 0), (8, 0), (6, 1), (7, 1), (8, 1), (6, 2), (7, 2), (8, 2)],
    3:[(0, 3), (1, 3), (2, 3), (0, 4), (1, 4), (2, 4), (0, 5), (1, 5), (2, 5)],
    4:[(3, 3), (4, 3), (5, 3), (3, 4), (4, 4), (5, 4), (3, 5), (4, 5), (5, 5)],
    5:[(6, 3), (7, 3), (8, 3), (6, 4), (7, 4), (8, 4), (6, 5), (7, 5), (8, 5)],
    6:[(0, 6), (1, 6), (2, 6), (0, 7), (1, 7), (2, 7), (0, 8), (1, 8), (2, 8)],
    7:[(3, 6), (4, 6), (5, 6), (3, 7), (4, 7), (5, 7), (3, 8), (4, 8), (5, 8)],
    8:[(6, 6), (7, 6), (8, 6), (6, 7), (7, 7), (8, 7), (6, 8), (7, 8), (8, 8)]
}
EMPTY = "."

class Sudoku:  
    def __init__(self, grid):
        if not grid:
            self.create_new_game()
        else:
            self._grid = grid
        self._count = None
    
    def __str__(self):
        s = ""
        for row in self._grid:
            s += " ".join(row)  + "\n"
        return s
    
    def clone(self):
        return Sudoku(grid=self._grid)
    
    def create_new_game(self):
        self._grid = []

    def find_empty_cells(self):
        return [(row, col, self.find_3by3(row, col)) for row in range(9) for col in range(9) if self._grid[row][col] == EMPTY]

    def find_possible_numbers(self, row, col):
        if self._grid[row][col]:
            return None  
        possible_numbers = []      
        for num in range(1, 10):
            if self.check_number(num, row, col):
                possible_numbers.append(num)
        return possible_numbers

    def check_number(self, num, row, col):
        return self.check_number_in_row( num, row) and self.check_number_in_col(num, col) and self.check_number_in_3by3(num, row, col)
            
    def check_number_in_row(self, num, row):
        return num not in self._grid[row]

    def check_number_in_col(self, num, col):
        return num not in [self._grid[r][col] for r in range(0, 9)]

    def check_number_in_3by3(self, num, row, col):
        nums = [self._grid[r][c] for r, c in POSITIONS[self.find_3by3(row, col)]]
        return num not in set(nums)

    def check(self, values):
        return len(set(values)) == 9

    def find_3by3(self, row, col):
        if row < 3:
            if col < 3: 
                return 0
            elif col > 5:
                return 6
            else:
                return 3
        elif row > 5:
            if col < 3: 
                return 2
            elif col > 5:
                return 8
            else:
                return 5
        else:
            if col < 3: 
                return 1
            elif col > 5:
                return 7
            else:
                return 4

    def find_order(self):
        c = Counter([i for row in self._grid for i in row if i != EMPTY])
        print(c)
        self._count = sorted(c.items(), key=lambda x: x[1], reverse=True)
        
        
    def get_count(self):
        return self._count

    def get_number_positions(self, number):
        return self._number_dictionary[number]
    
    def get_empty_cells(self):
        return self._empty_cells

    def place_number(self, num, row, col):
        self._grid[row][col] = num

    def check_solve(self):
        if not len(self.find_empty_cells()) == 0:
            return False
        return True
        

def brute_force(board):

    empty_cells = board.find_empty_cells(board)
    while empty_cells:
        row, col = empty_cells.pop(0)
        possible_numbers = board.find_possible_numbers(board, row, col)
        if not possible_numbers:
            return board, False
        if len(possible_numbers) == 1:
            board.place_number(board, possible_numbers[0], row, col)
        else:
            clone = copy.deepcopy(board)
            print(clone)
            for number in possible_numbers:
                board.place_number(clone, number, row, col)
                clone, state = brute_force(clone)   
                if state:
                    board = clone
                    empty_cells = []
                    break
    return board, True

x = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

y = Sudoku(x)
print(y)
y.find_order()
while not y.check_solve():
    for number, dummy in y._count:

        # print(y.get_number_positions(number))
        # print(y.get_empty_cells())
        # print(y.get_count())

        r= {}
        c= {}
        t= {}
        p = y.find_empty_cells()
        for row,col, threebythree in p:
            if y.check_number(number,row,col):
                for a, d in [[row, r],[col,c],[threebythree,t]]:
                    if a not in d:
                        d[a] = []
                    d[a].append((row,col,threebythree))
        print(r)
        print(c)
        print(t)
        for d in [r, c, t]:
            for key, value in d.items():
                if len(value) == 1:
                    print(value)
                    y.place_number(number, value[0][0], value[0][1])
            print(y)

