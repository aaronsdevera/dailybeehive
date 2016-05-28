import sys

args = sys.argv

word = args[1]

letters = args[2:]

def find_super_words(word,letters):
	all_letters_fulfilled = [False,False,False,False,False,False,False]

	#print letters
	#print word

	for each in range(len(letters)):
		if word.count(letters[each]) >= 1:
			all_letters_fulfilled[each] = True
	
	print all_letters_fulfilled
	print all(all_letters_fulfilled)
	
	
	if all(all_letters_fulfilled) and all_letters_fulfilled[0] == True:
		return word

print find_super_words(word,letters)
