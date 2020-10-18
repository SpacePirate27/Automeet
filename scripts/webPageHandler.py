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

def profile_creator(link): #the function receives the meet link, the function first needs perform the above mentioned functions and return nothing
    drivers = os.getcwd().split('\\scripts')[0]+'\\web_drivers'
    #meetdriver = None
    temp = 'user-data-dir='+drivers+'\myprofile'
    to = Options()
    to.add_argument(temp)
    meetdriver = webdriver.Chrome(executable_path=drivers+'\chromedriver.exe', chrome_options=to)
    meetdriver.get('http://www.google.com')
    while(  ):#condition to keep the browser open
        #keep running the code / browser open 
        #probably the participants part
        
    #sendNotif(5)
    

    












profile_creator ('mail.google.com')