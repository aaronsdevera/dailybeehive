#from freq import freq
freq=[
	['e',12.702],
	['t',9.056],
	['a',8.167],
	['o',7.507],
	['i',6.966],
	['n',6.749],
	['s',6.327],
	['h',6.094],
	['r',5.987],
	['d',4.253],
	['l',4.025],
	['c',2.782],
	['u',2.758],
	['m',2.406],
	['w',2.361],
	['f',2.228],
	['g',2.015],
	['y',1.974],
	['p',1.929],
	['b',1.492],
	['v',0.978],
	['k',0.772],
	['j',0.153],
	['x',0.150],
	['q',0.095],
	['z',0.074]
]

cons=[
	['t',9.056],
	['n',6.749],
	['s',6.327],
	['h',6.094],
	['r',5.987],
	['d',4.253],
	['l',4.025],
	['c',2.782],
	['m',2.406],
	['w',2.361],
	['f',2.228],
	['g',2.015],
	['y',1.974],
	['p',1.929],
	['b',1.492],
	['v',0.978],
	['k',0.772],
	['j',0.153],
	['x',0.150],
	['q',0.095],
	['z',0.074]
]

vowels = [freq[0],freq[2],freq[3],freq[4],freq[12]]

import random


def get_rand_letter(type):
	if type == 'all':
		x = random.random() * 26
		xmod = x % 1
		select = int(x-xmod)
		all_letters = freq
		return all_letters[select]
		
	if type == 'vow':
		x = random.random() * 5
		xmod = x % 1
		select = int(x-xmod)
		return vowels[select]
		
	if type == 'cons':

		x = random.random() * 21
		xmod = x % 1
		select = int(x-xmod)
		return cons[select]


def get_cen_letter():
	rep = True
	
	while rep == True:
		i=0
		
		selection = get_rand_letter('all')
		
		if selection[1] > 0.9:
			rep = False
			
		return selection
		
		'''
		nofreq=0
		lowfreq=0
		midfreq=0
		
		selection = [get_rand_letter('all'),get_rand_letter('all'),get_rand_letter('all'),get_rand_letter('all'),get_rand_letter('all')]
		
		for each in selection:
			if each[1] > 0.0 and each[1] < 0.1:
				nofreq += 1
			if each[1] < 1:
				lowfreq += 1
			if each[1] < 2 and each[1] > 1:
				midfreq += 1
		
		freqsum=0
		freqmean=0
		
		for each in selection:
			freqsum += each[1]
		freqmean = freqsum/5 
		
		if freqmean < 2.78 and nofreq < 2 and lowfreq < 2 and midfreq < 3:
			rep = False
	
		cen_rand = random.random() * 5
		cen_rand_mod = cen_rand % 1
		cen_select = cen_rand-cen_rand_mod
		

		
		return selection[int(cen_select)]
		'''
		
		
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

	
def get_cons_letters(amt):
	rep = True
	while rep == True:
		i=0
		
		selection = [0] * amt
		
		for each in range(0,amt):
			selection[i] = get_rand_letter('cons')
			i+=1
			
		freqsum=0
		freqmean=0
		
		for each in selection:
			freqsum += each[1]
			
		freqmean = freqsum/len(selection) 
			
		
		if freqmean > 4.9:
			rep = False

	return selection

# MAIN
letter_total = 0
cons_count = 0
vow_count = 0
force_vow_amt = False

# Get center letter
center = get_cen_letter()
for each in vowels:
	if center[0] == each[0]:
		vow_count += 1
		force_vow_amt = [True, center[0]]
if vow_count == 0:
	cons_count += 1
	force_vow_amt = [False, center[0]]
letter_total += len(center)/2


# Get vowel letters
vowels = get_vow_letters(force_vow_amt)
vow_count += len(vowels)
letter_total += len(vowels)/1

# Get remaining letters
cons_count = 7-letter_total
consonants = get_cons_letters(cons_count)
letter_total += len(consonants)/1

print 'center: ' + str(center)
print 'vowels: ' + str(vowels)
print 'consonants: ' + str(consonants)
print 'letter total: ' + str(letter_total)
