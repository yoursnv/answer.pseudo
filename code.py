# Code for WingiFy
# This is my python code..ok tested.
# The program is to generate random number between 6 and 15 and return the result in this format: “Name GeneratedNumber”. Eg: “Rahul 11”

# author : Nitin V Kuttan
# email: nitinvkttn@gmail.com

# import packege named random
import random

# we will now define a function called number_name that takes it as a parameter
def number_name():
	# input the name from the user!!
	name =  input("Enter the name: ")
	# {}{} combines name and random.randrange
	# random.randrange gives a random number between 6 and 15
	print("{}{}".format(name, random.randrange(6,15)))

# calls the main function: number_name.
if __name__ == "__main__":number_name()