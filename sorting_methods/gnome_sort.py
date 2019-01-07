
# input  is a List of unsorted numbers
# output is a List of sorted numbers


def gnome_sort(array):

	for i in range(0, len(array)-1):
		# compare current and next numbers. if next lower then current we have to stop outer cycle and
		# to find position of next number at previously watched part of array
		if array[i+1] < array[i]:
			for j in range(-len(array)+i, -len(array)-1, -1):
				# have to take part of previously watched array and have to compare pairs of number until the
				# corresponding position is found. if number on higher position lowest then number on lower
				# position have to swap two compared number.
				if array[j+1] < array[j]:
					tmp = array[j+1]
					array[j+1] = array[j]
					array[j] = tmp

	return array
