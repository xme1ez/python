# determining the sum of all numbers less than MAX variable, multiples of
# numbers at list.


def determining(max, dividers):

	sum = 0
	for num in range(max):  # loop through numbers in searchable range
		for elem in dividers:  # loop through dividers
			if num % elem == 0:
				sum += num
				break

	return sum
