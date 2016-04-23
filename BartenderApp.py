questions = {
	"strong": "Do you like your drinks strong?",
	"salty": "Do you like your drinks salty?",
	"bitter": "Do you like your drinks bitter?",
	"sweet": "Do you like your drinks sweet?",
	"fruity": "Do you like your drinks frutiy?",
}

ingredients = {
	"strong": ["whiskey", "rum", "gin"],
	"salty": ["salted rim", "bacon", "olives"],
	"bitter": ["bitters", "tonic water", "lemon peel"],
	"sweet": ["sugar cube", "honey", "coca cola"],
	"fruity": ["orange", "cherry", "pineapple"],
}

def customer_preferences():
	"""Asks what customers like"""
	preferences = {}
	for key, value in questions.items():
		print (value)
		answer = input()
		if answer.lower() in ('yes','y'):
			preferences[key] = True
		elif answer.lower() in ('no','n'):
			preferences[key] = False
	return preferences

def make_drink():
	"""Makes drink according to preferences"""
	preferences = customer_preferences ()
	for key, value in ingredients.items():
		if preferences [key]:
			print (value)

if __name__ == '__main__':
	make_drink ()
