

# function will count sum of three digit number
# input is three-digit number

def sum_of_three_digit_number(three_digit_number):

	digit_to_str = str(three_digit_number)
	first = int(digit_to_str[0])
	second = int(digit_to_str[1])
	third = int(digit_to_str[2])

	return first+second+third

