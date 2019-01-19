# Function for define if the number is a simple or not.
# This is the simplest method of define.
# First stage is to find square root of input number
# Second stage is through the loop calculate modulo of input number and
# each number from range(2, square_root+1)
# Input is a (int) number
# Output is boolean:
# 					True if input number is a simplest number
# 					False if not.


import math


def check_on_the_simplicity_of_the_number(number):

	simplicity = True
	square_root = math.ceil(math.sqrt(number))

	for divider in range(2, square_root+1):
		if number % divider == 0:
			simplicity = False
			break

	return simplicity

