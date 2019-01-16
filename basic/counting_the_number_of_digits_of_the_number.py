

# function will count number of digits of "int" number
# there're 2 functions:
# - first  use converting from int to string
# - second use while loop

def number_of_digits_of_the_number1(number):

		dig_to_str = str(number)

		return len(dig_to_str)


def number_of_digits_of_the_number2(number):

	i = 0

	while number != 0:

		i += 1
		number //= 10

	return i
