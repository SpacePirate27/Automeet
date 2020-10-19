# sending notifs for all info
# notif for entering into the class
# notif for exiting the class
# notif for loss of internet
# notif for finding the apropriate link
# notif for inability to find the link on mail

from pynotifier import Notification
import sys
import os

notif_title = "Automeet Notification"
notif_desc = ["Entered the class",
        "Exited the class successfully",
        "Found the class link",
        "Audio Muted",
        "Video turned off"]

def notifier(param):
    Notification(
	title=notif_title,
    description=notif_desc[param],
	icon_path=icopath,
	duration=5,
	urgency=Notification.URGENCY_CRITICAL
).send()

def sendNotif(param):
    try:
        notifier(param)
    except:
        print('User Notified')

if __name__ == "__main__":
    icopath = ''
    if sys.platform.startswith('linux'):
        icopath = os.getcwd().split('\\scripts')[0]+'\\automeet.png'
    elif sys.platform.startswith('windows'):
        icopath = os.getcwd().split('\\scripts')[0]+'\\automeet.ico'
    print(icopath)