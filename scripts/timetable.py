timeTable=[{"Monday":[]},{"Tuesday":[]},{"Wednesday":[]},{"Thursday":[]},{"Friday":[]},{"Saturday":[]}]


def inputTimetable():
    # A function to take the timetable as input
    isExit="n"
    days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    for day in days:
        print("Enter the Course Code, Timing, Meeting Link Mode following for {} in the following format 'Timing, Course Code, Meet link mode':".format(day))
        while isExit == "n":
            inputString=input()
            convertToTimeTable(inputString,day)
            isExit=input("Are you done (y/n)?")
        isExit="n"
    print(timeTable)
        

def convertToTimeTable(inputString,day):
    # a function to convert the input string data into the required format and input into the timetable
    timeTableFields=inputString.split(",")
    timing = timeTableFields[0]
    courseCode = timeTableFields[1]
    meetLinkMode = timeTableFields[2]
    detailsDict={}
    detailsDict["timing"]=timing.strip()
    detailsDict["courseCode"]=courseCode.strip()
    detailsDict["meetLinkMode"]=meetLinkMode.strip()
    if day == "Monday":
        dayEntry=timeTable[0].get(day)
    elif day == "Tuesday":
        dayEntry=timeTable[1].get(day)
    elif day == "Wednesday":
        dayEntry=timeTable[2].get(day)
    elif day == "Thursday":
        dayEntry=timeTable[3].get(day)
    elif day == "Friday":
        dayEntry=timeTable[4].get(day)
    elif day == "Saturday":
        dayEntry=timeTable[5].get(day)
    dayEntry.append(detailsDict)


if __name__ == "__main__":
    # program flow starts here
    inputTimetable()