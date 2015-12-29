def main():
	# MAIN
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
        
	all_letters_freq = 0
	for each in all_letters:
		all_letters_freq += each[1]
	all_letters_freq_mean = all_letters_freq/7
    
	# TWITTER DISTRO AND FORMAT
	# 30 characters to work with in top and bottom messages
	
	#date = datetime.today().strftime('%m/%d/%y')
	
	# load letters from letter generator functions "gen_x_letter"
    
    #hive_let = [0] * 6
	i=0
	let_vow = [0] * len(vowels)
	for each in vowels:
		let_vow[i] = each[0]
		i+=1
		
	i=0
	let_cons = [0] * len(consonants)
	for each in consonants:
		let_cons[i] = each[0]
		i+=1
	
	hive_let = let_vow + let_cons
	
	
	#print hive_let
	hive_cen_let = center[0]
    
	
	top_message = 'Beehive for ' + date + ':' + '\n' #20 characters
	hive = [0] * 7
	hive[0]='        ___' + '\n'
	hive[1]=' ___/  '+str(hive_let[0])+'  \___' + '\n'
	hive[2]='/  '+str(hive_let[1])+'  \___/  '+str(hive_let[2])+'  \\' + '\n'
	hive[3]='\___/  '+str(hive_cen_let)+'   \___/' + '\n'
	hive[4]='/  '+str(hive_let[3])+'  \___/  '+str(hive_let[4])+'  \\' + '\n'
	hive[5]='\___/  '+str(hive_let[5])+'  \___/' + '\n'
	hive[6]='       \___/' + '\n'
	bottom_message = 'ALF: ' + str("%.2f" % all_letters_freq_mean) #10 characters
	
	
	payload = top_message + hive[0] + hive [1] + hive[2] + hive[3] + hive[4] + hive[5] + hive[6] + bottom_message
	
	status = api.PostUpdate(payload)
    
    # Logger

    with open('server.log', 'a') as logfile:
        import time
        import datetime
        timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        logfile.write('time:'+timestamp+',center:'+str(center)+',vowels:'+str(vowels)+',consonants:'+str(consonants)+',all_letters:'+str(all_letters)+',freq_mean:'+str(all_letters_freq_mean))

if __name__ == '__main__':

    import twitter

    from twitter_api_keys import KEYS

    api = twitter.Api(consumer_key=KEYS[0],
                        consumer_secret=KEYS[1],
                        access_token_key=KEYS[2],
                        access_token_secret=KEYS[3])
                        


    # make path to lib
    import sys
    sys.path.append('./lib')

    # import lib
    from get_rand_letter import *
    from get_cen_letter import *
    from get_vow_letters import *
    from get_cons_letters import *
    from check_letter import *
    from lib_vowels import lib_vowels as vowels

    import time
    date = time.strftime("%x")
    main()
