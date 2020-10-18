# sending notifs for all info
# notif for entering into the class
# notif for exiting the class
# notif for loss of internet
# notif for finding the apropriate link
# notif for inability to find the link on mail

from pynotifier import Notification

notif_title = "Automeet Notification"
notif_desc = ["Entered the class successfully",
        "Exited the class successfully",
        "Loss of internet",
        "Found the class link",
        "Unable to find meeting link"]
def sendNotif(param):
    Notification(
	title=notif_title,
    description=notif_desc[param],
	icon_path='Paomedia-Small-N-Flat-Bell.ico',
	duration=5,
	urgency=Notification.URGENCY_CRITICAL
).send()

