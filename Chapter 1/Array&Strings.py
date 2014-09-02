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

def premutation(s1,s2):
	directory = list(s2)
	for i in s1:
		for d in s2:
			if i == d:
				print True
	return False
	
premutation("fdf","god")		
