import schedule
import time
import os

def job():
    os.system('mkdir dailybeehive')
    os.system('cd dailybeehive')
    os.system('git clone https://github.com/aaronsdevera/dailybeehive.git')
    os.system('cd dailybeehive/prod')
    os.system('python dailybeehive.py -gpst')
    os.system('cd; rm -rf dailybeehive')
    

schedule.every(.05).minutes.do(job)
#schedule.every().hour.do(job)
#schedule.every().day.at("10:30").do(job)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(10)