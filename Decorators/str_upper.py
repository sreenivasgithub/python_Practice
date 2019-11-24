# it followed by the Decorator name

def str_upper(func):
	def inner():
		a = func()
		return a.upper()
	return inner

@str_upper
def abc():
	return "hi, i am sreenivas"
print(abc())