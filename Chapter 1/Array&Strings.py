#1.1 implement an algorthiem to determine if the string has all unique characters. What if you cannot use additional data structure?
#Number of Unique Characters are 256
def isUniqueCharacter(s):
	ucharacter = set()	
	for c in s:
		if c in ucharacter:
			return False
		ucharacter.add(c)		
	return True
#1.2 implement a function void reverse(char*str) in C or C++ which reverse a null terminate string
def reverse(s):
	m = ""
	lengthOfString = len(s)

	for i in range(0,lengthOfString):
		m +=s[lengthOfString-1]
		lengthOfString -=1
	print m
	
reverse("Hello")			

#1.3 Given two string. write a method to decide if one is the premutation of the others
#Not Being able to use any data Structure 

def premutation(s1,s2):
	directory = list(s2)
	for i in s1:
		if i in directory:
			directory.remove(i)
	if len(directory) == 0:
		print True
	else:
		print False			
	

premutation("dog","god")

#Using DataStructure

#1.4 
#Using replace Function! Cheating 
def Space_Replacer(s, lengthOfString):
	m = s.replace(" ","%2")
	print m

#using 	
Space_Replacer("Mr John Smith ", 13)		


# using a list to store each char and change space to '%20', then join list into a string
def replaceSpace(string):
	charList = []
	for char in string:
		if char == ' ':
			char = '%20'
		charList.append(char)
	return ''.join(charList)

#test
inputStr = " Smith    q m "
expectOutput = "%20Smith%20%20%20%20q%20m%20"
if replaceSpace(inputStr) == expectOutput:
	print "test passed"
else:
	print "test failed"			
