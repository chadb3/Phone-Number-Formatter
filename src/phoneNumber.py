import re
# import like see __init__.py
# Phone_Number class to store a "Phone Number" object.
class Phone_Number:
	def _getTranslatePhone(this,phoneNumIn):
		returnString = ""
		pdict = {"A":2,"B":2,"C":2,"D":3,"E":3,"F":3,"G":4,"H":4,"I":4,"J":5,"K":5,"L":5,"M":6,"N":6,"O":6,"P":7,"Q":7,"R":7,"S":7,"T":8,"U":8,"V":8,"W":9,"X":9,"Y":9,"Z":9}
		for i in range(0,len(phoneNumIn)):
			try:
				returnString+=str(pdict[phoneNumIn[i].upper()])
			except:
				returnString+=phoneNumIn[i]
		#print(returnString)
		return returnString
	def _getDigitsOnly(this,translatedPhoneNumberIn):
		retString = ""
		retString = re.sub(r"\D", "", translatedPhoneNumberIn)
		return retString
	def _getSplitDigits(this, theDigitsOnly):
		retArr = [] # [ 'country code', 'area code', 'cent. office code', 'line number']
		# Need to figure out how many digits the phone number is.
		# need to determine if Country Code is attached.
		# if 11 digits and a 1 is in front then it is following USA phone number schema.
		# I am only concerned for US based phone numbers for now.
		if(len(theDigitsOnly)==10):
			retArr.append("1")
			retArr.append(theDigitsOnly[:3])
			retArr.append(theDigitsOnly[3:6])
			retArr.append(theDigitsOnly[6:])
		elif(len(theDigitsOnly)==11 and theDigitsOnly[0]=='1'):
			retArr.append(theDigitsOnly[0:1])
			retArr.append(theDigitsOnly[1:4])
			retArr.append(theDigitsOnly[4:7])
			retArr.append(theDigitsOnly[7:])
		else:
			print("Error: Phone number segments not recoreded. Not A phone number.")
			for iiii in range(0,4):
				retArr.append("Not a Phone Number")
		return retArr
	def _getHumanReadable(this, phoneArrIn):
		strHumanReadable = "{}-{}-{}"
		#strHumanReadable=strHumanReadable.format(phoneArrIn[1],phoneArrIn[2],phoneArrIn[3])
		#print(strHumanReadable)
		return strHumanReadable.format(phoneArrIn[1],phoneArrIn[2],phoneArrIn[3])
	def _getPhoneNumberParts(this, PhoneNumberIn):
		#retArr = ["translated phone number, "digits only (no formatting)", "(country code) 1-US",[["555"],["555"],["0100"]], "human readable format","outgoing format (ex: 15555550111)"]
		retArr = []
		translatedPhone = this._getTranslatePhone(PhoneNumberIn)
		phoneNumOnlyDigits = this._getDigitsOnly(translatedPhone)
		phoneSegments = this._getSplitDigits(phoneNumOnlyDigits)
		humanReadable = this._getHumanReadable(phoneSegments)
		outgoingFormat = "1"+phoneNumOnlyDigits
		# return Array of Phone Number Segments for the Constructor
		retArr.append(translatedPhone)
		retArr.append(phoneNumOnlyDigits)
		retArr.append(phoneSegments)
		retArr.append(humanReadable)
		retArr.append(outgoingFormat)
		# return the array
		return retArr

	def __init__(this,phoneNumberIn):
		# getting the parts of the phone number for easy manipulation
		i = this._getPhoneNumberParts(phoneNumberIn)
		# Phone Number as entered after running through getPhoneNumberParts
		this.phone_number_as_entered=i[0]
		this.paste_friendly=i[1]
		# Segments of phone number
		this.country_code=i[2][0] # Country Code 1 for US
		this.area_code=i[2][1] # area Code
		this.central_office_code=i[2][2] # office code
		this.line_number=i[2][3] # line number
		# end of Segment
		# Human Readable 555-555-0100
		this.human_readable=i[3]
		# outgoing format 1+thedigits for copy paste to phone program.
		this.outgoingFormat = i[4]
		#this.translatePhone(phoneNumberIn)
		#print(i)
		i=0
	def printPhoneNumber(this):
		print("\nPhone Number AS ENTERED: {}\n\n\nPhone Number: {}\n\nHuman Readable: {}\n\nOutgoing Format: {}\n".format(this.phone_number_as_entered,this.paste_friendly,this.human_readable,this.outgoingFormat))

