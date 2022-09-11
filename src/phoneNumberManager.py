# phone number object
#import importlib pep320ex omniproc
#import importlib
#PNF=importlib.import_module("Phone-Number-Formatter")
from pickle import NONE
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
        #print("generating phone number from place: place")
        pn=Phone_Number()
        pn=pn.genPhoneNumberFromSpecificPlace(place)
        #print(pn.genPhoneNumberFromSpecificPlace(place))
        #print(an)
        #print("HIT")
        if(str(pn)==str(Phone_Number())):
            print("Not a valid location")
        else:
            print("{} created and added to list".format(pn))
            this._PN_LIST.append(pn)
        #this._PN_LIST.append(pn.genPhoneNumberFromSpecificPlace(place))
        #print("WIP")
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
    def printPnWithCount(this):
        index=1
        for i in this._PN_LIST:
            print("{}: {}".format(index,i))
            index+=1
    def printSimpleIndex(this, number):
        try:
            index=int(number)-1
            if(index<0):
                print("Index less than 0")
                return 0
        except:
            print("Input Not a Number")
            return 0
        try:
            print("Debug index: {}".format(index))
            this._PN_LIST[index].simplePrint()
        except:
            print("INDEX out of range")
    def removePhoneNumber(this):
        # print phone numbers
        # ask what number to remove.
        # remove from list
        print("Enter Number To Remove: ")
        num=1
        for pn in this._PN_LIST:
            print("{}: {}".format(num,pn))
            num+=1
        num_to_remove=input("Enter Number: ")
        print("{} REMOVED!".format(num_to_remove))
