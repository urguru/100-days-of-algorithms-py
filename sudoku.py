def print_board(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j],end=' ')
        print('',end='\n')
        
def find_empty_cell(board,l):
    for r in range(9):
        for c in range(9):
            if board[r][c]==0:
                l[0]=r
                l[1]=c
                return True
    return False

def solve_sudoku(board):
    l=[0,0]
    if not find_empty_cell(board,l):
        return True
    else:
        for i in range(1,10):
            if fits_into_board(board,l,i):
                board[l[0]][l[1]]=i
                if solve_sudoku(board):
                    return True
                board[l[0]][l[1]]=0
        return False
        
def fits_into_board(board,l,i):
    return fits_into_column(board,l[1],i) and fits_into_row(board,l[0],i) and fits_into_box(board,l,i)

def fits_into_row(board,r,i):
    for x in range(9):
        if board[r][x]==i:
            return False
    return True

def fits_into_column(board,c,i):
    for x in range(9):
        if board[x][c]==i:
            return False
    return True

def fits_into_box(board,l,i):
    r=l[0]//3
    c=l[1]//3
    for x in range(r*3,r*3+3):
        for y in range(c*3,c*3+3):
            if board[x][y]==i:
                return False
    return True


board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

if(solve_sudoku(board)):
    print_board(board)
else:
    print('Cannot Solve the Sudoku')

