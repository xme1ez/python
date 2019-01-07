
# input  is a List of unsorted numbers
# output is a List of sorted numbers


def cocktail_sort(array):

	h = 0
	t = 0
	while h+t < len(array):

		for j in range(h, len(array)-1-t):
			if array[j] > array[j+1]:
				tmp = array[j]
				array[j] = array[j+1]
				array[j+1] = tmp
		t += 1

		for j in range(-(t+1), -((len(array)+1)-h), -1):
			if array[j] > array[j+1]:
				tmp = array[j]
				array[j] = array[j+1]
				array[j+1] = tmp
		h += 1

	return array
