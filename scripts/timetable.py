from os import path
from os.path import isfile

from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os.path
from operator import itemgetter
import getpass

times=['08:45 AM','09:45 AM','11:00 AM','12:00 PM','01:00 PM','02:00 PM','03:15 PM','04:15 PM']
days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

os.chdir(os.getcwd().split('\\scripts')[0])
if not os.path.isdir('timetables'):
    os.makedirs('timetables')
if not os.path.isdir('user_mail_creds'):
    os.makedirs('user_mail_creds')

def profile_creator(): #the function receives the meet link, the function first needs perform the above mentioned functions and return nothing
    drivers = os.getcwd().split('\\scripts')[0]+'\\web_drivers'
    temp = 'user-data-dir='+drivers+'\myprofile'
    to = Options()
    to.add_argument(temp)
    to.add_experimental_option('detach',True)
    prf = webdriver.Chrome(executable_path=drivers+'\chromedriver.exe', chrome_options=to)
    prf.get('http://mail.google.com')
    
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
        if t2[len(t2)-1][1].startswith('12'):
            final_t2.append(t2[len(t2)-1])
            for i in range(len(t2)-1):
                final_t2.append(t2[i])
        final_t2=t2
    #print('super sorted pms',final_t2)         
    # append the sorted courses am first and pm last to tt and return it
    for course in t1:
        tt.append(course)
    for course in final_t2:
        tt.append(course)
    return tt

if __name__ == "__main__":
    courses = []
    if os.path.isfile(os.getcwd()+'\\timetables\\'+'courses'+'.pkl') is True:
        inp_course = open(os.getcwd()+'\\timetables\\'+'courses'+'.pkl',"rb")
        courses = pickle.load(inp_course)
        inp_course.close()

    for i in days:
        dir = os.getcwd()+'\\timetables\\'+i+'.pkl'
        if os.path.isfile(dir) is False:
            print('Enter the timetable for '+i)
            print('If there are no courses for the day, type nill as course code')
            temp = []
            flag = 'y'
            while(flag == 'y'):
                cc = None
                time = None
                try:
                    cc = prompt('Enter the course code: ',completer=WordCompleter(courses))
                    if cc == 'nill':
                        temp = []
                        break
                    if cc not in courses:
                        courses.append(cc)
                except:
                    print('error')
                try:
                    time = prompt('Enter the time: ',completer=WordCompleter(times))
                except:
                    print('Error occured')
                temp.append((cc,time))
                flag = input('Do you want to add another course? (y/n)')
            final_tt = []
            if len(temp) != 0:
                final_tt = sort_the_timetable(temp)
            print(final_tt)
            
            #attempting to save
            print('Saving',i,'\b'+'s timetable')
            try:
                file_object = open(dir,'wb')
                pickle.dump(final_tt,file_object)
                file_object.close()
                print('Successfully saved '+i)
            except:
                print('Failed to save')
    
    dirc = os.getcwd()+'\\timetables\\'+'courses'+'.pkl'
    if courses is not []:    
        file_object = open(dirc,'wb')
        pickle.dump(courses,file_object)
        file_object.close()
    


    dirc = os.getcwd()+'\\user_mail_creds\\'+'user_name'+'.pkl'
    if os.path.isfile(dirc) is False:
        print('Before proceeding, ensure that less secure apps is allowed on your SASTRA account by clicking on the link below, \n\n https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiB2oXrk7zsAhXGZSsKHc6pAD4QFjAAegQIAxAC&url=https%3A%2F%2Fmyaccount.google.com%2Flesssecureapps&usg=AOvVaw3FH1O5TwzTEB9B9yhEUsI7 \n\n then press enter')
        fake = input()
        
        email = input('Enter the SASTRA Email ID')
        print('Enter the SASTRA Password (Your password will be stored locally on your device and will not be shared anywhere else!!!)')
        p = ''
        try: 
            p = getpass.getpass() 
        except Exception as error: 
            print('ERROR', error) 

        dirc = os.getcwd()+'\\user_mail_creds\\'+'user_name'+'.pkl'
        fo = open(dirc,'wb')
        pickle.dump(email,fo)
        fo.close

        dirc = os.getcwd()+'\\user_mail_creds\\'+'password'+'.pkl'
        fo = open(dirc,'wb')
        pickle.dump(p,fo)
        fo.close

    webdri_dir=os.getcwd()+'\\web_drivers\\myprofile'
    print(webdri_dir)

    if os.path.isdir(webdri_dir) is False:
        profile_creator()
        
    



