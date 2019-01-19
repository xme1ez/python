# Function will define is string palindrome or not.
# Input is:
# 			input_string - is a target string
# 			flag - indicating the effect of the register.
# 					True - case is sensitive
# 					False - case is not sensitive
# Output is:
# 			result - is boolean value. True -  string is a palindrome
# 									   False - string is not a palindrome


def is_string_palindrome_or_not(input_string, flag):

	counter = 0
	result = True

	if not flag:
		input_string = input_string.lower()

	while counter < len(input_string) // 2:

		if input_string[counter] != input_string[counter * (-1) - 1]:
			result = False
			break
		counter += 1

	return result

