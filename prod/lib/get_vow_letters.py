from random import random
from get_rand_letter import *

def get_vow_letters(amt_and_let):
	rep = True
	
	while rep == True:
		i=0
		
		# how many vowels?
		
		if amt_and_let[0] == True:
			vowel_count = 2
		
		if amt_and_let[0] == False:
			vow_count_rand = random.random() * 2
			vow_count_rand_mod = vow_count_rand % 1
			vow_count_select = vow_count_rand-vow_count_rand_mod
			
			
	
			vowel_count = 0
			
			if vow_count_select == 1.0:
				vowel_count = 2
			if vow_count_select == 0.0:
				vowel_count = 3

		selection = [0] * vowel_count
		counter = 0
		
		for each in range(0,vowel_count):
			selection[i] = get_rand_letter('vow')
			i+=1
		
		# if center letter is vowel, check for no redundancies
		if amt_and_let[0] == True:
			for each in selection:
				if each[0] == amt_and_let[1]:
					while each[0] == amt_and_let[1]:
						each = get_rand_letter('vow')

		
		freqsum=0
		freqmean=0
		
		if vowel_count == 2:
			if selection[0] == selection[1]:
				while selection[0] == selection[1]:
					vow = random.random() * 5
					vowmod = vow % 1
					select = vow-vowmod
					select = int(select)
					selection[1] = get_rand_letter('vow')
			
		if vowel_count == 3:
			if selection[0] == selection[1] or selection[0] == selection[2] or selection[1] == selection[2]:
				while selection[0] == selection[1]:
					vow = random.random() * 5
					vowmod = vow % 1
					select = vow-vowmod
					select = int(select)
					selection[1] = get_rand_letter('vow')

				x = selection[0]
				y = selection[1]
				selection = [0] * 2
				selection = [x,y]
	
		
		for each in selection:
			freqsum += each[1]
		freqmean = freqsum/len(selection) 
		
		if freqmean > 8.5:
			rep=False
	
			
	return selection
	
if __name__ == "__main__":
	get_vow_letters(amt_and_let)