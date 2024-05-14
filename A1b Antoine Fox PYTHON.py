#-------------------------------------
#Name: Antoine Fox
#Date: 4/04/24
#Reference: Assignment 1b for CISP 300
#Title: Customer info update
#Inputs: My name, birth city, birth year
#Process: Store the data
#Outputs: Print stored data
#-------------------------------------



#Initialize variables
fNameVariable = str(input("Your first name:"))
mNameVariable = str(input("Your Middle name:"))
lNameVariable = str(input("Your last name:"))
cityVariable = str(input("The city you were born in:"))
birthYearVariable = 0 
birthYearVariable = int(input("Enter your 4 digit birth year:"))

#main module to print out info
def main(fname, mname, lname, city, birth):
    print("My name is: \t\t", fname, mname, lname)
    print("My birth city is: \t", city)
    print("My birth year is: \t", birth)
main(fNameVariable, mNameVariable, lNameVariable, cityVariable, birthYearVariable)
