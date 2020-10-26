from scripts.main import mainrunner
import traceback
import os.path
from selenium import webdriver
from scripts.timetable import initiate_credentials
from googleapiclient.discovery import build

checker = []

def credcheck():
    if os.path.isfile('credentials.json'):
        return 1
    else:
        return 0

def chrome_check():
    try:
        drivers = os.getcwd()+'\\web_drivers'+'\\chromedriver.exe'
        temp = webdriver.Chrome(executable_path=drivers)
        temp.close()
        return 1
    except:
        return 0

def chrome_profile():
    profpath = os.getcwd()+'\\web_drivers\\myprofile'
    if os.path.isdir(profpath):
        return 1
    else:
        return 0

def calendar_api():
    try:
        creds = initiate_credentials()
        calservice = build('calendar', 'v3', credentials=creds)
        return 1
    except:
        return 0

def classroom_api():
    try:
        creds = initiate_credentials()
        classervice = build('classroom', 'v1', credentials=creds)
        return 1
    except:
        return 0

def timetables_creation():
    days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','courses','course_classroom']
    for i in days:
        dir = os.getcwd()+'\\timetables\\'+i+'.pkl'
        if os.path.isfile(dir) is False:
            return 0
    return 1

def all_verified():
    if 0 in checker:
        return 0
    else:
        return 1


if __name__ == "__main__":
    with open('log.txt','w') as log:
        try:
            mainrunner()
        except:
            traceback.print_exc(file=log)
            print('Errors have been written to a log file')
