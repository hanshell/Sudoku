from math import floor
filename='//home//melbster//Desktop//sudokuboard.txt'
def initialize_board(n):
    return [[0 for i in range(n)]for j in range(n)]
def setBoard():
    f=open(filename, 'r')
    BOARD_DIMENSIONS=9
    matrix=initialize_board(BOARD_DIMENSIONS)
    for i in f.readlines():
        rowCol=i.strip()
        tupleList=rowCol.split(',')
        y=int(tupleList[0])
        x=int(tupleList[1])
        value=int(tupleList[2])
        matrix[y][x]=value
    return matrix
matrix=setBoard()
def setPosition(y,x,value):
    matrix[y-1][x-1]=value
    return matrix
def validRow(y, x, value):
    for i in matrix[y-1]:
        if(i==value):
            return False
    return True
def validColumn(y, x, value):
    for i in range(1, len(matrix)+1):
        if(matrix[i-1][x-1]==value):
            return False
    return True
def validGrid(y, x, value):
    y-=1
    x-=1
    upperY=(floor(y/3)+1)*3
    upperX=(floor(x/3)+1)*3
    lowerY=upperY-3
    lowerX=upperX-3
    for i in range(lowerY, upperY):
        for j in range(lowerX, upperX):
            if(matrix[i][j]==value):
                return False
    return True
def is_Empty(y,x):
    return matrix[y-1][x-1]==0
def valid_Placement(y,x, cell):
    print_matrix()
    if(validRow(y, x, cell)):
        if(validColumn(y, x, cell)):
            if(validGrid(y, x, cell)):
                if(is_Empty(y, x)):
                    return True
    return False
def set_pos(y,x,cell):
    if(valid_Placement(y, x, cell)):
        matrix[y-1][x-1]=cell
        print('Valid placement!')
    else:
        print('Invalid placement! Try again')
    return matrix
def input_prompt():
    while(True):
        print_matrix()
        Ypos=input('Enter row number ')
        if(exit_input(Ypos)or (int(Ypos)<1 or int(Ypos)>9)):
            exit_message()
            break
        Xpos=input('Enter column number ')
        if(exit_input(Xpos)or (int(Xpos)<1 or int(Xpos)>9)):
            exit_message()
            break
        cell=input('Enter value ')
        if(exit_input(cell) or (int(cell)<1 or int(cell)>9)):
            exit_message()
            break
        set_pos(int(Ypos),int(Xpos),int(cell))
        if(victory()):
            print('Congratulations! Board solved')
            break
def exit_message():
    print('\nGame ended\n')
    print_matrix()
def exit_input(s):
    e='exit'
    if(s.lower()==e):
        return True
    return False
def print_matrix():
    for item in matrix:
        print (item)
def victory():
    for i in range(len(matrix)):
        for j in matrix[i]:
            if(matrix[i][j]==0):
                return False
    return True
def main():
    input_prompt()
main()