# sending notifs for all info
# notif for entering into the class
# notif for exiting the class
# notif for loss of internet
# notif for finding the apropriate link
# notif for inability to find the link on mail

import sys
import os

notif_title = "Automeet Notification"
notif_desc = ["Entered the class",
        "Exited the class successfully",
        "Found the class link",
        "",
        "Audio and Video turned off"]

def sendNotif(param):
    from notifypy import Notify
    notification = Notify()
    notification.title = 'Info'
    notification.message = notif_desc[param]
    notification.application_name = 'AutoMeet'
    notification.icon = os.getcwd().split('\\scripts')[0]+'\\automeet.png'

    notification.send()
