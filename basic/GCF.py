# Function for calculation of the greatest common factor (GFC) of two
# (int) numbers. Calculation will perform by the Euclidean algorithm.

# Input is two (int) numbers.
# Output is (int) number.


def gcf(number1, number2):

	sequence = []
	counter = 0
	if number1 != 0 and number2 != 0:

		if number1 > number2:
			sequence.append(number1)
			sequence.append(number2)
		elif number2 > number1:
			sequence.append(number2)
			sequence.append(number1)

		while True:
			modulo = sequence[counter] % sequence[counter + 1]
			if modulo != 0:
				sequence.append(modulo)
				counter += 1
			elif modulo == 0:
				counter += 1
				break

	else:
		return -1

	return sequence[counter]
