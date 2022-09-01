from src.phoneNumberManager import phoneNumberManager
def main():
    a=phoneNumberManager()
    usrInput=""
    loopVal=True
    while(loopVal):
        usrInput=input("> ")
        a.newPhoneNumber(usrInput)
