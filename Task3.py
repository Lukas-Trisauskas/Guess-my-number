
# -*- coding: utf-8 -*-
# pylint: disable=unbalanced-tuple-unpacking
# ==========================================
# Created by: Lukas Trisauskas (25480454)
# Description: Programming Fundamentals Assesment 1

import random # This is the only module you can import for this task

def guess_my_number():
    
    instructions = """
    +-----------------------------------------------------+
    | ** Instructions                                     |
    +-----------------------------------------------------+
    | 1. Think of any number.                             |
    | 2. Enter the range that your number is in eg. (1,10)|
    +-----------------------------------------------------+
    | ** Commands                                         |
    +-----------------------------------------------------+
    | $ If my guess is too low enter:  [toolow  ]         |
    | $ If my guess is too high enter: [toohigh ]         |
    | $ If my guess is right enter:    [mynumber]         |
    +-----------------------------------------------------+
    """
    print(instructions)
    
    # Set range_valid to True to break the loop when range has been seuccessfully validated
    range_valid = False
    
    while not range_valid:
        
        # Ask the user to enter the range
        # Seperate start range and end range using split function
        user_input = str(input("> Tell me the range e.g (1,10) seperated by (,): ")).split(',')

        # Check if the lenght of user_input is minimum of 2 characters e.g 1,5
        # Loop over user_input and convert both ranges from string to integer
        if len(user_input) >= 2:
            extracted_range = []
            for i in user_input:
                extracted_range.append(int(i))
                
            # Assign the first element of the list "extracted_range" to start_range,
            # and second element of the list to end_range
            start_range, end_range = extracted_range
            
            # Create a list of numbers based on the given range e.g 4,7 = [4,5,6,7]
            user_range = list(range(start_range, end_range + 1))
            
            # Check if the range is not equal to 0 or the same e.g 0,1 or 1,1
            if start_range == 0 or end_range == 0 or start_range == end_range:
                print("$ The start and end range can't be zero or the the same")
            elif start_range > end_range:
                print("$ You must enter a valid range eg. (1,10)")
            else:
                range_valid = True
                break
        elif len(user_input) <= 1:
            print("$ You must enter a valid range eg. (1,10)")
            
    user_commands = ["toolow","toohigh","mynumber"] 
    
    # Set my_number to True to break the loop when correct guess has been made
    my_number = False
    # Counts the amount of guesses that have been made
    guess_counter = 0
    
    while not my_number:
        
        # Take the list of numbers and find the middle number (median)
        median_number = int(sum(user_range) / len(user_range))
        print(user_range)
        # If the list lenght is equal to 1 it will automatically guesses,
        # your number without asking you to enter "mynumber".
        if len(user_range) == 1:
            print("$ Your number is: ", median_number)
            print("")
            print("$ It took me", guess_counter, "guess(es) to find your number.")
            # Breaks the whileloop if the guess is correct
            my_number = True
        else:
            # If above condition is false, print the middle number,
            # of the list and continue checking.
            print("$ Is this your number: ", median_number)
            
            # Ask the user to enter one of the commands.
            # The input will only accept one of the three commands, otherwise 
            # it will print an error message.
            user_answer = input("> Enter, toolow, toohigh or mynumber: ")
            if not user_answer in user_commands:
                print("$ You must enter one of the following commands: [toolow], [toohigh], [mynumber]")
            # It will prevent the user from trying enter toohigh if the lenght of the list is 2
            elif len(user_range) == 2 and user_answer == "toohigh": 
                print("")
                print("You can't use command [toohigh] at this stage, enter [mynumber], [toolow]")
                print("")
            else:
                # Finds the index of the middle number and deletes either right or left portion of the 
                # list based on the command user enters, starting from the index of the middle number.
                # Adds (+1) to guess_counter everytime a wrong guess has been made.
                if user_answer == "toohigh":
                    range_index = user_range.index(median_number)
                    del user_range[range_index:]
                    guess_counter += 1
                elif user_answer == "toolow":
                    # (median_number + 1) so that it removes the previous middle number.
                    range_index = user_range.index(median_number + 1)
                    del user_range[:range_index]
                    guess_counter += 1
                # my_number will be set to True which will stop the whileloop if the correct guess has been made.
                elif user_answer == "mynumber":
                    my_number = True
                    print("")
                    # This will print the amount of guesses it took.
                    print("> It took me", guess_counter, "guess(es) to find your number.")
                    break
    # Keeps checking if the whileloop condition has been set to True.
    if my_number:
        commands = ["yes", "Yes", "No", "no"]
        # Loops until one of the conditions below are True.
        while True:
            # Ask the user if they want to play again.
            restart_game = input("> Would you like to play again?: ")
            # Check if the input is not alphabetical characters
            if not restart_game.isalpha():
                print("$ You must enter Yes or No!")
            # Checks which command the user entered
            # [2:4] = No/no and [0:2] = Yes/yes
            elif restart_game in commands[2:4]:
                print("Thank you for playing. Goodbye")
                exit() # Exists the game if the user enters No
            elif restart_game in commands[0:2]:
                guess_my_number() # Restarts the game if the user enters Yes.
                
#Program main -- Do not change code below
guess_my_number()
