"""
Driver: Maksym Kalinin/ Aline Hirsch
Navigator: 
Assignment: Template INST326
Date: 12_02_22

Challenges Encountered: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

import re
import sys
import argparse

def parse_name(text:str):
    """
    This function will contain one parameter, text, a string representing a single line of the file.
    This function should use regular expressions in order to capture the first name and the last name of the person in question
    This function will return a tuple containing the first and the last names as strings
    """
    first_name = ""
    last_name = ""
    return (first_name, last_name)
    
def parse_address(text:str):
    """
    This function will contain one parameter, text, a string representing a single line of the file
    This function should use regular expressions in order to capture the street, city and state of person in question
    This function will create and return an address object using the street, city and state identified.
    """
    street = ""
    city = ""
    state = ""

    address = (street, city, state)
    return address

def parse_email(text:str):
    """
    This function will contain one parameter, text, a string representing a single line of the file
    This function should use regular expressions in order to capture the email of the person in question
    This function will return the email identified.
    """
    email= ""
    return email
    
class Address(street, city, state):
    """
    This class will have three attributes (street, city, state) that are created from the arguments that are passed in when an instance
    of address is created
    This class will not have any methods
    """
    pass

class Employee(first_name, last_name, address, email):
    """
    ◦ This class will have 4 attributes (first_name, last_name, address, email).
        ▪ These attributes will all be created by passing in a row of the file when an instance of
        employee is created. This meaning, the init method will only have one parameter other than self.
        ▪ The first_name and last_name attributes are created by calling the parse_name function
        and passing in the parameter of the init method of employee as an argument in the parse_name function call.
        ▪ The address attribute is created by calling the parse_address function and passing in the
        parameter of the init method of employee as an argument in the parse_address function call.
        ▪ The email attribute is created by calling the parse_email function and passing in the
        parameter of the init method of employee as an argument in the parse_email function call.
    ◦ This class will not have any methods.
    """
    def __init__(parameter1, self):
        pass
    pass
    
    
def main(path):
    """
    Write a main function. Your main should have one parameter, path, which is the path to the file
    that is being parsed.
        ◦ Create an empty list called employee_list.
        ◦ Open up the file from the path.
    ▪ For each line in the file, create an instance of employee by passing in the string which is
    the line of the file that you are reading.
    ▪ Append this instance to the employee_list.
    ▪ Within the main, return the employee_list
    """
    employee_list = []
    
    pass

def parse_args(args_list):
    """Takes a list of strings from the command prompt and passes them through as arguments
    
    Args:
        args_list (list) : the list of strings from the command prompt
    Returns:
        args (ArgumentParser)
    """
    
    #For the sake of readability it is important to insert comments all throughout.
    #Complicated operations get a few lines of comments before the operations commence. 
    #Non-obvious ones get comments at the end of the line.
    #For example:
    #This function uses the argparse module in order to parse command line arguments.
    
    parser = argparse.ArgumentParser() #Create an ArgumentParser object.
    
    #Then we will add arguments to this parser object.
    #In this case, we have a required positional argument.
    #Followed by an optional keyword argument which contains a default value.
    
    parser.add_argument('required', type=float, help='This is an example of a required argument.')
    parser.add_argument('--optional', '-o', type=int, default=12, help='This is an example of an optional argument')  
    
    args = parser.parse_args(args_list) #We need to parse the list of command line arguments using this object.

    return args

if __name__ == "__main__":
    #If name == main statements are statements that basically ask:
    #Is the current script being run natively or as a module?
    #It the script is being run as a module, the block of code under this will not be executed.
    #If the script is being run natively, the block of code below this will be executed.
    
    arguments = parse_args(sys.argv[1:]) #Pass in the list of command line arguments to the parse_args function.
    
    #The returned object is an object with those command line arguments as attributes of an object.
    #We will pass both of these arguments into the main function.
    #Note that you do not need a main function, but you might find it helpfull.
    #You do want to make sure to have minimal code under the 'if __name__ == "__main__":' statement.
    
    main(arguments.required, arguments.optional)

