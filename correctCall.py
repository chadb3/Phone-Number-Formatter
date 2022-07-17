import re
# Takes in a "Phone Number"
def nullPhone(phoneNumberIn):
	# Prints the phone number in the before state
	print("Before: {}".format(phoneNumberIn))

	# Debug Length from before regex
	# print(len(phoneNumberIn))

	# uses regex to match digits (the \D) and make everything else blank (the "")
	newPhone = re.sub(r"\D", "", phoneNumberIn)
	# prints only the digits (0-9)
	# in other words, anything that wasn't a digit is destroyed.
	print(newPhone)

# main calls the function currently called nullPhone (that removes everything that is not a digit).
def main():
	# nullPhone takes in an a user input as a "Phone Number".
	nullPhone(input("Enter Phone Number: "))
	return 0

if __name__ == "__main__":
	main()
