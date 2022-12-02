"""
Driver: Maksym Kalinin/ Aline Hirsch
Navigator: 
Assignment: INST326 Exercise 4
Date: 12_02_22

Challenges Encountered: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

import re
import sys
import argparse
## Do we need parser?
def parse_name(text:str):
    """
    This function will contain one parameter, text, a string representing a single line of the file.
    This function should use regular expressions in order to capture the first name and the last name of the person in question
    This function will return a tuple containing the first and the last names as strings
    """
    text = text.split(" ")
    text = [text[0],text[1]]    
    return tuple(text)
    
def parse_address(text:str):
    """
    This function will contain one parameter, text, a string representing a single line of the file
    This function should use regular expressions in order to capture the street, city and state of person in question
    This function will create and return an address object using the street, city and state identified.
    """
    
    text = text.split(" ")
    street = text[2:-3]
    street = " ".join(street)
    city = text[-3]
    state = text[-2]
    address = [street,city,state]
    return address

def parse_email(text:str):
    """
    This function will contain one parameter, text, a string representing a single line of the file
    This function should use regular expressions in order to capture the email of the person in question
    This function will return the email identified.
    https://www.emailregex.com/ for email regex
    """
    
    email = re.search(r"([a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+)", text).group()
    return email
    
class Address():
    """
    This class will have three attributes (street, city, state) that are created from the arguments that are passed in when an instance
    of address is created
    This class will not have any methods
    """
    def __init__(self, street, city, state):
        self.street = street
        self.city = city
        self.state = state

class Employee():
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
    def __init__(self,text):
        self.firstname = parse_name(text) [0]
        self.lastname = parse_name(text) [1]
        street = parse_address(text) [0]
        city = parse_address(text) [1]
        state = parse_address(text) [2]
        self.address = Address(street, city, state)
        self.email = parse_email(text)
    
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
    with open(path,"r") as file:
        for text in file:
            inst_employee = Employee(text)
            employee_list.append(inst_employee)
            
    return employee_list
    

#def parse_args(args_list):
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
    
    #arguments = parse_args(sys.argv[1:]) #Pass in the list of command line arguments to the parse_args function.
    
    #The returned object is an object with those command line arguments as attributes of an object.
    #We will pass both of these arguments into the main function.
    #Note that you do not need a main function, but you might find it helpfull.
    #You do want to make sure to have minimal code under the 'if __name__ == "__main__":' statement.
    
   # main(arguments.required, arguments.optional)

    
    employee_list = main("people.txt")
    for i in employee_list:
        print("\n\tFirst name:   ",i.firstname)
        print("\tLast name:    ",i.lastname)
        print("\tAddress:      ",i.address.street)
        print("\tCity:         ",i.address.city)
        print("\tState:        ",i.address.state)
        print("\tEmail:        ",i.email)
