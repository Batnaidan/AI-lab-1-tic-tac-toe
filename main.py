is_game_over = 0
user = 1
score = [[0, 0, 0],
        [0, 0, 0,],
        [0, 0, 0,]]

print("   1  2  3")
for count, row in enumerate(score):
    print(count+1, row)

def checkPattern():
    for row in range(3):
        if(score[row][0] == score[row][1] and score[row][1] == score[row][2] and not score[row][0] == 0):
            return True
    for col in range(3):
        if(score[0][col] == score[1][col] and score[1][col] == score[2][col] and not score[0][col] == 0):
            return True
    if(score[0][0] == score[1][1] and score[1][1] == score[2][2] and not score[0][0] == 0):
        return True
    elif(score[0][2] == score[1][1] and score[1][1] == score[2][0] and not score[0][0] == 0):
        return True
    else:
        return False

def checkInput(row_input, col_input):
    while not (row_input + 1 >= 1) or not (row_input + 1 <= 3):
        row_input = int(input("Enter row number: ")) - 1
    while not (col_input + 1 >= 1) or not (col_input + 1 <= 3):
        col_input = int(input("Enter column number: ")) - 1
    return [row_input, col_input]

while(is_game_over == 0):

    # while(score[col_input][row_input] == 0):
        # row_input = 4
        # col_input = 4
        # checkInput()

    while True:
        inputs = checkInput(4, 4)
        if score[inputs[0]][inputs[1]] == 0:
            break

    if user % 2 == 1:
        score[inputs[0]][inputs[1]] = 1
    else:
        score[inputs[0]][inputs[1]] = 2
    
    print("   1  2  3")
    for count, row in enumerate(score):
        print(count+1, row)
    if checkPattern():
        is_game_over = 1
        if user % 2 == 1:
            print("User 1 Has WON. Congratulations!!!")
        else:
            print("User 2 has WON. Congratulations!!!")
    else:
        user += 1