
# input  is a List of unsorted numbers
# output is a List of sorted numbers

def bubble_sort(array):

	for i in range(len(array)-1):
		# have to move pointer on beginning element of array each iteration on position +1
		for j in range(i, len(array)):
			# on each step have to compare two numbers and if condition is met have to swap this numbers
			if array[i] > array[j]:  # '>' - Sort Ascending; '<' - Sort Descending
				tmp = array[i]
				array[i] = array[j]
				array[j] = tmp

	return array

