# .................................................................. #
# Title:  Assignment07
# Description:  Script that includes pickling and exception handling
# Dev: Denise Albano
# Date: 2/27/22
# Change Log: (Who, When, What)
# DAlbano, 2/27/22, created pickling script
# DAlbano, 3/1/22, added exception handling script
# .................................................................. #

import pickle  # This imports code from another code file!

# Data ------------------------------------------------------------- #
strFileName = 'ChildData.dat'
lstChild = []

# Processing ------------------------------------------------------- #
def save_data_to_file(file_name, list_of_data):
    objFile = open(file_name, "ab")
    pickle.dump(list_of_data, objFile)
    objFile.close()

def read_data_from_file(file_name):
    objFile = open(file_name, "rb")
    list_of_data = pickle.load(objFile)
    objFile.close()
    return list_of_data

# Presentation ----------------------------------------------------- #
# Get name and age from user, then store it in a list object
while (True):
    print("""
    Menu of Options
    1) Add data
    2) Save data to file
    3) Read data from file
    4) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
    print()

    if (strChoice.strip() == '1'):
        while True:
            try:
                strName = str(input("Enter the child's name: "))
                if strName.isnumeric():
                    raise Exception("Do not use numbers for child's name")
                break
            except Exception as e:
                print("There was a non-specific error!")
                print("Built-In Python error info: ")
                print(e, e.__doc__, type(e), sep='\n')
                print()

        while True:
            try:
                intAge = int(input("Enter the child's age: "))
                if intAge < 0:
                    raise ValueError
                break
            except ValueError:
                print("Please use a postivie number")

        lstChild = [strName,intAge]

    # Store the list object into a binary file
    elif (strChoice.strip() == '2'):    # Store the list object into a binary file
        save_data_to_file(strFileName, lstChild)
        print("Data saved")

    # Read the data from the file into a new list object and display the contents
    elif (strChoice.strip() == '3'):
        print(read_data_from_file(strFileName))

    # Exit the program
    elif (strChoice.strip() == '4'):

        print("Goodbye!")
        break