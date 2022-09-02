from collections import UserString
from src.phoneNumberManager import phoneNumberManager
def main():
    a=phoneNumberManager()
    usrInput=""
    loopVal=True
    while(loopVal):
        usrInput=input("> ")
        if(usrInput.upper()=="EXIT"):
            break
        elif(usrInput.upper()=="PRINT"):
            a.printList()
        elif(usrInput.upper()=="RANDOM"):
            a.newRandomPhoneNumber()
        elif(usrInput.upper()=="PRINT 2"):
            a.detailedPrint()
        else:
            a.newPhoneNumber(usrInput)

if __name__ == "__main__":
	main()