import sys

def calculate(action, arg1, arg2):
	if action=='add':
		return arg1+arg2
	if action=='multiply':
		return arg1*arg2
	return None

def parseArguments(str):
	if str=='':
		return None
	# for character in str:

def main():
	try:
		exp = (sys.argv[1])
		for char in exp:
			print(char)
		print(exp)
	except:
		print("Invalid input")

if __name__ == '__main__':
    main()