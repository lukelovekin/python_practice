# calculator
import operator


def calculator():
    num1 = input("Enter your first number (in digits):")
    operator = input("Now enter an operator (*, +, -, /):")
    num2 = input("And lastly, enter another number (in digits):")
    
    nums = check_nums(num1, num2)
    oper = check_operator(operator)

    if (nums and oper):
        result = operators[oper](int(num1),int(num2))
        print(result)
        return result
        
   
def check_nums(num1, num2):
    if (num1 + num2).isdigit():
        return True
    else:
        print("2 numbers not entered")
        return False

    # attempt at python ternary
    # return True if (num1 + num2).isdigit() else False
    

def check_operator(operator):
    if operator in ("*", "/", "+", "-"):
        return operator
    else:
        print("an operator was not picked")
        return False

    # attempt at python ternary
    # return True if operator != ("*" or "/" or "+" or "-") else False


operators = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv
    }

calculator()


# papper scissors rock

# hangman