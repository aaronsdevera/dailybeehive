from get_rand_letter import *
from get_cen_letter import *
from get_vow_letters import *
from get_cons_letters import *
from check_letter import *
from lib_vowels import lib_vowels as vowels
 
def generate():
    repeat = True
    while repeat == True:
        letter_total = 0
        cons_count = 0
        vow_count = 0
        force_vow_amt = False
        
        # Get center letter
        center = get_cen_letter()
        for each in lib_vowels:
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
        
        
        all_letters = [center]
        for each in vowels:
            all_letters += [each]
        for each in consonants:
            all_letters += [each]
        
            
            # CHECK FOR REDUNDANCIES
        redundancies = 0
        for each in all_letters:
            for all in all_letters:
                if check_letter(all[0],each[0])== True:
                    # Count of 7 is normal
                    redundancies += 1
        
        # Redundancy action
        if redundancies > 7:
            repeat = True
        else:
            repeat = False
            exit
        
	all_letters_freq = 0
	for each in all_letters:
		all_letters_freq += each[1]
	all_letters_freq_mean = all_letters_freq/7
    
    return all_letters, all_letters_freq_mean