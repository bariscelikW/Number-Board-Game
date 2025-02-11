import sys

def traverse(board, row, column):
    #if return true, continue
    # get value of given index
    val = board[row][column]
    #used queue for breadth first search, used 'all' for checking
    queue = []
    queue.append([row, column])
    all = []
    all.append([row, column])

    # while queue is not empty:
    while queue:
        # get first element of queue
        element = queue.pop()
        # downward direction
        try:
            if val == board[element[0] + 1][element[1]] and [element[0] + 1, element[1]] not in all and element[0] + 1 >= 0:
                all.append([element[0] + 1, element[1]])
                queue.append([element[0] + 1, element[1]])
        except:
            pass
        # upward direction
        try:
            if val == board[element[0] - 1][element[1]] and [element[0] - 1, element[1]] not in all and element[0] - 1 >= 0:
                queue.append([element[0] - 1, element[1]])
                all.append([element[0] - 1, element[1]])           
        except:
            pass
        # rightward direction
        try:
            if val == board[element[0]][element[1] + 1] and [element[0], element[1] + 1] not in all and element[1] + 1 >= 0:   
                queue.append([element[0], element[1] + 1])  
                all.append([element[0], element[1] + 1])                     
        except:
            pass
        # leftward direction
        try:
            if val == board[element[0]][element[1] - 1] and [element[0], element[1] - 1] not in all and element[1] - 1 >= 0:
                queue.append([element[0], element[1] - 1])
                all.append([element[0], element[1] - 1])
        except:
            pass
    #  duplicate number is length of all, and ctr times val equals to adding to score
    ctr = len(all)
    score = ctr * val
    
    # if lengt of all equals to 1, it means there is no duplicate
    if len(all) == 1:
        return 0
    else:
        # change same element by -1
        for index in all:
            board[index[0]][index[1]] = -1
        return score


def checker(board, row , column):
    #for checking if given row and column's length are convenient for our board
    try:
        if  0 <= row <= len(board) - 1 and 0 <= column <= len(board[row]) and board[row][column] != -1:
            return 1
        else: 
            return 0
    except:
        return 0
    

def move_down(board):
    # when encountered with -1(deleted item), carry them above the column
    is_continue = True
    while is_continue:
        is_continue = False
        for i in range(len(board) - 1):
            for j in range(len(board[i])):

                if board[i + 1][j] == -1 and board[i][j] != -1:
                    board[i + 1][j] = board[i][j]
                    board[i][j] = -1
                    is_continue = True
    return board


def row_del(board):
    # if a row's all elements consist of -1(deleted item), delete this row
    rows_to_delete = set()

    for i in range(len(board)):
        if all(cell == -1 for cell in board[i]):
            rows_to_delete.add(i)

    rows_to_delete = sorted(list(rows_to_delete), reverse=True)

    for row in rows_to_delete:
        board.pop(row)

    return board

        
def column_del(board):
    # if a column's all elements consist of -1(deleted item), delete this column
    length_of = len(board[0])  # Assuming all rows have the same length
    columns_to_delete = set()

    for calc in range(length_of):
        temp = 0
        for j in range(len(board)):
            if board[j][calc] == -1:
                temp += 1

        if temp == len(board):
            columns_to_delete.add(calc)

    columns_to_delete = sorted(list(columns_to_delete), reverse=True)

    for col in columns_to_delete:
        for row in board:
            row.pop(col)

    return board


def look_upward(board, rows, columns):
    # look given index's upward
    if rows != 0 and board[rows - 1][columns] == board[rows][columns]:
        return 1
    else:
        return 0

def look_downward(board, rows, columns):
    # look given index's downward
    if rows != len(board) - 1 and board[rows + 1][columns] == board[rows][columns]:
        return 1
    else:
        return 0

def look_leftward(board, rows, columns):
    # look given index's leftward
    if columns != 0 and board[rows][columns - 1] == board[rows][columns]:
        return 1
    else:
        return 0

def look_rightward(board, rows, columns):
    # look given index's rightward
    if columns != len(board[rows]) - 1 and board[rows][columns + 1] == board[rows][columns]:
        return 1
    else:
        return 0

def is_game_over(board):
    # if there is no possibility in given board return 0 and game over
    for rows in range(len(board)):
        for columns in range(len(board[rows])):
            if board[rows][columns] != -1 and (look_upward(board, rows, columns) or look_downward(board, rows, columns) or look_rightward(board, rows, columns)):
                return 1
    return 0

              
def play(board, total):
    # print initial board and score
    for r in board:
        print(*r)

    print()
    print(f'Your score is: {total}')
    print()
    
    # check is game over and if not:
    while is_game_over(board):
        try:
            # get row and column from user 
            row, column = map(int, input('Please enter a row and a column number: ').split())
            print()
            row -= 1
            column -= 1

            if checker(board, row, column):
                # make calculations here
                temp = traverse(board, row, column)
                if temp == 0:
                    print('No movement happened try again')
                    print('')

                else:
                    move_down(board)
                    column_del(board)
                    row_del(board)

                # print board
                for k in board:
                    for l in k:
                        if l != -1:
                            print(l, end=' ')
                        else: 
                            print(' ', end = ' ')
                    print()

                total += temp
                print('')
                print(f'Your score is : {total}')
                print('')

            else:
                print('Please enter a correct size!')
                print('')
        except:
            print('')
            print('Please enter a correct size!')
            print('')
    print('Game over')

def read_input_file():
    #read input file
    input_file = open(sys.argv[1], "r")
    board = input_file.readlines()
    board = [list(map(int, line.strip().split())) for line in board if line.strip()]
    
    input_file.close()
    return board

def main():
    
    #global variables
    total = 0
    board = read_input_file()
    play(board, total)
    
if __name__ == "__main__":
    main()