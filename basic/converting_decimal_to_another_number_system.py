# Function can be use for converting number in decimal system to
# another system from 2 to 9.
# Input is:
# 			number - number for converting (int)
# 			system - system of converted number (int)
# Output is:
# 			converted number (int)


def converting_decimal_to_another_number_system(number, system):

	converted_number = []

	if system != 0 and system != 1:
		while True:
			remainder = number % system
			converted_number.append(remainder)
			number //= system
			if number == 0:
				break
	else:
		converted_number.append(-1)

	converted_number.reverse()

	return int(''.join(str(element) for element in converted_number))


