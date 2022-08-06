from src import *
def main():
	hasExtension=False
	phone_number=Phone_Number(input("\nEnter Phone Number: "))
	phone_number.addExtension(input("Extension (leave blank if no): "))
	phone_number.printPhoneNumber()
	return 0
if __name__ == "__main__":
	main()
