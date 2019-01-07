
# input  is a List of unsorted numbers
# output is a List of sorted numbers


def cocktail_sort(array):

	h = 0  # position from the beginning of the array
	t = 0  # position from the end of the array
	while h+t < len(array):

		# moving highest number to the end of array
		for j in range(h, len(array)-1-t):
			if array[j] > array[j+1]:
				tmp = array[j]
				array[j] = array[j+1]
				array[j+1] = tmp
		t += 1  # move end of array for consideration to position -1

		# moving lowest number to the beginning.
		for j in range(-(t+1), -((len(array)+1)-h), -1):
			if array[j] > array[j+1]:
				tmp = array[j]
				array[j] = array[j+1]
				array[j+1] = tmp
		h += 1  # move beginning of array for consideration to position +1

	return array
