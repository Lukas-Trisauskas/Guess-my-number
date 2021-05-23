# -*- coding: utf-8 -*-
# pylint: disable=unbalanced-tuple-unpacking
# ==========================================
# Created by: Lukas Trisauskas (25480454)
# Description: Programming Fundamentals Assesment 1

import random

def sch_register():
    
    email_generated = False
    while not email_generated:
        # Create a new variable store the email
        email = ""
        valid_name = False
        while not valid_name:
            contains_digit = False
            # Catch any errors that happen inside the try:
            try:
                # Ask the user to enter their full name
                full_name = input("> Please enter your full name: ")
                # Loops over full_name and checks whether it contains any digits, assigns has_digit to True
                # which sets off False condition below and executes the next part of the code.
                for i in full_name:
                    if i.isdigit():
                        contains_digit = True
                        raise ValueError
                if full_name == "":
                    raise TypeError
                elif not contains_digit:           
                    # Seperate first and last name using split function
                    # Assign the result to new variable
                    split_name = full_name.split()
                    # Print the first name by call element [0] of the list split_name
                    print("> Hello " + split_name[0])
                    # This breaks the loop if full_name has been successfully validated
                    valid_name = True
                    break
            # Handle the try error. by printing a custom error message for,
            # when an invalid data type is entered.
            except ValueError:
                print("> Console: You've entered an invalid character!:", full_name)
            except TypeError:
                print("> Console: Can't be left empty!")
            
        valid_age = False
        while not valid_age:
            # Catch any errors that happen inside the try:
            try:
                # Ask the user to enter their age
                age = input("> Please enter your age: ")
                # Check if the input contains any letters
                for i in age:
                    if i.isalpha():
                        raise ValueError
                    else:
                        age = int(age)
                # Check if the age_converted is less than the min age 11
                if age < 11:
                    print("> Sorry, you are too young to be registered at this school.")
                    valid_age = False
                    break
                # Check if the age_converted is greater than the max age 18
                elif age > 18:
                    print("> Sorry, you are too old to be registered at this school.")
                    valid_age = False
                    break
                # Check if the age is between the min 11 and max 18 age
                elif age >= 11 and age <= 18:
                    # Ask the user to enter their date of birth. 
                    date_of_birth = input("# Please enter your date of birth, in (dd/mm/yyy) format: " )
                    print("> Thank you.")
                    valid_age = True
                    break
            # Handle the try error. by printing a custom error message for,
            # when an invalid data type is entered.
            except ValueError:
                print("> Console: You've entered an invalid character!:", age)
            except TypeError:
                print("> Console: Can't be left empty!")
                
        if valid_name and valid_age:
            # Extracts the year from date_of_birth using split function,
            # and assign the result to a new variable birth_year.
            # Print the birth year by indexing the second element inside birth_year.
            birth_year = date_of_birth.split("/")
            print("> You were born in the year " + birth_year[2])
        
            # Extracts first letter of their first and last name
            # Loops over each element inside split_name and assigns the first letter,
            # of the first name and last name, to student_initials.
            student_initials = ""
            for i in split_name:
                student_initials += i[0][0]
        
            # Generate a random two digit number, ranging from 10, 99.
            # Assign random to random_number.
            random_number = str(random.randint(10, 99))
            school_domain = '@school.ac.uk'

            # Generating an email by combining and,
            # assign student_initials, birth_year, random_numbe and school_domain to email variable.
            email = student_initials + birth_year[2] + random_number + school_domain
            email_generated = True
        else:
            exit()
    # Return the variable email
    return email

def pwd_validate(pwd):

    instructions = """
    [!] Your password must be 12 characters long.
    [!] It must contain at least 1 symbol: ($ % & * + @)
    [!] And is composed of numbers, lowercase and uppercase letters.
    """
    symbols = ['!','"','#','$','%','&','(',')','*','+','-','.','/',':',';','<',
    '=','>','?','@','[',']','^','_','`','{','|','}','~',"\\",'£']

    # Set to True when password has been successfully validated to break the loop
    password_valid = False
    
    while not password_valid:
        
        # Password states is set to False by default
        lenght = False
        symbol = False
        number = False 
        uppers = False
        lowers = False
        
        # For testing purposes, to see what is being inputted
        """
        i_symbol = []
        i_number = []
        i_uppers = []
        i_lowers = []
        """
        
        # Check if password lenght is equal to 12, set lenght to True if condition is True.
        pwd_lenght = len(pwd)
        if pwd_lenght == 12:
            lenght = True
        else:
            lenght = False
            
        # Loops over each character inside pwd and assign it to i
        # Checks if the password contains symbols, numbers, uppercase and lowercase letters
        # Set each variable to True if condition is True
        for i in pwd:
            if i in symbols:
                symbol = True
                #i_symbol.append(i)
            elif i.isdigit(): 
                #i_number.append(i)
                number = True
            elif i.isupper():
                #i_uppers.append(i)
                uppers = True
            elif i.islower(): 
                #i_lowers.append(i)
                lowers = True
                
        # If all password states are True, set password_valid to True to break the whileloop
        # Ask the user to re-enter the password if one or more variables are False
        if lenght and symbol and number and uppers and lowers:
            password_valid = True
            break
        else:
            password_valid = False
            print("The password you entered is not strong enough.")
            print("You've entered: ", pwd)
            print(instructions)
            
            # For testing purposes, to see what is being inputted
            """
            print(" lenght:", len(pwd), lenght)
            print(" symbol:", i_symbol, symbol)
            print(" number:", i_number, number)
            print(" uppers:", i_uppers, uppers)
            print(" lowers:", i_lowers, lowers)
            """

            # Ask user to re-enter the password again, until it's strong enough.
            pwd = input("\nPlease enter your password again: ")
            
            
    # For testing purposes, to see what is being inputted 
    """
    print(" lenght:", len(pwd))
    print(" symbol:", i_symbol)
    print(" number:", i_number)
    print(" uppers:", i_uppers)
    print(" lowers:", i_lowers)
    """

    # Check if the whileloop condition has been set - 
    # to True and return the new password.
    if password_valid:
        print("\n")
        return " Your new password is: " + pwd 

# Program main --- Do not change the code below but feel free to comment out 
# sections of code when working on individual functions. 
# Calling Task 1 function
email = sch_register()
print("Your new school email is: ", email)

#Calling Task 2 function
pwd = input("\nPlease enter your new password, it should be 12 characters long: ")
print("Your new password is: ")  
print(pwd_validate(pwd))
