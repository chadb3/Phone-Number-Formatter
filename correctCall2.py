from collections import UserString
from src.phoneNumberManager import phoneNumberManager
def main():
    a=phoneNumberManager()
    usrInput=""
    loopVal=True
    while(loopVal):
        usrInput=input("> ")
        usrInput=usrInput.upper()
        if(usrInput=="EXIT" or usrInpt=="EXIT()"):
            break
        elif(usrInput=="PRINT"):
            a.printList()
        elif(usrInput=="RANDOM"):
            a.newRandomPhoneNumber()
        elif(usrInput=="PRINT 2"):
            a.printSimple()
        elif(usrInput=="HELP" or usrInput=="COMMAND" or usrInput=="COMMANDS"):
            print("EXIT\nRANDOM\nPRINT 2\nHELP")
        else:
            a.newPhoneNumber(usrInput)

if __name__ == "__main__":
	main()