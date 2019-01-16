
# function will count mass, volume or density
# for each choice have to input 2 parameters
# flag (m - mass, v - volume or d - density shows which parameters you
# would like to calculate


def mass_volume_density_calculation():

	flag = input("What do you want to calculate? (m, v, d): ")

	if flag == "m":
		volume = input("Input volume: ")
		density = input("Input density: ")
		mass = int(density) * int(volume)
		return mass

	elif flag == "v":
		mass = input("Input mass: ")
		density = input("Input density: ")
		volume = int(mass) / int(density)
		return volume

	elif flag == "d":
		mass = input("Input mass: ")
		volume = input("Input volume: ")
		density = int(mass) / int(volume)
		return density
	else:
		return -1


