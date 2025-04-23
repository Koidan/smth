from random import randint

history_random = []
history_calculate = []

def main():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    while True:
        try:
            request = int(input("What do u want? \nCalculate - 1 \nHistory - 2 \nRandom - 3 \nBattleship - 4 \nExit - 5 \n>>> "))
        except ValueError:
            print("Write correct operation")
            continue
        if request == 1:
            calculator()
        elif request == 2:
            history()
        elif request == 3:
            randomizer()
        elif request == 4:
            battle()
            break
        elif request == 5:
            print("Existing, bye")
            break
        else:
            print(f"I have no idea, what do u mean by {request}, sorry")

def calculator():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    while True:
        try:
            x = int(input("Write the first number: "))
            y = int(input("Write the second number: "))
        except ValueError:
            print("Please enter valid numbers")
            continue 
        option = input("Choose the option \n(+, -, *. /)(x - Exit) \n>>>")
        if option == "+":
            z = x + y
            history_calculate.append(z)
            print(f"{x} + {y} = {z}")
            main()
        elif option == "-":
            z = x - y
            history_calculate.append(z)
            print(f"{x} - {y} = {z}")
            main()
        elif option == "*":
            z = x * y
            history_calculate.append(z)
            print(f"{x} * {y} = {z}")
            main()
        elif option == "/":
            z = x / y
            history_calculate.append(z)
            print(f"{x} / {y} = {z}")
            main()
        elif option.lower() == "x":
            print("Bye bye")
            break

def history():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"History of calculate numbers: \n{history_calculate} \nHistory of random numbers: \n{history_random}")
    action = int(input("What's next? \nClear - 1 \nCalculate - 2 \nRandom - 3 \nBattleship - 4 \nExit - 5\n >>>"))
    if action == 1:
        clear = int(input("Clear all - 1 \nClear history of calculate numbers - 2 \nClear History of random numbers - 3 \n>>>"))
        if clear == 1:
            history_calculate.clear()
            history_random.clear()
            print("Done!")
            history()
        elif clear == 2:
            history_calculate.clear()
            print("Done!")
            history()
        elif clear == 3:
            history_random.clear()
            print("Done!")
            history()
    elif action == 2:
        calculator()
    elif action == 3:
        randomizer()
    elif action == 4:
        battle()
    elif action == 5:
        print("Bye bye")

def randomizer():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("You have to write a minimal n maximal number: ")
    min = int(input("Write a minimal number \n>>>"))
    max = int(input("Write a maximal number \n>>>"))
    print(randint(min, max))
    action = int(input("What's next? \nCalculate -1 \nHistory - 2 \nBattleship - 3 \nExit - 4 \n>>> "))
    if action == 1:
        calculator()
    elif action == 2:
        history()
    elif action == 3:
        battle()
    elif action == 4:
        print("Bye bye")
    else:
        print("idk")

def battle():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    board = []
    for x in range(0, 5):
        board.append(["O"] * 5)

    def print_board(board):
        for row in board:
            print(" ".join(row))

    print_board(board)
    print("You have to guess where is my ship: row 0 - 4, col 0 - 4, you have 3 attempts.")
    def random_row(board):
        return randint(0, len(board) - 1)
    random_row(board)
    def random_col(board):
        return randint(0, len(board[0]) - 1)

    ship_row = random_row(board)
    ship_col = random_col(board)
    turn = 0
    for turn in range(4):
        if turn < 3:
            guess_row = int(input("Guess Row: "))
            guess_col = int(input("Guess Col: "))

            if guess_row == ship_row and guess_col == ship_col:
                print("Congratulations! You Sank my battleship!")
                break
            else:
                if guess_row not in range(5) or guess_col not in range(5):
                    print("Oops, that's not even in the ocean.")
                else:
                    print("You missed my battleship!")
                    board[guess_row][guess_col] = "X"
                    
                    print_board(board)
        else: 
            print("Game Over")         

if __name__ == "__main__":
    main()

