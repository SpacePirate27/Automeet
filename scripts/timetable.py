from os import path, removedirs
from os.path import isfile
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton, QWidget

from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
import pickle
from prompt_toolkit.filters import cli
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os.path
import time

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui
import sys
import webbrowser

import threading

times=['08:45 AM','09:45 AM','11:00 AM','12:00 PM','01:00 PM','02:00 PM','03:15 PM','04:15 PM']
days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
SCOPES = ['https://www.googleapis.com/auth/classroom.courses.readonly','https://www.googleapis.com/auth/classroom.announcements','https://www.googleapis.com/auth/calendar.readonly','https://www.googleapis.com/auth/calendar.events']

def initiate_credentials():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid: #ADD OAUTH 2.0 REQUESTS API HERE TO CREATE THE CREDENTIALS FILE  
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds

def profile_creator(): #the function receives the meet link, the function first needs perform the above mentioned functions and return nothing
    drivers = os.getcwd().split('\\scripts')[0]+'\\web_drivers'
    temp = 'user-data-dir='+drivers+'\myprofile'
    to = Options()
    to.add_argument(temp)
    to.add_experimental_option('detach',True)
    print('A browser will open! Login in to your SASTRA Account in that')
    time.sleep(5)
    prf = webdriver.Chrome(executable_path=drivers+'\\chromedriver.exe', chrome_options=to)
    prf.get('https://accounts.google.com')
    
def fun(course):
    timing=course[1]
    temp=timing.split(" ")
    temp2=temp[0].split(":")
    hr=temp2[0]
    return int(hr)

def sort_the_timetable(tt_list): # function to sort the timetable based on the timings of the class
    tt=[]
    ams=[] #contains all the am courses in the format ('<course-name>','<time>')
    pms=[] #contains all the pm courses in the format ('<course-name>','<time>')
    for course in tt_list:
        timing=course[1]
        temp1=timing.split(" ")
        if temp1[1] == 'AM':
            ams.append(course) #splitting the times based on am/pm
        elif temp1[1] == 'PM':
            pms.append(course)
    #print('ams',ams)
    #print('pms',pms)
    t1=sorted(ams,key=fun)
    t2=sorted(pms,key=fun)

    #print('sorted ams',t1)
    #print('sorted pms',t2)
    # t2 has 12pm courses at the last, so we're gonna fix that below
    final_t2=[]
    if len(t2) != 0:
        if t2[-1][1].split(':')[0] == str(12):
            final_t2.append(t2[-1])
            for i in range(len(t2)-1):
                final_t2.append(t2[i])
        else:
            final_t2=t2
    #print('super sorted pms',final_t2)         
    # append the sorted courses am first and pm last to tt and return it
    for course in t1:
        tt.append(course)
    for course in final_t2:
        tt.append(course)
    return tt

def get_courses_list(credentials_user):
    service = build('classroom', 'v1', credentials=credentials_user)
    results = service.courses().list(pageSize=10,courseStates='ACTIVE').execute()
    cses = results.get('courses', [])
    clist = []
    for course in cses:
        clist.append(course['name'])
    return clist

def get_cal_list(creds_usr):
    calservice = build('calendar', 'v3', credentials=creds_usr)
    calendar_list = calservice.calendarList().list().execute()
    cal_list = []
    for calendar_list_entry in calendar_list['items']:
        cal_list.append(calendar_list_entry['summary'])
    return cal_list



class ttadder(QtWidgets.QMainWindow):

    def __init__(self):
        super(ttadder,self).__init__()
        uic.loadUi(os.getcwd()+'\\gui_uis\\timetable.ui',self)

        self.dayname = self.findChild(QtWidgets.QLabel,'dayname')
        self.coursebox = self.findChild(QtWidgets.QComboBox, 'coursebox')
        self.timebox = self.findChild(QtWidgets.QComboBox, 'timebox')
        self.classroombox = self.findChild(QtWidgets.QComboBox, 'classroombox')

        self.timebox.addItems(times)

        self.addbutton = self.findChild(QtWidgets.QPushButton,'addbutton')
        self.nextdaybutton = self.findChild(QtWidgets.QPushButton,'nextday')
        self.savebutton = self.findChild(QtWidgets.QPushButton,'save')
        self.savebutton.clicked.connect(self.save_day)
        self.daybox = self.findChild(QtWidgets.QComboBox,'daybox')

        self.addbutton.clicked.connect(self.add_days_timetable)
        self.nextdaybutton.clicked.connect(self.go_next_day)

        self.tempcreds = initiate_credentials()

        self.cseslist = get_courses_list(self.tempcreds)

        self.classroombox.addItems(self.cseslist)

        self.daycounter = 0

        self.courses = []
        self.clcourse = {}
        self.onedaytt = []
        self.final_tt = []

        daybodthreader = threading.Thread(target=self.redodays,daemon=True).start()
        self.tt_runner()

    def save_day(self):
        dir = os.getcwd()+'\\timetables\\'+self.daybox.currentText()+'.pkl'
        file_object = open(dir,'wb')
        pickle.dump(self.final_tt,file_object)
        file_object.close()
        #saving courses
        dirc = os.getcwd()+'\\timetables\\'+'courses'+'.pkl'
        if self.courses is not []:    
            file_object = open(dirc,'wb')
            pickle.dump(self.courses,file_object)
            file_object.close()
        #saving classroom info
        dirc = os.getcwd()+'\\timetables\\'+'course_classroom'+'.pkl'
        if len(self.clcourse.keys()) != 0:
            classrooom_info_obj = open(dirc,'wb')
            pickle.dump(self.clcourse,classrooom_info_obj)
            classrooom_info_obj.close()

    def redodays(self):
        while(1):
            for i in days:
                if os.path.isfile(os.getcwd()+'\\timetables\\'+i+'.pkl') is False and self.daybox.findText(i) == -1:
                    self.daybox.addItem(i)

    def add_days_timetable(self):
        if self.coursebox.currentText() not in self.courses:
            self.courses.append(self.coursebox.currentText())
            self.clcourse[self.coursebox.currentText()] = self.classroombox.currentText()
        self.onedaytt.append((self.coursebox.currentText(),self.timebox.currentText()))
        
    def go_next_day(self):   
        if self.onedaytt != []:
            self.final_tt = sort_the_timetable(self.onedaytt)
        self.save_day()
        self.daybox.removeItem(self.daybox.findText(self.daybox.currentText()))
        

    def tt_runner(self):

        os.chdir(os.getcwd().split('\\scripts')[0])
        if not os.path.isdir('timetables'):
            os.makedirs('timetables')
            
        if os.path.isfile(os.getcwd()+'\\timetables\\'+'courses'+'.pkl') is True:
            inp_course = open(os.getcwd()+'\\timetables\\'+'courses'+'.pkl',"rb")
            self.courses = pickle.load(inp_course)
            inp_course.close()
            self.coursebox.addItems(self.courses)
        
        if os.path.isfile(os.getcwd()+'\\timetables\\'+'course_classroom'+'.pkl') is True:
            classroom_file_obj = open(os.getcwd()+'\\timetables\\'+'course_classroom'+'.pkl',"rb")
            self.clcourse = pickle.load(classroom_file_obj)
            classroom_file_obj.close()



def __main__():
    ttapp = QtWidgets.QApplication(sys.argv)
    window = ttadder()
    window.show()
    am = ttapp.exec_()

        
        
        
    



