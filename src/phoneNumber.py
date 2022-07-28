import re
# import like
# from src import phoneNumber
class Phone_Number:
	def translatePhone(this,phoneNumIn):
		returnString = ""
		pdict = {"A":2,"B":2,"C":2,"D":3,"E":3,"F":3,"G":4,"H":4,"I":4,"J":5,"K":5,"L":5,"M":6,"N":6,"O":6,"P":7,"Q":7,"R":7,"S":7,"T":8,"U":8,"V":8,"W":9,"X":9,"Y":9,"Z":9}
		for i in range(0,len(phoneNumIn)):
			try:
				returnString+=str(pdict[phoneNumIn[i].upper()])
			except:
				returnString+=phoneNumIn[i]
		print(returnString)
	def getPhoneNumberParts(this, PhoneNumberIn):
		print(len(PhoneNumberIn))

	def __init__(this,phoneNumberIn):
		this.phone_number_as_entered=phoneNumberIn
		this.country_code=""
		this.area_code=""
		this.central_office_code=""
		this.line_number=""
		this.getPhoneNumberParts(phoneNumberIn)
		this.translatePhone(phoneNumberIn)

