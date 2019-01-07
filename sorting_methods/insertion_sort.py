
# input  is a List of unsorted numbers
# output is a List of sorted numbers


def insertion_sort(array):

	for i in range(0, len(array)-1):
		# compare current and next numbers. if next lower then current we have to stop outer cycle and
		# to find position of next number at previously watched part of array
		if array[i+1] < array[i]:
			# need to save a number that is not in its position to "lowest"
			lowest = array[i+1]
			for j in range(-len(array)+i, -len(array)-1, -1):
				# have to take part of previously watched array and have to compare pairs of number until the
				# corresponding position is found. Need to shift the numbers from left to right
				# until the number on the left will be smaller than the stored number in "lowest"
				if array[j] > lowest:
					array[j+1] = array[j]
					if j == -len(array):
						array[j] = lowest
				else:
					array[j+1] = lowest
					break

	return array


