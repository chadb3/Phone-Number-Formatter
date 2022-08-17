import re
from random import randint
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
		outgoingFormat = "1"+copyPaste
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

	def __init__(this,phoneNumberIn="1 000-000-0000"):
		this._testAreaCodeList = {201:"NJ",202:"DC",203:"CT",204:"MANITOBA",205:"AL",206:"WA",207:"ME",208:"ID",209:"CA",210:"TX",212:"NY",213:"CA",214:"TX",215:"PA",216:"OH",217:"IL",218:"MN",219:"IN",220:"OH",223:"PA",224:"IL",225:"LA",226:"ONTARIO",228:"MS",229:"GA",231:"MI",234:"OH",236:"BRITISH COLUMBIA",239:"FL",240:"MD",242:"BAHAMAS",246:"BARBADOS",248:"MI",249:"ONTARIO",250:"BRITISH COLUMBIA",251:"AL",252:"NC",253:"WA",254:"TX",256:"AL",260:"IN",262:"WI",264:"ANGUILLA",267:"PA",268:"ANTIGUA/BARBUDA",269:"MI",270:"KY",272:"PA",276:"VA",279:"CA",281:"TX",284:"BRITISH VIRGIN ISLANDS",289:"ONTARIO",301:"MD",302:"DE",303:"CO",304:"WV",305:"FL",306:"SASKATCHEWAN",307:"WY",308:"NE",309:"IL",310:"CA",312:"IL",313:"MI",314:"MO",315:"NY",316:"KS",317:"IN",318:"LA",319:"IA",320:"MN",321:"FL",323:"CA",325:"TX",326:"OH",330:"OH",331:"IL",332:"NY",334:"AL",336:"NC",337:"LA",339:"MA",340:"USVI",341:"CA",343:"ONTARIO",345:"CAYMAN ISLANDS",346:"TX",347:"NY",351:"MA",352:"FL",360:"WA",361:"TX",364:"KY",365:"ONTARIO",367:"QUEBEC",368:"ALBERTA",380:"OH",385:"UT",386:"FL",401:"RI",402:"NE",403:"ALBERTA",404:"GA",405:"OK",406:"MT",407:"FL",408:"CA",409:"TX",410:"MD",412:"PA",413:"MA",414:"WI",415:"CA",416:"ONTARIO",417:"MO",418:"QUEBEC",419:"OH",423:"TN",424:"CA",425:"WA",430:"TX",431:"MANITOBA",432:"TX",434:"VA",435:"UT",437:"ONTARIO",438:"QUEBEC",440:"OH",441:"BERMUDA",442:"CA",443:"MD",445:"PA",447:"IL",448:"FL",450:"QUEBEC",458:"OR",463:"IN",464:"IL",469:"TX",470:"GA",473:"GRENADA",474:"SASKATCHEWAN",475:"CT",478:"GA",479:"AR",480:"AZ",484:"PA",501:"AR",502:"KY",503:"OR",504:"LA",505:"NM",506:"NEW BRUNSWICK",507:"MN",508:"MA",509:"WA",510:"CA",512:"TX",513:"OH",514:"QUEBEC",515:"IA",516:"NY",517:"MI",518:"NY",519:"ONTARIO",520:"AZ",530:"CA",531:"NE",534:"WI",539:"OK",540:"VA",541:"OR",548:"ONTARIO",551:"NJ",559:"CA",561:"FL",562:"CA",563:"IA",564:"WA",567:"OH",570:"PA",571:"VA",572:"OK",573:"MO",574:"IN",575:"NM",579:"QUEBEC",580:"OK",581:"QUEBEC",582:"PA",585:"NY",586:"MI",587:"ALBERTA",601:"MS",602:"AZ",603:"NH",604:"BRITISH COLUMBIA",605:"SD",606:"KY",607:"NY",608:"WI",609:"NJ",610:"PA",612:"MN",613:"ONTARIO",614:"OH",615:"TN",616:"MI",617:"MA",618:"IL",619:"CA",620:"KS",623:"AZ",626:"CA",628:"CA",629:"TN",630:"IL",631:"NY",636:"MO",639:"SASKATCHEWAN",640:"NJ",641:"IA",646:"NY",647:"ONTARIO",649:"TURKS & CAICOS ISLANDS",650:"CA",651:"MN",656:"FL",657:"CA",658:"JAMAICA",659:"AL",660:"MO",661:"CA",662:"MS",664:"MONTSERRAT",667:"MD",669:"CA",670:"CNMI",671:"GU",672:"BRITISH COLUMBIA",678:"GA",680:"NY",681:"WV",682:"TX",683:"ONTARIO",684:"AS",689:"FL",701:"ND",702:"NV",703:"VA",704:"NC",705:"ONTARIO",706:"GA",707:"CA",708:"IL",709:"NEWFOUNDLAND AND LABRADOR",712:"IA",713:"TX",714:"CA",715:"WI",716:"NY",717:"PA",718:"NY",719:"CO",720:"CO",721:"SINT MAARTEN",724:"PA",725:"NV",726:"TX",727:"FL",731:"TN",732:"NJ",734:"MI",737:"TX",740:"OH",742:"ONTARIO",743:"NC",747:"CA",753:"ONTARIO",754:"FL",757:"VA",758:"ST. LUCIA",760:"CA",762:"GA",763:"MN",765:"IN",767:"DOMINICA",769:"MS",770:"GA",771:"DC",772:"FL",773:"IL",774:"MA",775:"NV",778:"BRITISH COLUMBIA",779:"IL",780:"ALBERTA",781:"MA",782:"NOVA SCOTIA - PRINCE EDWARD ISLAND",784:"ST. VINCENT & GRENADINES",785:"KS",786:"FL",787:"PUERTO RICO",801:"UT",802:"VT",803:"SC",804:"VA",805:"CA",806:"TX",807:"ONTARIO",808:"HI",809:"DOMINICAN REPUBLIC",810:"MI",812:"IN",813:"FL",814:"PA",815:"IL",816:"MO",817:"TX",818:"CA",819:"QUEBEC",820:"CA",825:"ALBERTA",826:"VA",828:"NC",829:"DOMINICAN REPUBLIC",830:"TX",831:"CA",832:"TX",838:"NY",839:"SC",840:"CA",843:"SC",845:"NY",847:"IL",848:"NJ",849:"DOMINICAN REPUBLIC",850:"FL",854:"SC",856:"NJ",857:"MA",858:"CA",859:"KY",860:"CT",862:"NJ",863:"FL",864:"SC",865:"TN",867:"YUKON-NW TERR. - NUNAVUT",868:"TRINIDAD & TOBAGO",869:"ST. KITTS & NEVIS",870:"AR",872:"IL",873:"QUEBEC",876:"JAMAICA",878:"PA",901:"TN",902:"NOVA SCOTIA - PRINCE EDWARD ISLAND",903:"TX",904:"FL",905:"ONTARIO",906:"MI",907:"AK",908:"NJ",909:"CA",910:"NC",912:"GA",913:"KS",914:"NY",915:"TX",916:"CA",917:"NY",918:"OK",919:"NC",920:"WI",925:"CA",928:"AZ",929:"NY",930:"IN",931:"TN",934:"NY",936:"TX",937:"OH",938:"AL",939:"PUERTO RICO",940:"TX",941:"FL",943:"GA",945:"TX",947:"MI",948:"VA",949:"CA",951:"CA",952:"MN",954:"FL",956:"TX",959:"CT",970:"CO",971:"OR",972:"TX",973:"NJ",978:"MA",979:"TX",980:"NC",983:"CO",984:"NC",985:"LA",986:"ID",989:"MI", 888:"Toll Free"}
		this._testStateList = {"AL":"Alabama", "AK":"Alaska","AZ":"Arizona","AR":"Arkansas", "CA":"California","CO":"Colorado","CT":"Connecticut","DE":"Delaware","DC":"District Of Columbia","FL":"Florida", "GA":"Georgia", "HI":"Hawaii","ID":"Idaho", "IN":"Indiana", "IA":"Iowa","IL":"Illinois","KS":"Kansas","KY":"Kentucky", "LA":"Louisiana","ME":"Maine","MD":"Maryland", "MA":"Massachusetts","MI":"Michigan","MN":"Minnesota","MS":"Mississippi","MO":"Missouri","MT":"Montana","NE":"Nebraska","NV":"Nevada","NH":"New Hampshire","NJ":"New Jersey", "NM":"New Mexico", "NY":"New York", "NC":"North Carolina", "ND":"North Dakota", "OH":"Ohio", "OK":"Oklahoma","OR":"Oregon", "PA":"Pennsylvania", "RI":"Rhode Island", "SC":"South Carolina", "SD":"South Dakota", "TN":"Tennessee","TX":"Texas","UT":"Utah","VT":"Vermont","VA":"Virginia", "WA":"Washington","WV":"West Virginia","WI":"Wisconsin","WY":"Wyoming" }
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
	def printPhoneNumber(this):
		print("")
		#dash = ""
		if(this.isPhoneNumber):
			#for i in range(0,len(this.phone_number_as_entered)+len(" Phone Number AS ENTERED: {}")+2):
				#dash+="-"
				#print("-",end='')
			#print("---- i: {}".format(i))
			if( len(this.phoneExtension)==0):
				#print("\n")
				this._printInDashes("Phone Number as entered: "+this.phone_number_as_entered)
				print("\n\n  Phone Number: {}\n\n  Human Readable: {}\n\n  Outgoing Format: {}".format(this.paste_friendly,this.human_readable,this.outgoingFormat))
				#print("{}\n|| Phone Number AS ENTERED: {}||\n{}\n\n  Phone Number: {}\n\n  Human Readable: {}\n\n  Outgoing Format: {}\n\n".format(dash,this.phone_number_as_entered,dash,this.paste_friendly,this.human_readable,this.outgoingFormat))
			elif(len(this.phoneExtension)>0):
				print("  Phone Number with Extension !")
				this._printInDashes("Phone Number As Entered: "+this.phone_number_as_entered)
				#print("\n{}\n|| Phone Number As Entered: {} ||\n{}".format(dash,this.phone_number_as_entered,dash))
				print("\n\n  Phone Number: {} \n  Extension: {}".format(this.paste_friendly,this.phoneExtension[5:]))
				print("\n  Human Readable: {} {}".format(this.human_readable,this.phoneExtension))
				print("\n  Outgoing Format: {} ---- {}".format(this.outgoingFormat,this.phoneExtension))
		else:
			NAPN="- NOT A PHONE NUMBER -"
			#for i in range(0,len(NAPN)):
				#dash+="-"
			this._printInDashes(NAPN)
			this._printInDashes(this.phone_number_as_entered)
			this._printInDashes(NAPN)
			#print("{}\n{}\n{}\n\t".format(dash,NAPN,dash))
		#print("\n") was adding 2 spaces... I only wanted one
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
	def checkAreaCode(this):
		#this._printInDashes("Checking Area Code:")
		# see source in data file.
		# looking at creating that list programmatically or creating and using a DB
		# still just US States and not any Territories yet
		#testAreaCodeList = {201:"NJ", 202:"DC", 203:"CT",205:"AL", 206:"WA",207:"ME",208:"ID"}
		# finsihed list of states. (Still just a test)
		# Still might use a DB in the data file
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
		return 0
	# Generates a phone number in the fictional range.
	# note: this follows everyone following the North American plan, and has places in Canada and other Territories. 
	def createFictionalPhoneNumber(this):
		#print("asdf")
		#print("area code")
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
	# need the below too Maybe
	# __setitem__and __delitem__
	def generateRandom(this):
		areaCodeList = list(this._testAreaCodeList.keys())
		MAX=len(areaCodeList)-1
		index=randint(0,MAX)
		areaCode = str(areaCodeList[index])
		Code=str(randint(111,999))
		LineNumber=str(randint(1111,9999))
		return Phone_Number(areaCode+Code+LineNumber)
	def checkDistance(this, phoneNumIn):
		print("Checking Distance: ")
		# use datastructure too see how many states are between...
		# Still working on this.
		if(this.area_code==phoneNumIn.area_code):
			print(" Local")
		else:
			print(" Not Local")