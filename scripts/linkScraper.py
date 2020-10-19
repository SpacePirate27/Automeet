# scraper for the meeting link
# the mail will be in a html rendering
# grep for classroom.google.com and retirieve the entire link
# call webPageHandler


import mailaccess as ma

def linkscraper_runner(mailist,classinfo):
    classcode = classinfo[0][0]
    classtime = classinfo[0][1]

    #the program follows a step by step progressive manner of checking if the retrieved mails are possibly the mail with the link for the correct google meet  

    final_body = ''
    first_value = 20
    first_filter = [] #this filter simply checks if there is a google meet link in the obtained mails
    while len(first_filter) == 0:
        for i in mailist:
            if 'meet.google.com' in i.split('/'):
                first_filter.append(i)
        if len(first_filter) == 0: #if the acquired mails has no meet.google.com links, get more
            mailist = ma.get_the_link(classinfo,first_value + 3,rerunner=True)
            first_value += 3
        
    second_filter = [] #this filter tries to check if the subject code or the time of the class is mentioned
    print('second filter')
    for i in first_filter:
        if classtime.lower() in i.lower().split(' '):
            second_filter.append(i)
        if classcode.lower() in i.lower().split(' ') and i not in second_filter:
            second_filter.append(i)
        # classtime is of the format hh:mm AM/PM
        # include cases for h:mm<am/pm> and h<am/pm>
        temp_classtime=classtime
        l=temp_classtime.split(' ')
        t=l[0].split(':')
        t_type1=t[0][1]+':'+t[1]+l[1].lower() # h:mm<am/pm>
        t_type2=t[0][1]+l[1].lower()
        if t_type1 in i.split(' ') and i not in second_filter:
            second_filter.append(i)
        if t_type2 in i.split(' ') and i not in second_filter:
            second_filter.append(i)
        print('\n\n\n')
        print(i)
        print('\n\n\n')


    if len(second_filter) != 0: #if no link passes the second filter, then take the newest first filter pass, or take the first second filter if any links passes the second filter
        final_body = second_filter[0]
    else:
        final_body = first_filter[0]

    final_body = final_body.replace('\r',' ')
    final_body = final_body.replace('\n',' ')

    final_list = final_body.split(' ') #retrieve the link from the body of the mail and return it back to the main function

    link = ''
    for i in final_list:
        if 'meet.google.com' in i.split('/'):
            link = i
    
    return link