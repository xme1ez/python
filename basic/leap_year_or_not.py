

# function will define entered year is leap or not
# input is year (int)


def leap_year_or_not(year):
	if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
		return "Year is leap"
	else:
		return "Year is't leap"
