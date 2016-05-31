import os
import argparse
import logging

logging.basicConfig(filename='db.log', level=logging.INFO,format='%(asctime)s %(message)s')

ALF=''
letters=[0]*7
payload=''

def solve(opts):

    if opts['generate']:
        goodPuzzle = False
        while goodPuzzle == False:
            logging.info('Operation started: generation.')
            import sys
            sys.path.append('./lib')
            
            from generate import generate
            count=0
            for each in generate()[0]:
                letters[count] = each[0]
                count+=1
            ALF = generate()[1]
            
            print letters
            print ALF
            logging.info('SUCCEEDED: puzzle generation.')
            
            # SOLUTION
            logging.info('Operation started: solution generation.')
            
            f=open('./lib/wordlist.txt', 'r')
            uncheck_words = []
            
            letter_anag = ''
            for each in letters:
                letter_anag+=each
                
            # Can you think of any word with the same letter appearing more than 5 times?
            letter_anag+=letter_anag+letter_anag+letter_anag+letter_anag+letter_anag     
            
            def anagramchk(word,chkword):
                for letter in word:
                    if letter in chkword:
                        chkword=chkword.replace(letter, '', 1)
                    else:
                        return 0
                return 1
            
            for line in f:
                for line in f:
                    word=line.strip()
                    if anagramchk(word,letter_anag):
                        uncheck_words.append(word)
            f.close()

            logging.info('SUCCEEDED: Unchecked word solutions.')
            logging.info('Operation started: Checking word solutions for reqs.')
            
            words = []
            
            target_letter = set(letters[0])
            for each in uncheck_words:
                if target_letter & set(each):
                    words.append(each)
            
            ## CHECK SOLUTIONS FOR SUPER WORD
            from find_super_words import find_super_words
            super_words_noise = []
            for each in words:
                super_words_noise.append(find_super_words(each,letters))
            super_words = []
            if len(super_words_noise) > 1:
                for each in super_words_noise:
                    if each != None:
                        super_words.append(each)
            if len(super_words) > 1:
                goodPuzzle = True
         
                
        print super_words
        
        # DETERMINING DIFFICULTY
        difficulty = ''
        average_num_solutions = 200
        average_num_super_words = 5
        
        if len(words)-average_num_solutions > -70 and len(words)-average_num_solutions < 70:
            difficulty = 'MED'
        if len(words)-average_num_solutions <= -70:
            difficulty = 'HARD'
        if len(words)-average_num_solutions >= 70:
            difficulty = 'EASY'
        
        
        # GIT
        os.system('git add ' + solutions_file)
        os.system('git commit -m "added solutions file"')
        os.system('git push origin master')
        
        logging.info('SUCCEEDED: Uploaded solutions to GitHub.')
        
        # PRINT AND PUB
        # 140 character limit
        
        # 22 characters
        import time
        import os
        
        date = time.strftime("%x")
        header = 'Beehive for ' + date + ':' + '\n'
        
        hive = [0] * 5
        hive[0]='   \   '+str(letters[1]).upper()+'  /' + '\n'
        hive[1]=str(letters[2]).upper()+'   \    /   '+str(letters[3]).upper() + '\n'
        hive[2]='---(  '+str(letters[0]).upper()+'  )---' + '\n'
        hive[3]=str(letters[4]).upper()+'   /    \   '+str(letters[5]).upper() + '\n'
        hive[4]='    /  '+str(letters[6]).upper()+'   \\'
        
        #footer = '\nALF: ' + str("%.2f" % ALF)
        footer = '\nDIFF: %s (%s sltns)' % (difficulty,len(words))
        footer += '\nSolved: %s' % solution_link
        
        payload = header + hive[0] + hive [1] + hive[2] + hive[3] + hive[4] + footer
        
        print payload
        #os.system('echo "SOLUTIONS,%s,SUPER,%s" >> sol.csv' % (len(words),len(super_words)))
        
        logging.info('SUCCEEDED: Printed.')
        
        ## OUTPUT SOLUTIONS
        #solutions_file = './beehive'+str(date.replace('/',''))+'.txt'
        solutions_file = './solutions/beehive'+str(date.replace('/',''))+'.txt'
        
        f=open(solutions_file, 'w')  
        f.write('Daily Beehive solution for ' + date + ':\n')
        f.close()
        f=open(solutions_file, 'a')
        f.write('DIFFICULTY: %s (%s solutions)\n' % (difficulty,len(words)))
        f.write('--------------------------------------------'+'\n\n')
        f.write('Solutions that use each letter at least once (%s):\n' % len(super_words))
        for each in super_words:
            f.write(each+'\n')
        
        f.write('\nAll solutions (%s):\n' % len(words))
        
        for each in words:
            f.write(each+'\n')
        f.close()
        
        logging.info('SUCCEEDED: Solution generation accounting for reqs.')
        
        
       
    if opts['twitter']:
        logging.info('Operation started: Twitter publication.')
        
        payload+='\nSolved: https://raw.githubusercontent.com/aaronsdevera/dailybeehive/master/prod/solutions/beehive'+str(date.replace('/',''))+'.txt'
        
        import twitter
        from twitter_api_keys import KEYS
        
        api = twitter.Api(consumer_key=KEYS[0],
                        consumer_secret=KEYS[1],
                        access_token_key=KEYS[2],
                        access_token_secret=KEYS[3])

        status = api.PostUpdate(payload)
        logging.info('SUCCEEDED: Posted to Twitter.')
        
# Update with git
'''
logging.info('Operation started: Patching with git...')
os.system('git pull origin master')
logging.info('SUCCEEDED: Latest version active.')
'''

# Args
parser = argparse.ArgumentParser(description='Daily Beehive, an autmated word puzzle.')
parser.add_argument('-g','--generate', help='Generate a puzzle in a list output', required=False, action='store_true', default=True)
parser.add_argument('-t','--twitter', help='Publish list to Twitter', required=False, action='store_true')
args = vars(parser.parse_args())
    
# Main arg solve
solve(args)
logging.info('Main args solved.')

# Clean folder
os.system('rm -rf *.pyc ./lib/*.pyc')
logging.info('Folder hierarchy cleaned.')