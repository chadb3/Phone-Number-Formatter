from phoneNumber import *
class phoneNumberManager():
    def __init__(this):
        this._PN_LIST=[]
    def newPhoneNumber(this, pn_in):
        pn=Phone_Number(pn_in)
        this._PN_LIST.append(pn)
    def newRandomPhoneNumber(this):
        pn=Phone_Number()
        this._PN_LIST.append(pn.generateRandom())
    def debugTestPrintList(this):
        #debug test print.
        #may adjust to be actual at a later date.
        for phone_number in this._PN_LIST:
            print(phone_number)
    def detailedPrint(this):
        for pn in this._PN_LIST:
            pn.printPhoneNumber()