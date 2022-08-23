# Workout-Vid-Selector
My first script written in Python3 that selects random workout videos off different playlists (depending on the day) from the Youtube channel "Workout" and emails them to you on your schedule. 


## What is Workout-Vid-Selector?
Workout-Vid-Selector is a script written in Python3 and was made to automate finding workout videos for a given set workout schedule. Tweak the script as you'd like to fit your ideal workout days and correspoding Workout types, and enjoy automated workout videos delivered to your email on the days you workout! 

## How Does It Work? 
  1. Workout-Vid-Selector will call the sys.platform method to get the OS type. It will then query the date and filter the output with just the day using the OS's respective commands
  2. Depending on which day it is and the schedule you set, it will set the Playlist and Day variables with the corresponding Youtube Playlist ID string, and the days full name respectively
      - The script uses the YouTube channel "Workout" as the default channel. I picked this channel because of how their playlists are laid out by workout types
      - **note:** If you'd like to change the playlists to a different YouTube channel, edit the script to provide your own playlist IDs
  3. WVD will then grab the HTML response of the YouTube playlist by concatenating the Youtube playlist URL and the "playlist" variable (as the data for the URL's list parameter) and filters out the results by the 11 digit video ID using a Regex String. It then puts each ID as a string into a list called "ids"
  4. Randomly selects 3 strings from the "ids" list, while removing the prior selection from the list before each new selection. 
  5. Concatenates the YouTube watch URL with the "video" variables (as the data for the "v" parameter) to produce full-length URL's
  6. Uses the SimpleGmail module to authenticate your gmail account, and send the 3 randomly generated video links to your desired email address.
      - You'll supply the To:/From: email addresses respectively as system arguments. See *usage*
      - SimpleGmail is a Python module that utilizes the Gmail API to send the emails for this script.
      - *See Credits for link to Repo*

## First things, First 
Because SimpleGmail utilizes the Gmail API so we can send emails with the video links, you'll need to setup an OAuthv2 Client ID in the Google Cloud Console using the email that you intend to use to send messages. That way you can authenticate through this script. This can be done at: https://console.cloud.google.com

If you have not done this before, here are some instructions:

  1. Log into your Google Cloud Console with the Gmail account you are using to send emails. Select/Create the project that we will be using to create the OAuth Client-ID (if creating a new project make sure to configure the OAuth consent screen; you only need to set an Application name.)

  2. Click on the Navigation Menu, then select "APIs and Services". Then, click on the Library button and search "Gmail API" Then, select and enable it.

  3. Click on the Credentials tab, then "Create Credentials" --> "OAuth client ID".

  4. Select what kind of application this is for (I chose Desktop App), and name your device. Fill out all necessary information for the credential (e.g. Adding an email account that has permission to utilize the tool. (See https://developers.google.com/identity/protocols/oauth2 for more infomation).

  5. Go back to the credentials screen and click the download icon next to the credential you just created (Which should be under the "OAuth 2.0 Client IDs" section) and choose to download it as a JSON object.

  6. Save this file as "client_secret.json" and place it in the root directory of your where you have this script.

You can find the official docuemntation here: https://support.google.com/googleapi/answer/6158849?hl=en
You should now be good to go!

**note:** The first time you run this script (or create a new Client ID), a browser window will pop up and open with the google login screen. You will authenticate using the Gmail account that you'll be sending the emails from. Once you authenticate, it will create a "gmail_token.json" file that Workout-Vid-Selector script will use for authentication on all future runs (or until the token expires.)

## Installation
 -     git clone https://github.com/D0p3B34t5/Workout-Vid-Selector.git
   -  **Install Git on Windows here:** https://git-scm.com/download/win
  - Edit script to update your scheduled workout days/playlists on lines 62-77 (optional)
![image](https://user-images.githubusercontent.com/98996357/186215613-bbdff411-39df-4a51-ab5b-6322287d8b4c.png)

  
## Usage
    python3 workoutvidselector.py <To Address> <From Address>
- The From address will need to be the gmail account you used to set up the OAuth Client ID
 - **Note:** While this script can be ran on a single run basis, I intended for it to be ran as a scheduled task/cron job on either Windows/Linux respectively and would recommend such for implementation. Set this up however you feel is best.
## Dependencies 
  - simplegmail
    - Linux
      -     pip3 install simplegmail
    - Windows
      -     python3 -m pip install simplegmail
     - https://github.com/jeremyephron/simplegmail

## Credit Where Credit Is Due
SimpleGmail - jeremyephron: https://github.com/jeremyephron/simplegmail


For inspiration with the Randomly generated YouTube URLs:
  - CodeFather: https://www.youtube.com/watch?v=XLDvri9VS50

"Workout" YouTube Channel: https://www.youtube.com/c/WORKOUTBody


