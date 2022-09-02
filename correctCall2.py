from collections import UserString
from src.phoneNumberManager import phoneNumberManager
def main():
    a=phoneNumberManager()
    usrInput=""
    loopVal=True
    while(loopVal):
        usrInput=input("> ")
        a.newPhoneNumber(usrInput)
        if(usrInput.upper()=="EXIT"):
            break
        a.printList()

if __name__ == "__main__":
	main()