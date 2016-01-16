from get_rand_letter import *

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
	
if __name__ == "__main__":
	get_cons_letters(amt)