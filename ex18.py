def print_two(*args):
	arg1, arg2 = args
	print(f"arg1: {arg1}. arg2: {arg2}")

#*args is actually pointless we can just do
def print_two_again(arg1, arg2):
	print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
	print(f"arg1: {arg1}")

def print_none():
	print("I got nothin")


print_two("Kevin", "Huang")
print_two_again("Kevin", "Huang")
print_one("First!")
print_none()


