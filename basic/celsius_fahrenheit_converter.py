
# function will convert temperature from celsius to fahrenheit or
# fahrenheit to celsius
# input:
# - temperature (int)
# - flag shows in which form the temperature is entered:
# 														- c - celsius
# 														- f - fahrenheit


def celsius_fahrenheit_converter(temperature, flag):

	if flag == "c":
		return (temperature * (9 / 5)) + 32
	elif flag == "f":
		return (temperature - 32) * (5 / 9)
	else:
		return -1




