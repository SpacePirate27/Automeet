# this opens the browser with the specifc profile
# opens the meeting link
# mute audio
# turn off video
# join the link
# close the meet when the number of participants fall below 10

#from scripts.usernotifier import sendNotif
import selenium 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os

def profile_creator(): #the function receives the meet link, the function first needs perform the above mentioned functions and return nothing
    drivers = os.getcwd().split('\\scripts')[0]+'\\web_drivers'
    temp = 'user-data-dir='+drivers+'\myprofile'
    to = Options()
    to.add_argument(temp)
    prf = webdriver.Chrome(executable_path=drivers+'\chromedriver.exe', chrome_options=to)
    prf.get('http://mail.google.com')
    

def web_page_opener(link):
    drivers = os.getcwd().split('\\scripts')[0]+'\\web_drivers'
    temp = 'user-data-dir='+drivers+'\myprofile'
    to = Options()
    to.add_argument(temp)
    meetdriver = webdriver.Chrome(executable_path=drivers+'\chromedriver.exe', chrome_options=to)
    meetdriver.get(link)

    time.sleep(5)
    mic_btn = meetdriver.find_element_by_xpath('/html/body/div[1]/c-wiz/div/div/div[5]/div[3]/div/div/div[2]/div/div/div[1]/div/div[4]/div[1]/div/div/div').click()
    vid_btn = meetdriver.find_element_by_xpath('/html/body/div[1]/c-wiz/div/div/div[5]/div[3]/div/div/div[2]/div/div/div[1]/div/div[4]/div[2]/div/div').click()
    join_btn = meetdriver.find_element_by_xpath('/html/body/div[1]/c-wiz/div/div/div[5]/div[3]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]').click()
    time.sleep(5)
    people_btn = meetdriver.find_element_by_xpath('/html/body/div[1]/c-wiz/div[1]/div/div[5]/div[3]/div[6]/div[3]/div/div[2]/div[1]').click()
    time.sleep(2)
    nos = 20
    while nos > 20:
        nos = meetdriver.find_element_by_xpath('/html/body/div[1]/c-wiz/div[1]/div/div[5]/div[3]/div[3]/div/div[2]/div[2]/div[1]/div[1]/span/div/span[2]').text
        nos = nos.replace('(','')
        nos = nos.replace(')','')
        nos = int(nos)
web_page_opener('https://meet.google.com/ndy-qyum-jwh')
    

    












profile_creator ('mail.google.com')