#!/usr/bin/python3

import subprocess
import sys
import urllib.request 
import re
import random
from simplegmail import Gmail


def workout_vid_selector():
	"""
	
	Workout-Vid-Selector
	By: D0p3B34t5
	
	"""
	
#Check for OS
os = sys.platform
if "win" in os:
	os = "Win"
else:
	os = "Lin"

#Run respective OS command to get systems local date, and filter out just the day
if os=="Win":
	date = subprocess.getoutput("@echo OFF & FOR /F \"tokens=1 delims= \" %G in ('date /t') do echo %G")
elif os=="Lin":
	date = subprocess.getoutput("date | cut -d ' ' -f 1")

#Set playlist and day variables based on local date
if date=="Tue":
	playlist = "PLmw9rXTuLboAHKq8nMec-brq4ol35EKlS" #Arm Workout Exercises Playlist
	day = "Tuesday"
elif date=="Wed":
	playlist = "PLmw9rXTuLboDG2fXmMnff2XURFoPXMKAi" #Legs Workout Exercises Playlist
	day = "Wednesday"
elif date=="Fri":
	playlist = "PLmw9rXTuLboD_vybrb6he9wPRrCRAJDCe" #ABS Workout Exercises Playlist
	day = "Friday"
elif date=="Sun":
	playlist = "PLmw9rXTuLboB6iXwx3X_yVyd4OyCnQod5" #Full Body Workout Playlist
	day = "Sunday"
else: 
	exit()

#Gets HTML of specific playlist through HTTP request, filters out video ID's with Regex string and creates a list, then pulls 3 random videos from the created list. 
url = "https://www.youtube.com/playlist?list=" + playlist
request = urllib.request.urlopen(url)
ids = re.findall(r"watch\?v=(\S{11})", request.read().decode())
video1 = random.choice(ids)
ids.remove(video1) #Remove video1 from list
video2 = random.choice(ids)
ids.remove(video2) #Remove video2 from list
video3 = random.choice(ids)
final1 = "https://www.youtube.com/watch?v=" + video1
final2 = "https://www.youtube.com/watch?v=" + video2
final3 = "https://www.youtube.com/watch?v=" + video3

#Email the 3 random youtube videos for the day
gmail = Gmail()
params = {
	"to": "",
	"sender": "",
	"subject": "{} Workouts".format(day),
	"msg_html": "<h1>It's {} and it's a workout day! Here are your workouts for today:</h1> <h2>Video #1</h2> <href>{}</href> <h2>Video #2</h2> <href>{}</href> <h2>Video #3</h2> <href>{}</href>".format(day, final1, final2, final3),
	"signature": True
}
message = gmail.send_message(**params)

def credits():	
	"""
	
	Giving credit where credit is due: 
	
	https://www.youtube.com/c/WORKOUTBody - Workout YouTube Channel
	https://www.youtube.com/watch?v=XLDvri9VS50 - Code Father; Inspiration for URL generation
	https://github.com/jeremyephron/simplegmail - SimpleGmail Python Module
	
	"""
