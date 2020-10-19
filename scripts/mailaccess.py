import imaplib
import email
from email.header import decode_header
import webbrowser
import os
import pickle
import scripts.linkScraper as lis

def get_the_link(nextclass,no_of_mails,rerunner=False):

    dirc = os.getcwd()+'\\user_mail_creds\\'+'user_name'+'.pkl'

    usrname = open(os.getcwd()+'\\user_mail_creds\\'+'user_name'+'.pkl',"rb")
    username = pickle.load(usrname)
    passw = open(os.getcwd()+'\\user_mail_creds\\'+'password'+'.pkl',"rb")
    password = pickle.load(passw)
    usrname.close()
    passw.close()

    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    imap.login(username, password)
    status, messages = imap.select("INBOX")
    messages = int(messages[0])
    N = no_of_mails

    list_of_mail = []

    for i in range(messages, messages-N, -1):
        res, msg = imap.fetch(str(i), "(RFC822)")
        body = ''
        for response in msg:
            if isinstance(response, tuple):
                msg = email.message_from_bytes(response[1])
                if msg.is_multipart():
                    for part in msg.walk():
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))
                        try:
                            body = part.get_payload(decode=True).decode()
                        except:
                            pass
                        if content_type == "text/plain":
                            list_of_mail.append(body)
                else:
                    content_type = msg.get_content_type()
                    body = msg.get_payload(decode=True).decode()
                    if content_type == "text/plain":
                        list_of_mail.append(body)
    imap.close()
    imap.logout()

    if rerunner == False:
        final_link = lis.linkscraper_runner(list_of_mail,nextclass)
        return final_link
    else:
        return list_of_mail