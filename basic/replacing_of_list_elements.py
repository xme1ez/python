# Function will replace positive and negative numbers to expected value.
# Input:
# 		positive - value for replacing of positive numbers
# 		negative - value for replacing of negative numbers
# 		input_list - list of initial array
# Output: list of changed numbers


def replacing_of_list_elements(positive, negative, input_list):

	for index in range(0, len(input_list)):
		if input_list[index] > 0:
			input_list[index] = positive
		elif input_list[index] < 0:
			input_list[index] = negative

	return input_list










