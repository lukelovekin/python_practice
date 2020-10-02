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