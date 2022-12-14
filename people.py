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

def parse_name(text:str):
    """
    This function will contain one parameter, text, a string representing a single line of the file.
    This function should use regular expressions in order to capture the first name and the last name of the person in question
    This function will return a tuple containing the first and the last names as strings
    """
    first = re.search(r"(^\w+)",text).group(1)
    last = re.search(r"\s(\w+.?(?=\s\d))",text).group(1)
    names = (first,last)  
    return names
    
def parse_address(text:str):
    """
    This function will contain one parameter, text, a string representing a single line of the file
    This function should use regular expressions in order to capture the street, city and state of person in question
    This function will create and return an address object using the street, city and state identified.
    """

    street = re.search(r"\s(\d+\s.+?(?=\s\w+\s+[A-Z]{2}))",text).group(1)
    city = re.search(r"\s(\w+?(?=\s+[A-Z]{2}))",text).group(1)
    state = re.search(r"\s([A-Z]{2})",text).group(1)
  
    return (street,city,state)

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
    ??? This class will have 4 attributes (first_name, last_name, address, email).
        ??? These attributes will all be created by passing in a row of the file when an instance of
        employee is created. This meaning, the init method will only have one parameter other than self.
        ??? The first_name and last_name attributes are created by calling the parse_name function
        and passing in the parameter of the init method of employee as an argument in the parse_name function call.
        ??? The address attribute is created by calling the parse_address function and passing in the
        parameter of the init method of employee as an argument in the parse_address function call.
        ??? The email attribute is created by calling the parse_email function and passing in the
        parameter of the init method of employee as an argument in the parse_email function call.
    ??? This class will not have any methods.
    """
    def __init__(self,text):
        self.first_name = parse_name(text) [0]
        self.last_name = parse_name(text) [1]
    
        street, city, state = parse_address(text)

        self.address = Address(street, city, state)

        self.email = parse_email(text)
    
def main(path):
    """
    Write a main function. Your main should have one parameter, path, which is the path to the file
    that is being parsed.
        ??? Create an empty list called employee_list.
        ??? Open up the file from the path.
    ??? For each line in the file, create an instance of employee by passing in the string which is
    the line of the file that you are reading.
    ??? Append this instance to the employee_list.
    ??? Within the main, return the employee_list
    """
    employee_list = []
    with open(path,"r") as file:
        for text in file:
            inst_employee = Employee(text)
            employee_list.append(inst_employee)
            
    return employee_list
    

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
        print("\n\tFirst name:   ",i.first_name)
        print("\tLast name:    ",i.last_name)
        print("\tAddress:      ",i.address.street)
        print("\tCity:         ",i.address.city)
        print("\tState:        ",i.address.state)
        print("\tEmail:        ",i.email)