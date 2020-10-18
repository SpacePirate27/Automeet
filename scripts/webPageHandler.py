# this opens the browser with the specifc profile
# opens the meeting link
# mute audio
# turn off video
# join the link
# close the meet when the number of participants fall below 10

import selenium 
from scripts.usernotifier import sendNotif
def web_page_opener(link): #the function receives the meet link, the function first needs perform the above mentioned functions and return nothing
    print('test')

def mute_and_stuff(driver):
    join_btn = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[5]/div[3]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]')
    mic_btn = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[5]/div[3]/div/div/div[2]/div/div/div[1]/div/div[4]/div[1]/div/div/div')
    vid_btn = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[5]/div[3]/div/div/div[2]/div/div/div[1]/div/div[4]/div[2]/div/div')
    mic_btn.click()
    sendNotif(4)
    vid_btn.click()
    sendNotif(5)
    join_btn.click()
    sendNotif(0)
    # add code here to detect the time and exit the class after the number of participants has reduced to less thaan 10
    