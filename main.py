# ========== CALCULATOR ==========
# import operator
# import randint


# def calculator():
#     num1 = input("Enter your first number (in digits):")
#     operator = input("Now enter an operator (*, +, -, /):")
#     num2 = input("And lastly, enter another number (in digits):")
    
#     nums = check_nums(num1, num2)
#     oper = check_operator(operator)

#     if (nums and oper):
#         result = operators[oper](int(num1),int(num2))
#         print(result)
#         return result
        
   
# def check_nums(num1, num2):
#     if (num1 + num2).isdigit():
#         return True
#     else:
#         print("2 numbers not entered")
#         return False

#     # return True if (num1 + num2).isdigit() else False
    

# def check_operator(operator):
#     if operator in ("*", "/", "+", "-"):
#         return operator
#     else:
#         print("an operator was not picked")
#         return False

#     # return operator if operator != ("*" or "/" or "+" or "-") else False


# operators = {
#     '+': operator.add,
#     '-': operator.sub,
#     '*': operator.mul,
#     '/': operator.truediv
#     }

# calculator()


# ========== PAPER SCISSORS ROCK ==========
# import random


# quickest/laziest way
# def paper_scissors_rock():
#     options = ["paper", "scissors", "rock"]
#     outcomes = ["You win", "You lose", "It's a Tie"]
#     player_input = input("Please enter, Paper, Scissors or Rock: ").lower()

#     if player_input not in options:
#         player_input = input("Incorrect input, please choose, Scissors, Paper or Rock")
#     else:
#         print(outcomes[random.randint(-1, 2)])

# # expected way
# def paper_scissors_rock():
#     options = ["paper", "scissors", "rock"]
#     player_input = input("Please enter, Paper, Scissors or Rock: ").lower()
#     computers_choice = options[random.randint(-1, 2)] 

#     if player_input not in options:
#         player_input = input("Incorrect input, please choose, Scissors, Paper or Rock")
    
#     if player_input == "rock":
#         if computers_choice == "rock":
#             print("It's a tie, Computer also chose Rock")
#         if computers_choice == "scissors":
#             print("You win!, Computer chose Scissors")
#         if computers_choice == "paper":
#             print("You lose!, Computer chose Paper")
#     elif player_input == "scissors":
#         if computers_choice == "rock":
#             print("You Lose!, Computer chose Rock")
#         if computers_choice == "scissors":
#             print("It's a tie, Computer also chose scissors")
#         if computers_choice == "paper":
#             print("You win!, Computer chose Paper")
#     elif player_input == "paper":
#         if computers_choice == "rock":
#             print("You Win!, Computer chose Rock")
#         if computers_choice == "scissors":
#             print("You Lose, Computer chose scissors")
#         if computers_choice == "paper":
#             print("Its a tie, computer also chose paper")

# paper_scissors_rock()    


# ========== HANGMAN ==========
import getpass


def hangman():
    print("Welcome to hangman")

    # Hangman picture
    hangman_pic = [
        ["       ____       "],  # [0]
        ["      |    |      "],  # [1]
        ["      | ", " O      "],  # [2][0] - [2][1]
        ["      |", " /", "|", "\     "],  # [3][0] - [3][3]
        ["      | ", "/", " \     "],  # [4][0] - [4][2]
        ["   ___|___        "],  # [5][0] - [5][3]
        ["                  "]  # [6][0]       
    ]

    # print hangman pic on welcome
    for pic in range(0, len(hangman_pic)):
        print(hangman_pic[pic][0])

    word = getpass.getpass("Pick a word for others to guess, (keep it a secret):  ")

    # check for one word only
    if len(word.split(" ")) > 1:
        word = getpass.getpass("Please try again, Pick \"One\" word for others to guess, (keep it a secret)")

    lst = list(word)
    empty = []
    
    # display empty letters
    for letter in lst:
        empty.append("_ ")
    
    print("".join(empty))

    guesses = 6

    # 6 wrong guesses will Lose
    while guesses > 0:
        letter = input("Choose one letter to guess the word :")

        if len(letter) > 1:
            letter = input("Choose ONE letter to guess the word :")
        
        if letter in lst:
            # show letter in the blanks and continue while loop
            break
        else:
            # show a picture from the hangman and add to numver of guesses
            print(f'Try again, {guesses} guesses left')
            guesses -= 1
            break



        if "_ " not in empty:
            print("Congratulations!")

    if guesses == 0:
        print('Game Over')
    # else:


hangman()