# phone number object
#import importlib pep320ex omniproc
from src.phoneNumber import Phone_Number
# phone number manager is usable in other functions more easily.
class phoneNumberManager():
    # constructor
    def __init__(this):
        this._PN_LIST=[]
    # creates a new phone number, and adds it to the list
    def newPhoneNumber(this, pn_in):
        pn=Phone_Number(pn_in)
        if(pn.isPhoneNumber):
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
    # appends "notes" to current (numCalls-1)
    def addNoteToCurrentPN(this, note):
        noteToAppend=str(note)
        if(len(this._PN_LIST)>0):
            this._PN_LIST[len(this._PN_LIST)-1].addNotes(noteToAppend)
        else:
            print("No Phone Numbers")
    # sets the phone type for the current phone number
    def setPhoneTypeToCurrentPN(this):
        if(len(this._PN_LIST)>0):
            type=input("Cell, Work, Home, or Other: ")
            type=type.upper()
            if(type=="CELL" or type=="HOME" or type=="WORK" or type=="OTHER"):
                print(type)
                this._PN_LIST[len(this._PN_LIST)-1].addPhoneNumberType(type)
            else:
                print("Type not in list.")
        else:
            print("No Phone Numbers")
    def printTypes(this):
        for pn in this._PN_LIST:
            pn.printType()
    def printNotes(this):
        for pn in this._PN_LIST:
            pn.printNotes()
    #def checkIfPhoneNumber(this,input):
    def printSimple(this):
        for i in this._PN_LIST:
            i.simplePrint()