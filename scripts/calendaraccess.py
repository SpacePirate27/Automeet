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

def getthelink(nextclass,creds):
    classcode = nextclass[0][0]
    classtime = nextclass[0][1]
    classday = get_the_day(nextclass[1])

    starter = datetime.datetime.now()
    starttime = datetime.datetime.now().isoformat() + 'Z'
    endtime = starter + datetime.timedelta(hours=1,minutes=5)
    endtime = endtime.isoformat() + 'Z'
    calservice = build('calendar', 'v3', credentials=creds)
    id_list = []
    calendar_list = calservice.calendarList().list().execute()
    for calendar_list_entry in calendar_list['items']:
        id_list.append(calendar_list_entry['id'])
    link = None

    for eachid in id_list:
        eventc = calservice.events().list(calendarId=eachid,timeMin=starttime,timeMax=endtime,singleEvents=True,orderBy='startTime').execute()
        eventc = eventc['items']
        try:
            link = eventc[0]['conferenceData']['entryPoints'][0]['uri']
        except:
            None

    return link