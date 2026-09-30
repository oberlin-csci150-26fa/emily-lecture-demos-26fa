import random

def display_animal(c):
	"""
	given a number, return the corresponding animal
	"""

	animal = ''
	if c == 0:
		animal = '_/\__/\__0>' # worm
	elif c == 1:
		animal = '=^..^=' # cat
	else:
		animal = '(0.0)' # owl	

	return animal

print('Welcome to the text animal generator!')
choice = int(input("Choose 0, 1, or 2:"))
print(display_animal(choice))