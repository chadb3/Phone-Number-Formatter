from src import *
def main():
	hasExtension=False
	phone_number=Phone_Number(input("\nEnter Phone Number: "))
	if(phone_number.isPhoneNumber):
		phone_number.addExtension(input("Extension (leave blank if no): "))
	phone_number.printPhoneNumber()
	phone_number.checkAreaCode()
	return 0
if __name__ == "__main__":
	main()
