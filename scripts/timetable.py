from os import path
from os.path import isfile
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
import pickle
import os.path

times=['08:45 AM','09:45 AM','11:00 AM','12:00 PM','01:00 PM','02:00 PM','03:15 PM','04:15 PM']
days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

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
                    time = prompt('Enter the time: ',completer=WordCompleter(times))
                except:
                    print('Error occured')
                temp.append((cc,time))
                flag = input('Do you want to add another course? (y/n)')
            ############################################################################################################
            #                ADD A CODE HERE THAT FORMATS THE LIST TEMP, IN ORDER OF THE CLASSES,                      #
            #     THE LIST WILL HAVE TUPLES IN IT IN THE DESIGN OF [('cse308', '08.45 am'), ('cse301', '11.00 am')]    #
            #                       COMPARE THE TIMES OF EACH TUPLE[1] AND SORT THEM                                   #
            #       NOTE THE AM AND PM, SO SORT THEM SEPARATELY, MAINTAINGING THEIR OWN ORDER OF FIRST AM THEN PM      #
            #              ALSO NOTE THIS FUNCTION HAS TO BE IN THE FOR LOOP - OUTSIDE THE WHILE LOOP                  #
            ############################################################################################################

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

