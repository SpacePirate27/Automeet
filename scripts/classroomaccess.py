import imaplib
import email
from email.header import decode_header
from os import name
import webbrowser
import os
import pickle
import scripts.linkScraper as lis
import datetime

from googleapiclient.discovery import build


def get_the_day(gap):
    days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    day = datetime.date.today() + datetime.timedelta(days=gap)
    day = days[day.weekday()]
    return day

def get_the_link(nextclass,creds):
    classcode = nextclass[0][0]
    classtime = nextclass[0][1]
    classday = get_the_day(nextclass[1])

    courses = {}
    if os.path.isfile(os.getcwd()+'\\timetables\\'+'course_classroom'+'.pkl') is True:
        clcourse = open(os.getcwd()+'\\timetables\\'+'course_classroom'+'.pkl',"rb")
        courses = pickle.load(clcourse)
        clcourse.close()
    #print(courses)
    
    classroom_name = courses[classcode]
    
    service = build('classroom', 'v1', credentials=creds)
    results = service.courses().list(pageSize=10).execute()
    courses = results.get('courses', [])
    current_course = None
    for course in courses:
        if course['name'] == classroom_name:
            current_course = course
            #print(course)
        else:
            #print('Course name is: ',course['name'],' AND CLASSROOM NAME IS: ',classroom_name)
            None
    
    #print('\n\n',current_course['id'],'\n\n')

    temp = service.courses().announcements().list(courseId=current_course['id']).execute()
    starter = 0
    while starter < 3:
        latest_annon = temp['announcements'][starter]
        text = latest_annon['text']
        link = None
        try:
            link = latest_annon['materials'][0]['link']['url']
        except:
            text = text.replace('\r',' ')
            text = text.replace('\n',' ')
            textlist = text.split(' ')
            #print(textlist)
            for i in textlist:
                if 'meet.google.com' in i.split('/'):
                    link = i
        if link == None:
            starter += 1
        else:
            return link