# work with *.json dump file
# if user starts program first time (.json file is empty) programs asks
# to enter user favorite number. if user entered his favorite number before
# program shows it.


import json

file_name = "dump_file.json"


def get_favourite_number():

	try:
		with open(file_name) as file_obj:
			content = json.load(file_obj)
	except FileNotFoundError:  # if file not found
		return None
	except ValueError:  # if file is empty
		return None
	else:
		return content


def write_favourite_number():

	while True:
		try:
			number = int(input("Enter your favourite number: "))
		except ValueError:
			print("Wrong enter! Try again, please ;) \n")
		else:
			break

	try:
		with open(file_name, 'w') as file_obj:
			json.dump(number, file_obj)
	except FileNotFoundError:
		print("File not Found")


def favourite_number():

	print("Hello, Dear!")

	fav_number = get_favourite_number()

	if fav_number:
		print("Your favorite number is -> {}".format(str(fav_number)))
	else:
		write_favourite_number()


favourite_number()
