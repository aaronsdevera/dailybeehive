from get_rand_letter import *


def get_cen_letter():
	rep = True
	
	while rep == True:
		i=0
		
		selection = get_rand_letter('all')
		
		if selection[1] > 0.9:
			rep = False
			
		return selection
		
if __name__ == "__main__":
	get_cen_letter()