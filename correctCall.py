# needed for regex (Regular Expression)
import re
# Called First.
# Removes Phonewords
# then calls nullPhone(may later rename) to remove formatting for easy copy paste to software that doesn't like it. 
def translatePhone(phoneNumberIn):
	humanReadable(phoneNumberIn)
	#stores if it the number was translated or not.
	bool_Required_translation = False
	#stores the updated phone number
	retPhoneStr = ""
	#Dictionary that holds each letter and its associated number for example pdict["A"]=2 and pdict["Z"]=9 
	pdict = {"A":2,"B":2,"C":2,"D":3,"E":3,"F":3,"G":4,"H":4,"I":4,"J":5,"K":5,"L":5,"M":6,"N":6,"O":6,"P":7,"Q":7,"R":7,"S":7,"T":8,"U":8,"V":8,"W":9,"X":9,"Y":9,"Z":9}
	#debug
	#print(len(phoneNumberIn))
	for i in range(0,len(phoneNumberIn)):
		try:
			#If possible, it converts the letter to number.
			retPhoneStr+=str(pdict[phoneNumberIn[i].upper()])
			bool_Required_translation = True
		except:
			#otherwise it just adds it to the string.
			retPhoneStr+=phoneNumberIn[i]
	if(bool_Required_translation):
		print("Required Translation: {}".format(bool_Required_translation))
		humanReadable(retPhoneStr)
	nullPhone(retPhoneStr)
	return 0
# Takes in a "Phone Number"
# Removes any formating from the phone number
# Leaving only the digits.
def nullPhone(phoneNumberIn):
	# Prints the phone number in the before state
	if(len(phoneNumberIn)>10):
		print("Before: {}".format(phoneNumberIn))
	# Debug Length from before regex
	# print(len(phoneNumberIn))
	# uses regex to match digits (the \D) and make everything else blank (the "")
	newPhone = re.sub(r"\D", "", phoneNumberIn)
	# prints only the digits (0-9)
	# in other words, anything that wasn't a digit is destroyed.
	print("\nAfter: {}\n".format(newPhone))
	return 0
# This will be responsible for printing a "Human Readable" phone number if one was not provided
# if 5552345678 was entered, then it will print "Human Readable: 555-234-5678"
# will also work with phone words. If "555ADGJMPT" was entered it will print "Human Readable: 555-ADG-JMPT"
def humanReadable(phoneNumberIn):
	humanReadbleNum=""
	if(len(phoneNumberIn)==10):
		for i in range(0,len(phoneNumberIn)):
			#print(phoneNumberIn[i],end="")
			humanReadbleNum+=phoneNumberIn[i]
			if(i==2 or i==5):
				#print("-",end="")
				humanReadbleNum+="-"
		print("Human Readable: {}\n".format(humanReadbleNum))
	return 0
# main calls the function currently called nullPhone (that removes everything that is not a digit).
def main():
	# now calls translate phone by default as it calls nullPhone as part of it.
	translatePhone(input("\nEnter Phone Number: "))
	return 0
if __name__ == "__main__":
	main()