import re
from random import randint
import sqlite3
#from src.phoneSQLHelper import *
#
class PhoneNumberDB:
	def __init__(this):
		this.DATABASEFILE="data/PNDB.sqlite3"
		this.MODE="?mode=rw"
		this._URI=True
		#this.sql_connection=sqlite3.connect(this.DATABASEFILE+this.MODE,this._URI)
	def SELECT_STATE_FROM_US_STATES_WHERE_STATE_ABBR_IS(this, ITEM_IN):
		retVal=""
		con=sqlite3.connect(this.DATABASEFILE)
		sqlCursor=con.execute("SELECT STATE FROM US_STATES WHERE STATE_ABBR='{}'".format(ITEM_IN))
		try:
			retVal=sqlCursor.fetchone()
		except Exception as EX:
			print(EX)
		return retVal
	def SELECT_PHONE_NUMBER(this,ID_IN):
		None
	def SELECT_STATE_FROM_USA_AREA_CODE(this,ITEM_IN):
		retVal=None
		con=sqlite3.connect(this.DATABASEFILE)
		sqlCursor=con.execute("SELECT STATE from USA_AREA_CODES where AREA_CODE='{}'".format(ITEM_IN))
		try:
			#debug
			#print("SELECT STATE FROM AREA CODE HIT")
			retVal=sqlCursor.fetchone()
			#debug
			#print(retVal)
			return retVal[0]
		except Exception as ex:
			print("Issue in SELECT_STATE_FROM_USA_AREA_CODE")
			print(ex)
			return retVal
		None
	def SELECT_ALL_AREA_CODES_AND_STATE_ABBR(this):
		con=sqlite3.connect(this.DATABASEFILE)#+this.MODE,this._URI) look into why this doesn't work, or if it is even needed at all...
		sqlCursor=con.execute("SELECT * FROM USA_AREA_CODES")
		try:
			retList=sqlCursor.fetchall()
			con.close()
			return retList
		except Exception as ex:
			print(ex)
			print("\n\nIssue: SELECT * FROM USA_AREA_CODES - Did Not Work!\n\n")
			con.close()
			return []
		print("(^: <-> if you see this something is wrong in \"SELECT_ALL_AREA_CODES_AND_STATE_ABBR\"")
		
	def TEST_SELECT_STATE(this):
		print("if you are not working directly inside src this might not work...")
		con=sqlite3.connect("testDB.sqlite3")
		#state=con.execute("SELECT STATE FROM US_STATES WHERE ID=1") #111=None
		state=con.execute("SELECT * FROM US_STATES")
		print(state)
		print("SELECT * FROM US_STATES")
		try:
			a=state.fetchall()
			print("STATEs: {}".format(a)) #.fetchone()[0]
			print(type(a))
			print(a[0][0])
			print(a[0][1])
			print(a[0][2])
		except Exception as k:
			print(k)
		con.close()
#################################################################################################################################################################################

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
			this.isPhoneNumber = False
			# DEBUG PRINT
			#print("Error: Phone number segments not recoreded. Not A phone number.")
			for iiii in range(0,4):
				#print("NAN Debug: {}".format(theDigitsOnly))
				retArr.append("Not a Phone Number")
		return retArr
	def _getHumanReadable(this, phoneArrIn):
		strHumanReadable = "{}-{}-{}"
		#strHumanReadable=strHumanReadable.format(phoneArrIn[1],phoneArrIn[2],phoneArrIn[3])
		#print(strHumanReadable)
		return strHumanReadable.format(phoneArrIn[1],phoneArrIn[2],phoneArrIn[3])
	def _getCtrlcCtrlv(this, phoneArrIn):
		strCopyPaste = "{}{}{}"
		return strCopyPaste.format(phoneArrIn[1],phoneArrIn[2],phoneArrIn[3])
	def _getPhoneNumberParts(this, PhoneNumberIn):
		#retArr = ["translated phone number, "digits only (no formatting)", "(country code) 1-US",[["555"],["555"],["0100"]], "human readable format","outgoing format (ex: 15555550111)"]
		retArr = []
		translatedPhone = this._getTranslatePhone(PhoneNumberIn)
		phoneNumOnlyDigits = this._getDigitsOnly(translatedPhone)
		phoneSegments = this._getSplitDigits(phoneNumOnlyDigits)
		humanReadable = this._getHumanReadable(phoneSegments)
		copyPaste = this._getCtrlcCtrlv(phoneSegments)
		outgoingFormat = "+1"+copyPaste
		# return Array of Phone Number Segments for the Constructor
		retArr.append(translatedPhone)
		retArr.append(copyPaste)
		retArr.append(phoneSegments)
		retArr.append(humanReadable)
		retArr.append(outgoingFormat)
		# return the array
		return retArr
	def _printInDashes(this, thing_to_print):
		dash = ''
		for i in range(0,len(thing_to_print)+6):
			dash+='-'
		print("{}\n|| {} ||\n{} ".format(dash,thing_to_print,dash))
		#print("len i (func test): {}".format(i))
		return 0
	def buildAreaCodeDictionary(this):
		retVal={}
		#this._testAreaCodeList
		for item in this._areaCode2:
			retVal[item[0]]=(item[1])
			#retVal.append("{}:{}".format(item[0],item[1]))
			#print("Debug:{}:\'{}\'".format(item[0],item[1]))
		#print("EXIT")
		#print(retVal)
		return retVal
		
	def __init__(this,phoneNumberIn="1 000-000-0000"):
		this.Phone_Database=PhoneNumberDB()
		this._areaCode2=this.Phone_Database.SELECT_ALL_AREA_CODES_AND_STATE_ABBR()
		#debug
		#print(this._areaCode2)
		this._testAreaCodeList= this.buildAreaCodeDictionary()
		this._testStateList = ""#{"AL":"Alabama", "AK":"Alaska","AZ":"Arizona","AR":"Arkansas", "CA":"California","CO":"Colorado","CT":"Connecticut","DE":"Delaware","DC":"District Of Columbia","FL":"Florida", "GA":"Georgia", "HI":"Hawaii","ID":"Idaho", "IN":"Indiana", "IA":"Iowa","IL":"Illinois","KS":"Kansas","KY":"Kentucky", "LA":"Louisiana","ME":"Maine","MD":"Maryland", "MA":"Massachusetts","MI":"Michigan","MN":"Minnesota","MS":"Mississippi","MO":"Missouri","MT":"Montana","NE":"Nebraska","NV":"Nevada","NH":"New Hampshire","NJ":"New Jersey", "NM":"New Mexico", "NY":"New York", "NC":"North Carolina", "ND":"North Dakota", "OH":"Ohio", "OK":"Oklahoma","OR":"Oregon", "PA":"Pennsylvania", "RI":"Rhode Island", "SC":"South Carolina", "SD":"South Dakota", "TN":"Tennessee","TX":"Texas","UT":"Utah","VT":"Vermont","VA":"Virginia", "WA":"Washington","WV":"West Virginia","WI":"Wisconsin","WY":"Wyoming" }
		this.isPhoneNumber=True
		this.phoneExtension = ""
		# need to split out most of the below to their own functions
		# getting the parts of the phone number for easy manipulation
		i = this._getPhoneNumberParts(phoneNumberIn)
		# Phone Number as entered after running through getPhoneNumberParts
		# have to pass "phoneNumberIn" as otherwise it is already translated...
		this.phone_number_as_entered=phoneNumberIn#i[0]
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
		# used for noting things like if you need to ask for someone.
		# (like if it is a main line for a business)
		# use of extensions
		this.phoneNumberNotes=[]
		# cell, work, home, etc.
		this.phoneNumberType=""


	def printPhoneNumber(this):
		print("")
		#dash = ""
		if(this.isPhoneNumber):
			if( len(this.phoneExtension)==0):
				#print("\n")
				this._printInDashes("Phone Number as entered: "+this.phone_number_as_entered)
				print("\n\n  Phone Number: {}\n\n  Human Readable: {}\n\n  Outgoing Format: {}".format(this.paste_friendly,this.human_readable,this.outgoingFormat))
				this.checkAreaCode()
			elif(len(this.phoneExtension)>0):
				print("  Phone Number with Extension !")
				this._printInDashes("Phone Number As Entered: "+this.phone_number_as_entered)
				print("\n\n  Phone Number: {} \n  Extension: {}".format(this.paste_friendly,this.phoneExtension[5:]))
				print("\n  Human Readable: {} {}".format(this.human_readable,this.phoneExtension))
				print("\n  Outgoing Format: {} ---- {}".format(this.outgoingFormat,this.phoneExtension))
				this.checkAreaCode()
		else:
			NAPN="- NOT A PHONE NUMBER -"
			this._printInDashes(NAPN)
			this._printInDashes(this.phone_number_as_entered)
			this._printInDashes(NAPN)
		print("")
		return 0
	def getPhoneNumber(this):
		return [this.country_code,this.area_code,this.central_office_code,this.line_number]
	def addExtension(this, extensionStr):
		if(len(extensionStr)>0):
			this.phoneExtension="Ext: "+extensionStr
			return 0
		return 0
# starting work on this
# should print the state the area code is part of
# working on getting a list of area codes and their associated states.
	def checkAreaCode2(this):
		#this._printInDashes("Checking Area Code:")
		# see source in data file.
		# looking at creating that list programmatically or creating and using a DB
		# still just US States and not any Territories yet
		#testAreaCodeList = {201:"NJ", 202:"DC", 203:"CT",205:"AL", 206:"WA",207:"ME",208:"ID"}
		# finsihed list of states. (Still just a test)
		# Still might use a DB in the data file
		state =""
		try:
			statAbbr = this._testAreaCodeList[int(this.area_code)]
			try:
				state = this._testStateList[statAbbr]
				print("  State: {} ({})".format(state,statAbbr))	
			except:
			#	state = "Not In List"
				print("  Country or Territory: {} ".format(statAbbr))
		except:
			print("  Not found or added to list yet")
		print("")
		return state
	# checkAreaCode but uses db rather than a dictionary. 
	def checkAreaCode(this):
		state=""
		full_state=""
		try:
			state=this.Phone_Database.SELECT_STATE_FROM_USA_AREA_CODE(this.area_code)
			if(state!=None):
				print("  STATE: {}".format(state))
			else:
				print("State/location not in database")
		except:
			print("issue with database in checkAreaCode")
		None
	# Generates a phone number in the fictional range.
	# note: this follows everyone following the North American plan, and has places in Canada and other Territories. 
	def createFictionalPhoneNumber(this):
		areaCodeList = list(this._testAreaCodeList.keys())
		MAX=len(areaCodeList)-1
		index=randint(0,MAX)
		areaCode = str(areaCodeList[index])
		centOfficeCode=str(555)
		lineNumber = "0"+str(randint(100,199))
		#print(areaCode+centOfficeCode+lineNumber)
		# use GUI to cut and paste to constructor ...
		# keys = list(testAreaCodeList.keys())
		return Phone_Number(areaCode+centOfficeCode+lineNumber)
	def __str__(this):
		if(this.isPhoneNumber):
			return "{}-{}-{}".format(this.area_code,this.central_office_code,this.line_number)
		else:
			#debug
			#print("NaN Debug: ".format(this.phone_number_as_entered))
			#/debug
			return "Not a Phone Number"
	# Don't know why you would need this. But I added it...
	def __int__(this):
		if(this.isPhoneNumber):
			return int("{}{}{}".format(this.area_code,this.central_office_code,this.line_number))
		else:
			return 0
	# This is so you can use hex() and oct () as overriding hex like __hex__(self): did not work
	def __index__(this):
		return int(this)
	def __getitem__(this, index):
		return this.paste_friendly[index]
	# need to review code above. generated phone numbers can generate a "Not A Phone Number..."
	# __setitem__and __delitem__
	def generateRandom(this):
		areaCodeList = list(this._testAreaCodeList.keys())
		MAX=len(areaCodeList)-1
		index=randint(0,MAX)
		areaCode = str(areaCodeList[index])
		Code=randint(1,999)
		#print(Code) #debug
		if(Code<10):
			tmp="00"+str(Code)
			Code=tmp
		elif(Code>=10 and Code<=99):
			tmp="0"+str(Code)
			Code=tmp
		else:
			#print("TEST HIT: {}".format(Code)) #debug
			Code=str(Code)
		LineNumber=randint(1,9999)
		tmpLN=""
		if(LineNumber<10):
			tmpLN="000"+str(LineNumber)
		elif(LineNumber>=10 and LineNumber <=99):
			tmpLN="00"+str(LineNumber)
		elif(LineNumber>=99 and LineNumber<1000):
			tmpLN="0"+str(LineNumber)
		else:
			tmpLN=str(LineNumber)
		LineNumber=tmpLN
		return Phone_Number(areaCode+Code+LineNumber)
	def checkDistance(this, phoneNumIn):
		print("Checking Distance: ")
		# use datastructure too see how many states are between...
		# Still working on this...
		if(this.area_code==phoneNumIn.area_code):
			print("  Local")
		elif(this.checkAreaCode()==phoneNumIn.checkAreaCode()):
			print("  Same State")
		else:
			print("  Not Same State")
	def genPhoneNumberFromSpecificPlace(this, place):
		#print("Generating phone number from: {} (WIP)".format(place))
		listOfAreaCodes=[]
		for i in this._testAreaCodeList:
			if(this._testAreaCodeList[i]==place):
				listOfAreaCodes.append(i)
				#print(listOfAreaCodes)
		if(len(listOfAreaCodes)==0):
			return Phone_Number()
		index=randint(0,len(listOfAreaCodes)-1)
		#print("index: {}".format(index))
		return Phone_Number(str(listOfAreaCodes[index])+this.genRandV2(3)+this.genRandV2(4))
	#instead of the above with 2 separate functions
	# now you will pass the number of digits to generate
	def genRandV2(this, numDigits):
		#print("V2 version of gen random.") #gets called based off number of times it is called
		retNumber=0
		retString=""
		randIntArray=[]
		for i in range(0,numDigits):
			randIntArray.append(randint(0,9))
		#aMax=""
		#for i in range(0,numDigits):
			#aMax+="9"
		#retNumber=randint(1,int(aMax))
		#print(retNumber)
		#print(randIntArray)
		for i in range(0,numDigits):
			retString+=str(randIntArray[i])
		#print(retString)
		return retString

	def addNotes(this, note):
		appNote=str(note)
		#noting here so I don't have to scroll up so far for now.
		#this.phoneNumberNotes=""
		# cell, work, home, etc.
		#this.phoneNumberType=""
		this.phoneNumberNotes.append(appNote)
	# input managed by the phoneNumberManager
	def addPhoneNumberType(this, typeIn):
		this.phoneNumberType=typeIn
	def printNotes(this):
		for note in this.phoneNumberNotes:
			print(note)
	def printType(this):
		print(this.phoneNumberType)
	def simplePrint(this):
		# still need to edit this down in the extension section once I added to v2
		#print("P")
		#dash = ""
		if(this.isPhoneNumber):
			if( len(this.phoneExtension)==0):
				#print("\n")
				#this._printInDashes("Phone Number as entered: "+this.phone_number_as_entered)
				print("\n  Phone Number: {}\n  Number W Dashes: {}\n  Outgoing Format: {}".format(this.paste_friendly,this.human_readable,this.outgoingFormat))
				this.checkAreaCode()
			elif(len(this.phoneExtension)>0):
				print("  Phone Number with Extension !")
				#this._printInDashes("Phone Number As Entered: "+this.phone_number_as_entered)
				print("\n\n  Phone Number: {} \n  Extension: {}".format(this.paste_friendly,this.phoneExtension[5:]))
				print("\n  Human Readable: {} {}".format(this.human_readable,this.phoneExtension))
				print("\n  Outgoing Format: {} ---- {}".format(this.outgoingFormat,this.phoneExtension))
				this.checkAreaCode()
		else:
			NAPN="- NOT A PHONE NUMBER -"
			this._printInDashes(NAPN)
			this._printInDashes(this.phone_number_as_entered)
			this._printInDashes(NAPN)
		#print("")
		return 0

#####################################################################################################################################################################
# phone number object
#import importlib pep320ex omniproc
#import importlib
#PNF=importlib.import_module("Phone-Number-Formatter")
#from pickle import NONE
#from src.phoneNumber import Phone_Number
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
