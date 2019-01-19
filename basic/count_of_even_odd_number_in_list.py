# function calculate count of odd and even numbers at input list
# input is a list of numbers
# output is a list where:
# 							[0] - even count
# 							[1] - odd count


def count_even_odd_numbers(input_list):

	odd_counter = 0
	even_counter = 0

	for number in input_list:

		if number % 2 == 0:
			even_counter += 1
		else:
			odd_counter += 1

	return [even_counter, odd_counter]
