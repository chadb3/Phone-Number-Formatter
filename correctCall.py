# needed for regex ( adding this comment as I didnt notice the date on this machine was wrong and I somehow now have commits on the 17th when this did not exist...)
import re

def translatePhone(phoneNumberIn):
	retPhone =[]
	retPhoneStr = "" 
	pdict = {"A":2,"B":2,"C":2,"D":3,"E":3,"F":3,"G":4,"H":4,"I":4,"J":5,"K":5,"L":5,"M":6,"N":6,"O":6,"P":7,"Q":7,"R":7,"S":7,"T":8,"U":8,"V":8,"W":9,"X":9,"Y":9,"Z":9}
	#debug
	#print(len(phoneNumberIn))
	for i in range(0,len(phoneNumberIn)):
		#print(phoneNumberIn[i],end="")
		try:
			retPhone.append(str(pdict[phoneNumberIn[i]]))
		except:
			retPhone.append(phoneNumberIn[i])
		retPhoneStr+=retPhone[i]
	#odd behavior
	#print("\nSTR: {}\nCorrected: {}".format(retPhoneStr, nullPhone(retPhoneStr)))
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
	print("\nAfter: "+newPhone)

# main calls the function currently called nullPhone (that removes everything that is not a digit).
def main():
	choice=input("One: Translate\tTwo: Remove Formatting\nChoice: ")
	# nullPhone takes in an a user input as a "Phone Number".
	if(choice.lower()=="two"):
		nullPhone(input("Enter Phone Number: "))
	if(choice.lower()=="one"):
		translatePhone(input("Enter Phone Number: "))
	return 0

if __name__ == "__main__":
	main()
