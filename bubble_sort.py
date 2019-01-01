

def bubble_sort(array):

	opp_count = 0
	assign_count = 0

	for i in range(len(array)-1):
		for j in range(i, len(array)):
			if array[i] > array[j]:  # '>' - Sort Ascending; '<' - Sort Descending
				tmp = array[i]
				array[i] = array[j]
				array[j] = tmp
				assign_count += 1
			opp_count += 1

	print(array)
	print(opp_count)
	print(assign_count)









arr_list = [3, 9, 6, 0, 8, 5, 7, 4, 1, 2]

bubble_sort(arr_list)

