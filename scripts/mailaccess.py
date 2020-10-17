import imaplib
import email
from email.header import decode_header
import webbrowser
import os
import pickle

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
N = 5

list_of_mail = []

for i in range(messages, messages-N, -1):
    res, msg = imap.fetch(str(i), "(RFC822)")
    for response in msg:
        if isinstance(response, tuple):
            msg = email.message_from_bytes(response[1])
            if msg.is_multipart():
                # iterate over email parts
                for part in msg.walk():
                    # extract content type of email
                    content_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition"))
                    try:
                        # get the email body
                        body = part.get_payload(decode=True).decode()
                    except:
                        pass
                    if content_type == "text/plain":
                        # print text/plain emails and skip attachments
                        list_of_mail.append(body)
            else:
                # extract content type of email
                content_type = msg.get_content_type()
                # get the email body
                body = msg.get_payload(decode=True).decode()
                if content_type == "text/plain":
                    # print only text email parts
                    list_of_mail.append(body)
imap.close()
imap.logout()

for i in list_of_mail:
    print(i)
    print('\n\n')
    print('*********************')
    print('\n\n')