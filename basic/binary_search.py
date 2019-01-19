# Function binary_search define position of number in a list
# Input is:
# 			list_for_search - list of int numbers where function have to find index
# 							  of goal number
# 			number_for_search - int number which index function have to find
# Output is:
# 			 (int) index of goal number at list for search


def binary_search(list_for_search, number_for_search):

	if len(list_for_search) == 0:
		result = -1

	elif len(list_for_search) == 1:
		result = 0

	elif number_for_search not in list_for_search:
		return -1

	else:
		start_point = 0
		end_point = len(list_for_search)

		while True:
			middle_pointer = (end_point - start_point) // 2 + start_point
			if number_for_search > list_for_search[middle_pointer]:
				start_point = middle_pointer
			elif number_for_search < list_for_search[middle_pointer]:
				end_point = middle_pointer
			elif number_for_search == list_for_search[middle_pointer]:
				result = middle_pointer
				break

	return result

