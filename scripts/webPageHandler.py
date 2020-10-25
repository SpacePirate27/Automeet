# this opens the browser with the specifc profile
# opens the meeting link
# mute audio
# turn off video
# join the link
# close the meet when the number of participants fall below 10

from time import sleep
#import scripts.usernotifier as uno
import selenium 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
import datetime


def web_page_opener(link):
    drivers = os.getcwd().split('\\scripts')[0]+'\\web_drivers'
    temp = 'user-data-dir='+drivers+'\myprofile'
    to = Options()
    to.add_argument(temp)
    to.add_argument("--use-fake-ui-for-media-stream")
    to.add_argument("--use-fake-device-for-media-stream")
    to.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 1 
})
    time1 = datetime.datetime.now()

    meetdriver = webdriver.Chrome(executable_path=drivers+'\chromedriver.exe', chrome_options=to)
    meetdriver.get(link)

    time.sleep(5)

    try:
        mic_btn = meetdriver.find_element_by_xpath('/html/body/div[1]/c-wiz/div/div/div[5]/div[3]/div/div/div[2]/div/div/div[1]/div/div[4]/div[1]/div/div/div').click()
        vid_btn = meetdriver.find_element_by_xpath('/html/body/div[1]/c-wiz/div/div/div[5]/div[3]/div/div/div[2]/div/div/div[1]/div/div[4]/div[2]/div/div').click()
    except:
        time.sleep(10)
        mic_btn = meetdriver.find_element_by_xpath('/html/body/div[1]/c-wiz/div/div/div[5]/div[3]/div/div/div[2]/div/div/div[1]/div/div[4]/div[1]/div/div/div').click()
        vid_btn = meetdriver.find_element_by_xpath('/html/body/div[1]/c-wiz/div/div/div[5]/div[3]/div/div/div[2]/div/div/div[1]/div/div[4]/div[2]/div/div').click()

    time.sleep(2)
    
    uno.sendNotif(4)
    
    time.sleep(3)

    join_btn = meetdriver.find_element_by_xpath('/html/body/div[1]/c-wiz/div/div/div[5]/div[3]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]').click()

    uno.sendNotif(0)

    time.sleep(10)
    
    people_btn = meetdriver.find_element_by_xpath('/html/body/div[1]/c-wiz/div[1]/div/div[5]/div[3]/div[6]/div[3]/div/div[2]/div[1]').click()

    time.sleep(5)


    nos = 20
    while nos > 15:
        time.sleep(15)
        try:
            nos = meetdriver.find_element_by_xpath('/html/body/div[1]/c-wiz/div[1]/div/div[5]/div[3]/div[3]/div/div[2]/div[2]/div[1]/div[1]').text
            nos = nos.replace('(','')
            nos = nos.replace(')','')
            nos = nos.replace('People','')
            nos = nos.replace('\n','')
            nos = int(nos)
        except:
            time2 = datetime.datetime.now()
            diff = time2 - time1
            if diff.total_seconds() >= 3600:
                break

    meetdriver.close()
    uno.sendNotif(1)

web_page_opener('https://www.google.com')