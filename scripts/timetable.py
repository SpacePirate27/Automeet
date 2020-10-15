from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
import pickle

times=['08.45 am','09.45 am','11.00 am','12.00 pm','01.00 pm','02.00 pm','03.15 pm','04.15 pm']
monday=[]
tuesday=[]
wednesday=[]
thursday=[]
friday=[]
saturday=[]
classes=[]
def inputTimeTable(day):
    char='y'
    while(char == 'y'):
        coursecode = input("Enter the course code ")
        timing = prompt("Enter the time ",completer=WordCompleter(times))
        temp=(coursecode,timing)
        classes.append(temp)
        char = input("Do you want to input another course?(y/n) ")

if __name__ == "__main__":
    # initializing days
    try:
        print("Enter the courses for Monday ")
        inputTimeTable("monday")
        print("Enter the courses for Tuesday ")
        inputTimeTable("tuesday")
        print("Enter the courses for Wednesday ")
        inputTimeTable("wednesday")
        print("Enter the courses for Thursday ")
        inputTimeTable("thursday")
        print("Enter the courses for Friday ")
        inputTimeTable("friday")
        print("Enter the courses for Saturday ")
        inputTimeTable("saturday")
    except:
        print("Error Occur")

    # saving timetable
    print("Attempting to save the timetable... ")
    try:
        with open("../timetables/monday.pkl","w") as md:
            pickle.dump(monday,md)
        with open("../timetables/tuesday.pkl","w") as td:
            pickle.dump(tuesday,td)
        with open("../timetables/wednesday.pkl","w") as wd:
            pickle.dump(wednesday,wd)
        with open("../timetables/thursday.pkl","w") as thd:
            pickle.dump(thursday,thd)
        with open("../timetables/friday.pkl","w") as fd:
            pickle.dump(friday,fd)
        with open("../timetables/saturday.pkl","w") as sd:
            pickle.dump(saturday,sd)
        print("Timetable Saved Succesfully! ")
    except:
        print("Failed to save the timetable! Check Permissions ")
