
# input  is a List of unsorted numbers
# output is a List of sorted numbers


def selection_sort(array):

	for i in range(len(array)):
		# initialize minimal number and it position
		min_numb = array[i]
		min_numb_pos = i
		# from start position to end have to find minimal number and swap it with number on position "i"
		for j in range(i, len(array)):
			if min_numb > array[j]:
				min_numb = array[j]
				min_numb_pos = j
		# if minimal number and number on position "i" are not the same - swap both number
		if i != min_numb_pos:
			swap_number = array[i]
			array[i] = min_numb
			array[min_numb_pos] = swap_number

	return array


