from collections import UserString
from src.phoneNumberManager import phoneNumberManager
def main():
    a=phoneNumberManager()
    usrInput=""
    loopVal=True
    while(loopVal):
        usrInput=input("> ")
        usrInput=usrInput.upper()
        if(usrInput=="EXIT" or usrInput=="EXIT()"):
            break
        elif(usrInput=="PRINT"):
            a.printList()
        elif(usrInput=="RANDOM"):
            a.newRandomPhoneNumber()
        elif(usrInput=="PRINT 2"):
            a.printSimple()
        elif(usrInput=="PRINT 3"):
            a.printPnWithCount()
            num=input("Enter Number to Print: ")
            a.printSimpleIndex(num)
        elif(usrInput=="RANDOM 2"):
            place=input("Input state abbreviation: ").upper()
            a.genRanPhoneFromPlace(place)
        elif(usrInput=="HELP" or usrInput=="COMMAND" or usrInput=="COMMANDS"):
            print("EXIT\nRANDOM\nRANDOM 2\nPRINT 2\nPRINT 3\nHELP")
        else:
            a.newPhoneNumber(usrInput)

if __name__ == "__main__":
	main()