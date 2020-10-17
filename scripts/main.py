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
import pickle
import datetime
import os
import time
days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

def compare_times(timeone,timetwo): #the function needs to be filled to accept two strings in the format "04:40 PM" and compare them,return 0 if timeone is greater and return 1 if timetwo is greater
    t1 = timeone.split(' ')
    t2 = timetwo.split(' ')
    if(t1[1]!=t2[1]):
        if 'PM' in t1:
            return 0
        else:
            return 1
    else:
        t1hr = t1[0].split(':')[0]
        t2hr = t2[0].split(':')[0]

        if t1hr > t2hr:
            return 0
        elif t2hr > t1hr:
            return 1
        else:
            t1min = t1[0].split(':')[1]
            t2min = t2[0].split(':')[1]

            if t1min>t2min:
                return 0
            else:
                return 1

def get_next_class(ctime,todlist,x,tomlist,y,dayafterlist,z): #The function needs to be filled to accept the current time, a list of todays classes and a list of tomorrows classes, and to return a tuple (as shown in the example) that is the next class, FORMAT: ctime-"05:40 PM"(str), todlist/tomlist-[[('cse308', '08.45 am'),monday] ('cse301', '11.00 am')]

    for i in todlist:
        if compare_times(ctime,i[1]) == 1:
            return [i,0]
    if tomlist is not []:
        return [tomlist[0],1]
    else:
        return [dayafterlist[0],2]


def calculate_seconds(cxtime,nxclass): #The function needs to be filled to return the difference between timea and timeb in SECONDS (format of timea and timeb is same as above in STRING), 
    if nxclass[1] == 0:
        





while(1):
    today = days[datetime.date.today().weekday()] #days gets the value(string) of the current day
    tom = datetime.date.today() + datetime.timedelta(days=1)
    datom = datetime.date.today() + datetime.timedelta(days=2)
    tomorrow = days[tom.weekday()]
    dayaftertom = days[datom.weekday()]
    print(today,tomorrow,dayaftertom)

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
    next_class = get_next_class(current_time,today_classes_list,today,tomorrow_classes_list,tomorrow,dayafter_classes_list,dayaftertom)
    remaining_time = calculate_seconds(current_time,next_class)

    time.sleep(remaining_time-180) #sleeps the program until 3 minutes before the upcoming class
    class_link = get_the_link(next_class) #this function should be in the mailaccess.py file and should return either the link of the google meet or should automatically fall back to to the fallbackprotocol and find the link and return it 

    web_page_opener(class_link) #this function should be present in the webpagehandler python file and should accept the link and open it in the current profile, NOTE: webpageopener function will also close the webpage upon the class getting over




