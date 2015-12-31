import random
from freq import freq
from cons import cons
from lib_vowels import lib_vowels

def get_rand_letter(type):
	if type == 'all':
		x = random.random() * 26
		xmod = x % 1
		select = int(x-xmod)
		all_letters = freq
		selection = all_letters[select]
		
	if type == 'vow':
		x = random.random() * 5
		xmod = x % 1
		select = int(x-xmod)
		selection = lib_vowels[select]
		
	if type == 'cons':

		x = random.random() * 21
		xmod = x % 1
		select = int(x-xmod)
		selection = cons[select]
	return selection

if __name__ == '__main__':
	get_rand_letter(type)