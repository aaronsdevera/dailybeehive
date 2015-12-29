# -*- coding: utf-8 -*- 
import schedule
import logging
import time
import os

logging.basicConfig(filename='db.log', level=logging.INFO,format='%(asctime)s %(message)s')

import twitter
from twitter_api_keys import KEYS
api = twitter.Api(consumer_key=KEYS[0],
                        consumer_secret=KEYS[1],
                        access_token_key=KEYS[2],
                        access_token_secret=KEYS[3])

def job():
    try:
        #os.chdir("./prod/")
        #os.chdir("/home/pi/dailybeehive/")
        os.system('rm launch.py')
        os.system("wget https://raw.githubusercontent.com/aaronsdevera/dailybeehive/master/prod/launch.py")
        os.system("python launch.py")
        logging.info("Tweet posted")
        os.system("rm -rf *.pyc /lib/*.pyc")
    except:
        logging.error("Post job aborted: Error")
        # Post error tweet
        import datetime
        timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        message1 = u'    \U0001F525'
        message2 = u'  \U0001F525 \U0001F4BB \U0001F525'
        message3 = u'ʕノ•ᴥ•ʔノ' 
        payload = timestamp + '\n' + message1 + '\n' + message2 + '\n' + message3
        status = api.PostUpdate(payload)

#schedule.every().seconds.do(job)
#schedule.every().minutes.do(job)
#schedule.every().hour.do(job)
schedule.every().day.at("08:00").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)