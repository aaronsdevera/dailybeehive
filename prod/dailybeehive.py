import os
import argparse
import logging

logging.basicConfig(filename='db.log', level=logging.INFO,format='%(asctime)s %(message)s')

ALF=''
letters=[0]*7
payload=''

def solve(opts,msg):

    if opts['generate']:
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
    
    if opts['publish']:
    
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
        
        footer = '\nALF: ' + str("%.2f" % ALF)
        
        if len(msg) > 1:
            top_message = msg
            payload = top_message + '\n' + header + hive[0] + hive [1] + hive[2] + hive[3] + hive[4] + footer        
        else:
            payload = header + hive[0] + hive [1] + hive[2] + hive[3] + hive[4] + footer
        
        print payload
        logging.info('SUCCEEDED: Twitter publication.')

    if opts['solution']:
        logging.info('Operation started: solution generation.')
        
        f=open('./lib/wordlist.txt', 'r')
        words = []
        
        letter_anag = ''
        for each in letters:
            letter_anag+=each
            
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
                    
                        words.append(word)
        f.close()
        
        solutions_file = './solutions/beehive'+str(date.replace('/',''))+'.txt'
        
        f=open(solutions_file, 'w')  
        f.write('Daily Beehive solution for ' + date + ':\n')
        f.close()
        f=open('./solutions/beehive'+str(date.replace('/',''))+'.txt', 'a')
        for each in words:
            f.write(each+'\n')
        f.close()
        
        logging.info('SUCCEEDED: Solution generation.')
        
        logging.info('Operation started: Ulpoading solution via git')
        
        os.system('git add ' + solutions_file)
        os.system('git commit -m "added solutions file"')
        os.system('git push')
        
        logging.info('SUCCEEDED: Uploaded solutions to GitHub.')
       
    if opts['twitter']:
        logging.info('Operation started: Twitter publication.')
        
        payload+='/nSolved: https://raw.githubusercontent.com/aaronsdevera/dailybeehive/master/prod/solutions/beehive'+str(date.replace('/',''))+'.txt'
        
        import twitter
        from twitter_api_keys import KEYS
        
        api = twitter.Api(consumer_key=KEYS[0],
                        consumer_secret=KEYS[1],
                        access_token_key=KEYS[2],
                        access_token_secret=KEYS[3])

        status = api.PostUpdate(payload)

    if opts['automate']:
        logging.info('Operation started: automation.')
        
        logging.info('SUCCEEDED: Automation operation.')

# Args
parser = argparse.ArgumentParser(description='Daily Beehive, an autmated word puzzle.')
parser.add_argument('-g','--generate', help='Generate a puzzle in a list output', required=False, action='store_true', default=True)
parser.add_argument('-p','--publish', help='Publish a puzzle in ASCII', required=False, action='store_true')
parser.add_argument('-s','--solution', help='Provide solution link', required=False, action='store_true')
parser.add_argument('-t','--twitter', help='Publish list to Twitter', required=False, action='store_true')
parser.add_argument('-a','--automate', help='Automate puzzle generation', required=False, action='store_true')
args = vars(parser.parse_args())

# Dropbox for top message
logging.info('Connecting to Github for message dropbox.')
os.system('wget https://raw.githubusercontent.com/aaronsdevera/dailybeehive/master/prod/dropbox')
with open('dropbox') as f:
    msg = f.read()
    #msg = "'"+f.read()+"'"
    logging.info('Message processed from message dropbox.')
    f.close()
    
# Main arg solve
solve(args,msg)
logging.info('Main args solved.')

# Clean folder
os.system('rm -rf *.pyc ./lib/*.pyc')
os.system('rm -rf dropbox*')
logging.info('Folder hierarchy cleaned.')