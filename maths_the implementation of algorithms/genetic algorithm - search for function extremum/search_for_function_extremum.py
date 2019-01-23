import random
import math
import json
import time


# function formats expected count of pairs from inputted population
# input: population
# 		 count_pairs_of_persons - how many pairs expected
# output list of pairs
def pair_formation(population, count_pairs_of_persons):

	crossbreeding_population = []
	if len(population) > 1:

		for i in range(count_pairs_of_persons):
			index_person1 = random.randint(0, len(population)-1)
			while True:
				index_person2 = random.randint(0, len(population)-1)
				if index_person2 != index_person1:
					break
			crossbreeding_population.append(
				[population[index_person1], population[index_person2]])
		return crossbreeding_population

	else:
		return population


# function for selection pairs of person for crossbreeding.
# input are: population - current population
# 			 flag - setup type of selection
# 					1 - panmixia
# 					2 - selective
# 			count_pairs_of_persons - number of generated pairs of persons
# output: is population for crossbreeding
def selection_for_crossbreeding(population, flag, count_pairs_of_persons):

	population_for_crossbreeding = []

	if flag == 1:
		population_for_crossbreeding = pair_formation(population,
													count_pairs_of_persons)

	elif flag == 2:
		total = 0
		crossbreeding_population = []
		for person in population:
			total += person[2]

		average = total / len(population)

		for person in population:
			if person[2] >= average:
				crossbreeding_population.append(person)

		if len(crossbreeding_population) == 0:
			index = random.randint(0, len(population) - 1)
			crossbreeding_population.append(population[index])
			index = random.randint(0, len(population) - 1)
			crossbreeding_population.append(population[index])
		elif len(crossbreeding_population) == 1:
			index = random.randint(0, len(population) - 1)
			crossbreeding_population.append(population[index])

		population_for_crossbreeding = pair_formation(crossbreeding_population,
													count_pairs_of_persons)

	return population_for_crossbreeding


# Population sorting by bubble sort algorithm (Descending)
def population_sorting(population):

	for i in range(len(population) - 1):
		for j in range(i, len(population)):
			if population[i][2] < population[j][2]:
				tmp = population[i][2]
				population[i][2] = population[j][2]
				population[j][2] = tmp

	return population


# quality calculation for each person of excepted population
# input is population (list)
# output is population (list) with calculated quality
def quality_calculation(population):

	for person in population:
		person[2] = fitness_function(person[0], person[1])

	return population


# function contains math equation of distributions in two-dimensional
# space.
# Input is (int) value_x, (int) value_y of one person
# output is (int) calculated value
def fitness_function(value_x, value_y):

	result = 0

	try:
		result = round(100 / (100 * (math.pow(value_x, 2) - value_y) +
							  math.pow((1 - value_x), 2) + 1), 5)
	except ZeroDivisionError:
		result = 0

	return result


# function create initial population by random generating numbers in
# expected range(start, end).
# input are start, end - range for creating new persons
# 			size - count of person for new population
# 			accuracy - count of digits after '.'
# output are list of lists. inner lists contain id of person, it value and
# 			quality of current person: [value_x, value_y, quality].
# 			Now quality = 0.
def create_an_initial_population(start_x, end_x, start_y, end_y, size, accuracy):
	initial_population = list()

	for person in range(size):
		value_x = round(start_x + (end_x - start_x) * random.random(), accuracy)
		value_y = round(start_y + (end_y - start_y) * random.random(), accuracy)
		initial_population.append([value_x, value_y, 0])

	return initial_population


# converting from binary to gray code and back.
# input "number" is input (int) number
# 		"flag" shows which operation need to perform
# 				True - binary to gray
# 				False - gray to binary
# output is (int) number
def gray_code_converter(number, flag):

	if flag:
		return number ^ (number >> 1)
	else:
		mask = number
		while mask != 0:
			mask >>= 1
			number ^= mask
		return number


# Function get the byte from int number by position
def get_bit(x, n):

	return x & (1 << n) and 1 or 0


# Function change bit to "1" in int number by position
def set_bit(value, bit):

	return value | (1 << bit)


# Function change bit to "0" in int number by position
def clear_bit(value, bit):

	return value & ~(1 << bit)


# function will perform crossbreeding by two numbers
# input:
# 		- numb1 - 1 number (person 1)
# 		- numb2 - 2 number (person 2)
# 		- pointer1 - shows start bit for crossbreeding
# 		- pointer2 - if pointer2 != -1, part of numbers for crossbreeding
# 						is between pointer1 and pointer2
# output: is a number -  result of crossbreeding
def crossing(numb1, numb2, pointer1, pointer2):

	if pointer2 == -1:
		for i in range(0, pointer1):

			bit = get_bit(numb2, i)
			if bit == 1:
				numb1 = set_bit(numb1, i)
			elif bit == 0:
				numb1 = clear_bit(numb1, i)
	else:
		for i in range(pointer1, pointer2):

			bit = get_bit(numb2, i)
			if bit == 1:
				numb1 = set_bit(numb1, i)
			elif bit == 0:
				numb1 = clear_bit(numb1, i)

	return numb1


# function returns the max count of bits for both number
def bit_length(numb1, numb2):

	length1 = numb1.bit_length()
	length2 = numb2.bit_length()
	if length1 >= length2:
		common_length = length1
	else:
		common_length = length2

	return common_length


# function perform crossbreeding
# input: pairs - count of person pairs for crossbreeding
# 		accuracy - count of digits after "."
# 		numbers_of_breaks - define how to perform crossbreeding,
# 							by 1 break or by 2
# 		cross_probability - define what probability is for crossbreeding
# 		mut_probability - define what probability is for mutation
# output: list of persons after crossbreeding and mutation
def crossbreeding(pairs, accuracy, number_of_breaks, cross_probability,
				mut_probability):

	crossbreed_pairs = []

	for i in range(len(pairs)):
		if probability(cross_probability):
			numb1_x = gray_code_converter(int(pairs[i][0][0] *
										math.pow(10, accuracy)), True)
			numb1_y = gray_code_converter(int(pairs[i][0][1] *
										math.pow(10, accuracy)), True)
			numb2_x = gray_code_converter(int(pairs[i][1][0] *
										math.pow(10, accuracy)), True)
			numb2_y = gray_code_converter(int(pairs[i][1][1] *
										math.pow(10, accuracy)), True)
			tmp_x1 = numb1_x
			tmp_y1 = numb1_y

			common_length_x = bit_length(numb1_x, numb2_x)
			common_length_y = bit_length(numb1_y, numb2_y)

			if number_of_breaks == 1:
				pointer = random.randint(0, common_length_x)
				numb1_x = crossing(numb1_x, numb2_x, pointer, -1)
				numb2_x = crossing(numb2_x, tmp_x1, pointer, -1)

				pointer = random.randint(0, common_length_y)
				numb1_y = crossing(numb1_y, numb2_y, pointer, -1)
				numb2_y = crossing(numb2_y, tmp_y1, pointer, -1)
			else:
				pointer1 = random.randint(0, common_length_x//2)
				pointer2 = random.randint(common_length_x//2, common_length_x)
				numb1_x = crossing(numb1_x, numb2_x, pointer1, pointer2)
				numb2_x = crossing(numb2_x, tmp_x1, pointer1, pointer2)

				pointer1 = random.randint(0, common_length_y//2)
				pointer2 = random.randint(common_length_y//2, common_length_y)
				numb1_y = crossing(numb1_y, numb2_y, pointer1, pointer2)
				numb2_y = crossing(numb2_y, tmp_y1, pointer1, pointer2)

			numb1_x = gray_code_converter(mutation(numb1_x, mut_probability), False) / \
				  	math.pow(10, accuracy)
			numb2_x = gray_code_converter(mutation(numb2_x, mut_probability), False) / \
				  	math.pow(10, accuracy)
			numb1_y = gray_code_converter(mutation(numb1_y, mut_probability), False) / \
				  	math.pow(10, accuracy)
			numb2_y = gray_code_converter(mutation(numb2_y, mut_probability), False) / \
				  	math.pow(10, accuracy)

			crossbreed_pairs.append([numb1_x, numb1_y, 0])
			crossbreed_pairs.append([numb2_x, numb2_y, 0])
		else:
			crossbreed_pairs.append([pairs[i][0][0], pairs[i][0][1], 0])
			crossbreed_pairs.append([pairs[i][1][0], pairs[i][1][1], 0])

	return crossbreed_pairs


# function returns boolean variable.
# whether the event occurred (True) or not (False)
def probability(p):

	k = random.random()
	if k < p:
		return True
	else:
		return False


# perform mutation for each bit of input int number by probability case
# returns number after mutation
def mutation(numb, mutation_propability):

	length = numb.bit_length()
	for i in range(length):
		if probability(mutation_propability):
			if get_bit(numb, i) == 1:
				numb = clear_bit(numb, i)
			else:
				numb = set_bit(numb, i)

	return numb


# function updates population by criteria. Best persons by f_function of
# previous population and current will be placed in common population
# input: old_population - list with previous population
# 		new_population - list of population after crossbreeding and mutation
# 		population_size - (int) size of population
# output: list with best person from both populations by fitness function
def population_update(old_population, new_population, population_size):

	old_pop_counter = 0
	new_pop_counter = 0

	updated_population = []

	old_population = population_sorting(old_population)
	new_population = population_sorting(new_population)

	if len(old_population) == 0:
		updated_population == new_population[:]
	elif len(new_population) == 0:
		updated_population == old_population[:]
	else:

		for counter in range(population_size):

			if old_pop_counter < len(old_population) and new_pop_counter < len(new_population):
				if old_population[old_pop_counter][2] >= new_population[new_pop_counter][2]:
					updated_population.append(old_population[old_pop_counter])
					old_pop_counter += 1
				else:
					updated_population.append(new_population[new_pop_counter])
					new_pop_counter += 1
			elif old_pop_counter == len(old_population):
				updated_population.append(new_population[new_population])
				new_pop_counter += 1
			elif new_pop_counter == len(new_population):
				updated_population.append(old_population[old_pop_counter])
				old_pop_counter += 1

	return updated_population


# main function contains all start parameters and logic of execution.
def main_f():

	start_x = 1.28  # set start of range by x
	end_x = -1.28  # set end of range by x
	start_y = 1.28  # set start of range by y
	end_y = -1.28  # set end of range by y
	population_size = 20  #set how many person will take participation
							# at crossbreeding
	count_pairs_of_persons = 10  # how many pairs of person will be take
								# participation in crossbreeding
	accuracy = 5  # count of digit after "." at float value of parameters
									# persons and at f_function value
	number_of_breaks = 2  # count of breaks for crossbreeding. 1 or 2
	selection_type = 2	 # type of selection. 1 - panmixia, 2 - selection
	count_of_generations = 10000  # count of generation
	crossbreeding_probability = 0.6  # crossebreeding probability for each
									# pair of persons
	mutation_probability = 0.4   # mutation probability for each bit of
									# person
	set_of_unic_f_func = set()  # set of uniq f_func values
	list_of_unic_persons = list()  # list of uniq person

	# 1 stage - create new generation
	population = create_an_initial_population(start_x, end_x, start_y,
										end_y, population_size, accuracy)
	# 2 stage - calculate fitness function for each person at init population
	population = quality_calculation(population)

	# put all person to list_of_unic_persons
	for i in range(len(population)):
		if population[i][2] not in set_of_unic_f_func:
			set_of_unic_f_func.add(population[i][2])
			list_of_unic_persons.append(population[i])

	# perform excepted count of generation
	for generation in range(count_of_generations):

		# 3 stage - perform selection for crossbreeding
		pairs_for_crossbreeding = selection_for_crossbreeding(
			population, selection_type,	count_pairs_of_persons)

		# 4, 5 stages perform crossbreeding and mutation
		progeny_population = crossbreeding(pairs_for_crossbreeding, accuracy, number_of_breaks,
										   crossbreeding_probability, mutation_probability)

		# 5 stage - calculate fitness function for each person at progeny population
		progeny_population = quality_calculation(progeny_population)
		for i in range(len(progeny_population)):
			if progeny_population[i][2] not in set_of_unic_f_func:
				set_of_unic_f_func.add(progeny_population[i][2])
				list_of_unic_persons.append(progeny_population[i])

		# 5 create new population on base of prev and new population
		population = population_update(population, progeny_population, population_size)

	# print the last gen population
	for i in range(len(population)):
		print("{0}) f_func({1}, {2}) = {3} | ".format(i, population[i][0], population[i][1], population[i][2], generation),  end='')

	# write all uniq persons to *.json file
	json_dump_filename = "dump_file_" + time.strftime("%c") + ".json"
	print(json_dump_filename)
	with open(json_dump_filename, "w") as json_obj:
		json.dump(list_of_unic_persons, json_obj)


main_f()
