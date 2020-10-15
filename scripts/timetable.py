from os import path
from os.path import isfile
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
import pickle
import os.path

times=['08.45 am','09.45 am','11.00 am','12.00 pm','01.00 pm','02.00 pm','03.15 pm','04.15 pm']
days = ['monday','tuesday','wednesday','thursday','friday','saturday']

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
            temp = []
            flag = 'y'
            while(flag == 'y'):
                cc = None
                time = None
                try:
                    cc = prompt('Enter the course code: ',completer=WordCompleter(courses))
                    if cc not in courses:
                        courses.append(cc)
                    time = prompt('Enter the time: ',completer=WordCompleter(times))
                except:
                    print('Error occured')
                temp.append((cc,time))
                flag = input('Do you want to add another course? (y/n)')
            #attempting to save
            print('Saving',i,'\b'+'s timetable')
            try:
                file_object = open(dir,'wb')
                pickle.dump(temp,file_object)
                file_object.close()
                print('Successfully saved '+i)
            except:
                print('Failed to save')
    
    dirc = os.getcwd()+'\\timetables\\'+'courses'+'.pkl'
    if courses is not []:    
        file_object = open(dirc,'wb')
        pickle.dump(courses,file_object)
        file_object.close()

