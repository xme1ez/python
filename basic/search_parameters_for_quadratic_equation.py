# Function will define which combination of a, b, c for quadratic
# equation (ax^2+bx+c=0) have solution.
# Input is:
# 			(int) mina, maxa - range for searching parameter 'a'
# 			(int) minb, maxb - range for searching parameter 'b'
# 			(int) minc, maxc - range for searching parameter 'c'
# Output is:
# 			list of possible combination. each combination contains at
# 										tuple (a, b, c).


import math


def search_parameters_for_quadratic_equation(mina, maxa, minb, maxb, minc, maxc):

	list_of_possible_combinations = []

	for a in range(mina, maxa + 1):
		for b in range(minb, maxb + 1):
			for c in range(minc, maxc + 1):
				d = math.pow(b, 2) - 4 * a * c

				if d < 0:
					continue
				elif d == 0 or d > 0:
					list_of_possible_combinations.append((a, b, c))

	return list_of_possible_combinations
