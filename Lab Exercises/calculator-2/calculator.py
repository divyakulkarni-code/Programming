"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

def mathematical_functions():
    while True:
        user_input = input('Enter your equation > ')

        user_input = user_input.split(' ') # user input
        # If user wants to quit don't process anything

        if 'q' in user_input:
            print('Exiting out of the program')
            break 
        
        nums_list = []

        operator, *nums = user_input
        

        try:
            for num in nums:
                nums_list.append(float(num))
        except ValueError:
            print("One of your operand was not a number")
            continue
        if (operator not in ('square', 'cube') and len(nums) < 2):
            print("Error! not valid input")
        
        operate(operator, nums_list)
        
def operate(operator,nums_list):
    equation = None
    if operator == '+':
        equation = add(nums_list[0], nums_list[1])

    elif operator == '-':
        equation = subtract(nums_list[1], nums_list[2])

    elif operator == '*':
        equation = multiply(nums_list[0], nums_list[1])

    elif operator == '/':
        equation = divide(nums_list[0], nums_list[1])

    elif operator == 'square':
        equation = square(nums_list[0])
    
    elif operator == 'cube':
        equation = cube(nums_list[1])

    elif operator == 'mod':
        equation = mod(nums_list[0], nums_list[1])
        
    print("result is {}".format(equation))        

print(mathematical_functions())








 




