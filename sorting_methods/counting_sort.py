
# input:
# 		- "sortable_array" - is list of array for sorting;
# 		- "arr_of_pssbl_nmbrs" - list of possible number at array for sorting
# output:
# 		- sorted array


def counting_sort(sortable_array, arr_of_pssbl_nmbrs):

	# array for counting of same numbers
	counting_array = [0] * len(arr_of_pssbl_nmbrs)

	# counting of same numbers
	for i in range(len(sortable_array)):
		counting_array[arr_of_pssbl_nmbrs.index(sortable_array[i])] += 1

	# filling of input array by the sorted numbers
	pointer = 0
	for i in range(len(counting_array)):

		for j in range(pointer, pointer + counting_array[i]):
			sortable_array[j] = arr_of_pssbl_nmbrs[i]
		pointer += counting_array[i]

	return sortable_array

