# driver for the entire application
# find current date and time
# find the next class
# fix the time frame - for scanning the mail api for new mails
# scan the mail on the specified time frame
# get the meet link - perform scraping
# open the link and mute audio and video and join the meeting with the correct mail-id!
# close the meeting
# loop to ln3


from datetime import date
from datetime import timedelta
import datetime
import pickle
import os
from pickle import FALSE
from scripts.timetable import initiate_credentials
import scripts.webPageHandler as wph
import scripts.classroomaccess as ma
import scripts.calendaraccess as cac
import time
import sys

days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

def twelve_to_24(twelvetime):
    temp = twelvetime.split(' ')
    if temp[1] == 'AM':
        min = temp[0].split(':')[1]
        hr = temp[0].split(':')[0]
        if hr == '12':
            hr = '00'
        fin = hr + ':' + min + ':' + '00'
    else:
        hr = int(temp[0].split(':')[0])
        if hr != 12:
            hr += 12
        min = temp[0].split(':')[1]
        fin = str(hr)+':'+min+':'+'00'
    return fin

def compare_times(timeone,timetwo): #the function return 0 if timeone is greater and return 1 if timetwo is greater 12:45 am, 945 am , expected op is 1

    t1 = twelve_to_24(timeone).split(':')
    t2 = twelve_to_24(timetwo).split(':')

    if t1[0] > t2[0]:
        return 0
    elif t1[0] < t2[0]:
        return 1
    else:
        if t1[1] > t2[1]:
            return 0
        else:
            return 1

    
def get_next_class(): #The function obtains the next class time and day
    #print(todlist)
    today = days[datetime.date.today().weekday()] #days gets the value(string) of the current day
    tom = datetime.date.today() + datetime.timedelta(days=1)
    datom = datetime.date.today() + datetime.timedelta(days=2)
    tomorrow = days[tom.weekday()]
    dayaftertom = days[datom.weekday()]

    file_handler = open(os.getcwd()+'\\timetables\\'+today+'.pkl',"rb")
    today_classes_list = pickle.load(file_handler)
    file_handler.close()

    file_handler = open(os.getcwd()+'\\timetables\\'+tomorrow+'.pkl',"rb")
    tomorrow_classes_list = pickle.load(file_handler)
    file_handler.close()

    file_handler = open(os.getcwd()+'\\timetables\\'+dayaftertom+'.pkl',"rb")
    dayafter_classes_list = pickle.load(file_handler)
    file_handler.close()

    current_time = datetime.datetime.now().time().strftime("%I:%M %p")


    for i in today_classes_list:
        #print(i)
        if compare_times(current_time,i[1]) == 1:
            return [i,0]
    if len(tomorrow_classes_list) != 0:
        return [tomorrow_classes_list[0],1]
    else:
        return [dayafter_classes_list[0],2]



def calculate_seconds(cxtime,nxclass): #The function returns the difference between timea and timeb in SECONDS
    final_time = 0
    if nxclass[1] == 0:
        final_time = 0
    elif nxclass[1] == 1:
        final_time = 86400
    else:
        final_time = 172800

    timea = twelve_to_24(cxtime)
    timeb = twelve_to_24(nxclass[0][1])

    fmt = '%H:%M:%S'
    tdelta = datetime.datetime.strptime(timeb, fmt) - datetime.datetime.strptime(timea, fmt)
    seconds = int(tdelta.total_seconds())
    final_time += seconds
    return final_time

def mainrunner():
    creds = initiate_credentials()
    current_time = datetime.datetime.now().time().strftime("%I:%M %p")
    next_class = get_next_class()
    remaining_time = calculate_seconds(current_time,next_class)

    print('Next Class',next_class[0][0], 'is at', next_class[0][1], 'and starts in', int(remaining_time)//60,'minutes')

    next_calendar_check = datetime.datetime.now() + datetime.timedelta(seconds=remaining_time-300) #sleeps the program until 5 min before before the upcoming class
    next_classroom_check = datetime.datetime.now() + datetime.timedelta(seconds=remaining_time+180)

    while datetime.datetime.now() < next_calendar_check:
        #Display object . settext (waiting for class)
        None

    class_link = cac.getthelink(next_class,creds) #this function should be in the calendaraccess.py file and should return either the link of the google meet or none

    while datetime.datetime.now() < next_classroom_check:
        None

    if class_link == None:
        class_link = ma.get_the_link(next_class,creds)

    print('\n\n','Class Link is ',class_link)

    wph.web_page_opener(class_link) #this function should be present in the webpagehandler python file and should accept the link and open it in the current profile, NOTE: webpageopener function will also close the webpage upon the class getting over





