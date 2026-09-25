# Q12.0 Which of the following correctly returns whether char is a vowel?

# A
# def isVowel(char):
# 	for letter in "aeiou":
# 		if letter == char:
# 			return True
# 	return False

# B
# def isVowel(char):
# 	for letter in "aeiou":
# 		if letter == char:
# 			return True
# 	return False

# C
def isVowel(char):
	return char == "a" or char == "e" or char == "i" or char == "o" or char == "u"
  # return char == ("a" or "e" or "i" or "o" or "u")

print("a", isVowel("a")) # True
# Insert more test cases here!
print("i", isVowel("i")) # True
print("u", isVowel("u")) # True
print("b", isVowel("b")) # False
print(3, isVowel(3)) # False