#cells = str(input("Enter cells: "))
cells = "_________" # Starting Cell
turn = False # Check whose turn it is
win = False # Win condition
Xcol = False # Win for X on Columns
Ocol = False # Win for O on cColumns

# Make a list of list for the cells
board = [[i for i in range(3)] for j in range(3)]
print("---------")
k = 6
for i in range(3):

    for j in range(3):
        board[i][j] = cells[k]
        k += 1
    if k > 0:
        k -= 6
# Print the '_' Board
for i in range(2, -1, -1):
    print('|', end=" ")
    for j in range(3):
        print(board[i][j], end=" ")
    print('|')

print("---------")

#print([board[i][j] != '_' for i in range(3) for j in range(3)])

while (win == False): # Until win is True
    # If statement to check all the block for Draw
    if all([board[i][j] != '_' for i in range(3) for j in range(3)]) == True:
        print("Draw!")
        break
    # Import User's Move
    xcoord , ycoord = input("Enter the coordinates: ").split()
    # Use try to detect Integers, if not exception
    try:
        xcoord = int(xcoord)
        ycoord = int(ycoord)
    except:
        print("You should enter numbers!")
        continue
    # Check Range of Coordinates
    if xcoord < 1 or ycoord < 1 or xcoord > 3 or ycoord > 3:
        print("Coordinates should be from 1 to 3!")
        continue
    else:
        # Remove - 1 to do checks for my personally long checking rules
        xcoord -= 1
        ycoord -= 1
        # Occupied Cells ( Notice Y and X are reversed )
        if board[ycoord][xcoord] == 'X' or board[ycoord][xcoord] == 'O':
            print('This cell is occupied! Choose another one!')
            continue
        else:
            # Switch Turns by changing turn Variable
            if turn == False:
                board[ycoord][xcoord] = 'X'
                turn = True
            else:
                board[ycoord][xcoord] = 'O'
                turn = False

#Print Board
    print("---------")
    for i in range(2, -1, -1):
        print('|', end=" ")
        for j in range(3):
            print(board[i][j], end=" ")
        print('|')

    print("---------")
### Print End
    # Win Checks
    diagoX = 0 # For Diagos
    diagoO = 0
    for i in range(3):
            countX = 0
            countO = 0
            if board[i].count('X') == 3:
                print('X wins1')
                win = True
                break
            if board[i].count('O') == 3:
                print('O wins2')
                win = True
                break
                # count columns 3 in a row
            for j in range(3):
                if board[j][i] == "X":
                    countX += 1
                    if countX == 3:
                        Xcol = True
                if board[j][i] == "O":
                    countO += 1
                    if countO == 3:
                        Ocol = True
                if Xcol == True and Ocol == True:
                    print('Impossible')
                    break

            if board[i][i] == 'X': diagoX += 1
            if board[i][i] == 'O': diagoO += 1
            if diagoX == 3:
                print('X wins3')
                win = True
                break
            if diagoO == 3:
                print('O wins4')
                win = True
                break
            # Reverse Diagonals
            if board[0][2] == 'X' and board[2][0] == 'X' and board[1][1] == 'X':
                print('X wins5')
                win = True
                break
            if board[0][2] == 'O' and board[2][0] == 'O' and board[1][1] == 'O':
                print('O wins6')
                win = True
                break
            if Xcol == True:
                print('X wins7')
                win = True
                break
            if Ocol == True:
                print('O wins8')
                win = True
                break

# Check the impossible cases
# if cells.count('O') - cells.count('X') >= 2 \
#         or cells.count('X') - cells.count('O') >= 2:
#     print("Impossible")
#     exit()
#For loop to check 3 X's or O's in rows

# # Draw conditions
# #if cells.count('_') > 0 or cells.count(' ') > 0:
# #    print("Game not finished")
# #else:
#     print("Draw")


#### Win Conditions

