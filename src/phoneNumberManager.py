# phone number object
from phoneNumber import *
# phone number manager is usable in other functions more easily.
class phoneNumberManager():
    # constructor
    def __init__(this):
        this._PN_LIST=[]
    # creates a new phone number, and adds it to the list
    def newPhoneNumber(this, pn_in):
        pn=Phone_Number(pn_in)
        this._PN_LIST.append(pn)
    # generates random phone number and adds it to the list
    def newRandomPhoneNumber(this):
        pn=Phone_Number()
        this._PN_LIST.append(pn.generateRandom())
    # prints the list of phone numbers
    def printList(this):
        for phone_number in this._PN_LIST:
            print(phone_number)
    # prints the phone number's details
    def detailedPrint(this):
        for pn in this._PN_LIST:
            pn.printPhoneNumber()
    def genRanPhoneFromPlace(this, place):
        print("generating phone number from place: place")
        print("WIP")