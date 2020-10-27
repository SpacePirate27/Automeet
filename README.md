# Automeet
![GitHub](https://img.shields.io/github/license/RamNarayan27/Automeet?logo=Github&style=for-the-badge)
* This application has been developed to automate the task of attending the online class by students.

* Usually, we either open the Google Classroom or check our mails for the meeting link and then login in with the appropriate account into the meeting link.

* This application automated the above process for your convinience.

* And this application will keep running and attending the classes on your behalf


# Installation Instructions

### Enable the google calendar and google classroom api

* Click on the `ENABLE THE GOOGLE CALENDAR API` in https://developers.google.com/calendar/quickstart/python

* Click on `DOWNLOAD CLIENT CONFIGURATION` and save the file where automeet.exe is located

* Go to https://console.developers.google.com and at the top left, select the project you just created (mostly quickstart)

* After opening the project, click on the search bar in the middle and search for "Google Classroom API", Select the top most option from the drop down bar and click on 'Enable API'

* You can then close your browser and run automeet.exe



### Running The Application

* If u get a warning that the app isnt verified, click on `SHOW ADVANCED` and click on `Go to Quickstart` and Allow the requested permissions

* Make sure all the prerun options are ticked, else click on fix

* While entering the timetable, click add to add one class, click on save to save the class and click on next day to go to the next day

* Chrome needs to be installed to use the program, support for other browsers will be added later

* Once you finish setting up, the program should run on its own and be able to attend classes, if u have any issues, send an email to 'projectautomeet@gmail.com' and attach log.txt 

## To run python program

* Install the required libraries
```bash
pip install -r requirements.txt
```