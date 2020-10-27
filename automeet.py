from datetime import datetime
from threading import Event
from xml.etree.ElementTree import TreeBuilder
from PyQt5.QtCore import QThread

from selenium.webdriver.chrome.options import Options
from scripts.main import mainrunner
import traceback
import os.path
from selenium import webdriver
from scripts.timetable import initiate_credentials
from googleapiclient.discovery import build
from scripts.timetable import profile_creator
from scripts.timetable import ttadder
from scripts.main import get_next_class
from scripts.timetable import __main__


from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui
import sys
import webbrowser

import threading

checker = [1,1,1,1,1,1]

def credcheck():
    if os.path.isfile('credentials.json'):
        return True
    else:
        return False

def chrome_check():
    try:
        drivers = os.getcwd()+'\\web_drivers'+'\\chromedriver.exe'
        options = Options()
        options.add_argument('headless')
        temp = webdriver.Chrome(executable_path=drivers,chrome_options=options)
        temp.close()
        return True
    except:
        return False

def chrome_profile():
    profpath = os.getcwd()+'\\web_drivers\\myprofile'
    if os.path.isdir(profpath):
        return True
    else:
        return False

def calendar_api():
    try:
        creds = initiate_credentials()
        calservice = build('calendar', 'v3', credentials=creds)
        return True
    except:
        return False

def classroom_api():
    try:
        creds = initiate_credentials()
        classervice = build('classroom', 'v1', credentials=creds)
        return True
    except:
        return False

def timetables_creation():
    days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','courses','course_classroom']
    for i in days:
        dir = os.getcwd()+'\\timetables\\'+i+'.pkl'
        if os.path.isfile(dir) is False:
            return False
    return True

def all_verified():
    if 0 in checker:
        return False
    else:
        return True

class mainpage(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainpage,self).__init__()
        uic.loadUi(os.getcwd()+'\\gui_uis\\front.ui',self)

        self.currtime = self.findChild(QtWidgets.QLabel,'currtime')
        self.nxtclass = self.findChild(QtWidgets.QLabel,'nxtclass')
        self.stbutton = self.findChild(QtWidgets.QPushButton,'start')
        self.stbutton.clicked.connect(self.startbutton)     
        self.stopbutton = self.findChild(QtWidgets.QPushButton,'stop')
        self.stopbutton.clicked.connect(self.stopbuttonfunction)

        self.ttcross = self.findChild(QtWidgets.QLabel,'tt_cross')
        self.tttick = self.findChild(QtWidgets.QLabel,'tt_tick')
        self.ttfix = self.findChild(QtWidgets.QPushButton,'tt_fix')
        self.ttfix.clicked.connect(self.ttfixer)
        self.credcross = self.findChild(QtWidgets.QLabel,'cred_cross')
        self.credtick = self.findChild(QtWidgets.QLabel,'cred_tick')
        self.credfix = self.findChild(QtWidgets.QPushButton,'cred_fix')
        self.credfix.clicked.connect(self.credfixer)
        self.chromecross = self.findChild(QtWidgets.QLabel,'chrome_cross')
        self.chrometick = self.findChild(QtWidgets.QLabel,'chrome_tick')
        self.chromefix = self.findChild(QtWidgets.QPushButton,'chrome_fix')
        self.chromefix.clicked.connect(self.chromefixer)
        self.profilecross = self.findChild(QtWidgets.QLabel,'prof_cross')
        self.profiletick = self.findChild(QtWidgets.QLabel,'prof_tick')
        self.profilefix = self.findChild(QtWidgets.QPushButton,'prof_fix')
        self.profilefix.clicked.connect(self.profilefixer)
        self.calcross = self.findChild(QtWidgets.QLabel,'cal_cross')
        self.caltick = self.findChild(QtWidgets.QLabel,'cal_tick')
        self.calfix = self.findChild(QtWidgets.QPushButton,'cal_fix')
        self.calfix.clicked.connect(self.calfixer)
        self.classcross = self.findChild(QtWidgets.QLabel,'class_cross')
        self.classtick = self.findChild(QtWidgets.QLabel,'class_tick')
        self.classfix = self.findChild(QtWidgets.QPushButton,'class_fix')
        self.classfix.clicked.connect(self.classfixer)
        self.startbuttonflag = False
        self.startbuttonchecker = False
        self.mainfunflag = True
    

        self.credbuttoner()
        self.calbuttoner()
        self.ttbuttoner()
        self.chromebuttoner()
        self.profbuttoner()
        self.classbuttoner()

        self.mainthread = threading.Thread()


        self.timedisplay = threading.Thread(target=self.time_updater,daemon=True)
        self.timedisplay.start()

        self.starterThread = threading.Thread(target=self.verified_checker,daemon=True).start()


    def stopbuttonfunction(self):
        self.mainfunflag = False

    def verified_checker(self):
        while(self.startbuttonchecker is False):
            if all_verified():
                self.stbutton.setEnabled(True)

    def ttbuttoner(self):
        if timetables_creation():
            self.ttcross.hide()
            self.ttfix.hide()
            self.tttick.setHidden(False)
            checker[0] = 1
        else:
            self.tttick.hide()
            checker[0] = 0

    def credbuttoner(self):
        if credcheck():
            self.credcross.hide()
            self.credfix.hide()
            self.credtick.setHidden(False)
            checker[1] = 1
        else:
            self.credtick.hide()
            checker[1] = 0
    
    def profbuttoner(self):
        if chrome_profile():
            self.profilecross.hide()
            self.profilefix.hide()
            self.profiletick.setHidden(False)
            checker[2] = 1
        else:
            self.profiletick.hide()
            checker[2] = 0
    
    def chromebuttoner(self):
        if chrome_check():
            self.chromecross.hide()
            self.chromefix.hide()
            self.chrometick.setHidden(False)
            checker[3] = 1
        else:
            self.chrometick.hide()
            checker[3] = 0
    
    def calbuttoner(self):
        if calendar_api():
            self.calcross.hide()
            self.calfix.hide()
            self.caltick.setHidden(False)
            checker[4] = 1
        else:
            self.caltick.hide()
            checker[4] = 0


    def classbuttoner(self):
        if classroom_api():
            self.classcross.hide()
            self.classfix.hide()
            self.classtick.setHidden(False)
            checker[5] = 1
        else:
            self.classtick.hide()
            checker[5] = 0

    def ttfixer(self):
        window2.show()
        self.ttbuttoner()
          
    def credfixer(self):
        webbrowser.open('https://github.com/RamNarayan27/Automeet/tree/master')
        self.credbuttoner()


    def chromefixer(self):
        webbrowser.open('https://www.google.com/intl/en_in/chrome/')
        self.chromebuttoner()


    def profilefixer(self):
        self.profthread = threading.Thread(target=profile_creator,daemon=True).start()
        self.profbuttoner()


    def calfixer(self):
        webbrowser.open('https://github.com/RamNarayan27/Automeet/tree/master')
        self.calbuttoner()

    def classfixer(self):
        webbrowser.open('https://github.com/RamNarayan27/Automeet/tree/master')
        self.classbuttoner()
    
    def mainfunrunner(self):
        while(self.mainfunflag is True):
            nxt_class = get_next_class()
            self.nxtclass.setText('Next Class is '+ nxt_class[0][0] + ' at ' + nxt_class[0][1])
            mainrunner()

    def startbutton(self):
        self.startbuttonchecker = True
        self.stopbutton.setEnabled(True)
        self.mainfunflag = True
        with open('log.txt','w') as log:
            try:
                mainthread = threading.Thread(target=self.mainfunrunner,daemon=True).start()
            except:
                traceback.print_exc(file=log)
                print('Errors have been written to a log file')

    def time_updater(self):
        while self.startbuttonflag is False:
            currtentime = datetime.now().replace(microsecond=0).time()
            self.currtime.setText('Current Time: '+ str(currtentime))
    
    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.startbuttonflag = True
        a0.accept()
 

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = mainpage()
    window2 = ttadder()
    window.show()
    am = app.exec_()

    
    
   
