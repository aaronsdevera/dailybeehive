from freq import freq

cons1 = ['w','h','m','r']
cons2 = ['y','t','r']
cons3 = ['t','c','l','f']
cons4 = ['f','l','q','d']
cons5 = ['t','r','n','c']
cons6 = ['t','c','n']
cons7 = ['r','l','m','n']

vow1 = ['o','e']
vow2 = ['a','i','u']
vow3 = ['a','e']
vow4 = ['e','i']
vow5 = ['a','i']
vow6 = ['a','o','i']
vow7 = ['a','o']


def find_mean_freq(char_list):
	i=0
	freqsum = 0
	freqmean = 0
	
	
	
	char_list_freq = [0] * len(char_list)
	
	for each in char_list:
		for every in freq:
			if each[0] == every[0]:
				char_list_freq[i] = every
		i+=1
	print char_list_freq
	
	for each in char_list_freq:
		freqsum += each[1]
		freqmean = freqsum/len(char_list)
		
	return freqmean
				
print  (find_mean_freq(cons1)+ find_mean_freq(cons2)+ find_mean_freq(cons3)+ find_mean_freq(cons4)+ find_mean_freq(cons5)+ find_mean_freq(cons6)+ find_mean_freq(cons7))/7

# max avg cons freq at 4.9

print  (find_mean_freq(vow1)+ find_mean_freq(vow2)+ find_mean_freq(vow3)+ find_mean_freq(vow4)+ find_mean_freq(vow5)+ find_mean_freq(vow6)+ find_mean_freq(vow7))/7

# max avg vow freq at 8.5