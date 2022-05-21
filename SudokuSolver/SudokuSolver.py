from tabulate import tabulate

class Solver:

    def __init__(self, board):
        self.board=board

    def solve(self):
        empty=self.find_empty()

        if not empty:
            return True

        i,j=empty[0],empty[1]     
        for num in range (1,10):
            if self.valid(num,i,j):
                self.board[empty[0]][empty[1]]=num
                
                if self.solve():
                    return True
                else:
                    self.board[empty[0]][empty[1]]=0
        return False
    
    def valid(self, num, i, j):
        for row in range(9):
            if self.board[row][j]==num:
                return False
        for col in range(9):
            if self.board[i][col]==num:
                return False

        grid_row=(i//3)*3
        grid_col=(j//3)*3

        for i in range(3):
            for j in range(3):
                if self.board[grid_row+i][grid_col+j]==num:
                    return False

        return True

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j]==0:
                    return [i,j]
        return False

    def show_board(self):
        print(tabulate(self.board, tablefmt='fancy_grid'))



s1=Solver([
    [0,0,2,0,0,0,0,0,0],
    [0,0,0,0,0,4,0,0,7],
    [1,3,0,0,8,0,0,5,0],
    [0,0,9,0,0,0,0,6,0],
    [6,2,0,0,0,8,4,0,0],
    [0,0,5,0,2,0,0,0,0],
    [8,6,0,0,3,0,0,1,0],
    [9,0,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,5,0,0],
    ])



s2= Solver([
    [6,0,0],
    [0,0,2],
    [0,0,0],
    ])

#while s1.find_empty()!=None:
   # s1.replc(s1.find_empty())

s1.show_board()
s1.solve()

s1.show_board()