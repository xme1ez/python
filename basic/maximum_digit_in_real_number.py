# Function will define the maximum digit at real number
# Input is a real or int number
# Output is an maximum int number


def maximum_digit_in_real_number(real_number):

	maximum_digit = 0

	real_number = str(real_number)
	real_number = list(real_number)
	if '.' in real_number:
		real_number.remove('.')
	real_number = list(int(digit) for digit in real_number)

	for digit in real_number:
		if digit > maximum_digit:
			maximum_digit = digit

	return maximum_digit


print(maximum_digit_in_real_number(0.0))
