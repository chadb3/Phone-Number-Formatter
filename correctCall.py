# needed for regex ( adding this comment as I didnt notice the date on this machine was wrong and I somehow now have commits on the 17th when this did not exist...)
import re

def translatePhone(phoneNumberIn):
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
	nullPhone(retPhoneStr)
# Takes in a "Phone Number"
def nullPhone(phoneNumberIn):
	# Prints the phone number in the before state
	print("Before: {}".format(phoneNumberIn))

	# Debug Length from before regex
	# print(len(phoneNumberIn))

	# uses regex to match digits (the \D) and make everything else blank (the "")
	newPhone = re.sub(r"\D", "", phoneNumberIn)
	# prints only the digits (0-9)
	# in other words, anything that wasn't a digit is destroyed.
	print("\nAfter: {}\n".format(newPhone))

# main calls the function currently called nullPhone (that removes everything that is not a digit).
def main():
	# now calls translate phone by default as it calls nullPhone as part of it.
	translatePhone(input("\nEnter Phone Number: "))
	return 0

if __name__ == "__main__":
	main()
