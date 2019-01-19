# function will define which number at input list is positive and
# which is negative. Numbers fit to separate lists.
# Function returns list of lists:
# 								[0] - lists of positive numbers
# 								[1] - list of negative numbers


def separation_into_positive_negative(input_list):
	positive_list = []
	negative_list = []

	for element in input_list:
		if element >= 0:
			positive_list.append(element)
		else:
			negative_list.append(element)

	return [positive_list, negative_list]
