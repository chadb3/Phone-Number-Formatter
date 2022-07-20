import re
def nullPhone(phoneNumberIn):
	print("Before: {}".format(phoneNumberIn))
	print(len(phoneNumberIn))
	newPhone = re.sub(r"\D", "", phoneNumberIn)
	print(newPhone)

def main():
	nullPhone(input("Enter Phone Number: "))

if __name__ == "__main__":
	main()