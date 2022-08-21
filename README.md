# Workout-Vid-Selector
A simple script written in Python3 that selects random videos off playlists from the Youtube channel "Workout" and emails them to you on your schedule. 


## What is Workout-Vid-Selector?
Workout-Vid-Selector is a script written in Python3 and was made to automate finding workout videos for a given set workout schedule. Tweak the script as you'd like to fit your ideal workout days and correspoding Workout types, and enjoy automated workout videos delivered to your email on the days you workout! 

## How Does It Work? 
  - Workout-Vid-Selector will call the sys.platform method to get the OS type. It will then query the date and filter the output with just the day using the OS's respective commands
  - Depending on which day it is and the schedule you set, it will set the Playlist and Day variables with the corresponding Youtube Playlist ID string, and the days Full name respectively
    - The script uses the YouTube channel "Workout" as the default channel. I picked this playlist because of how their playlists are laid out by workout types
      - **note:** If you'd like to change the playlists to a different YouTube channel, edit the script to provide your own playlist IDs
  - WVD will then grab the HTML response of the YouTube playlist by concatenating the Youtube playlist URL and the "playlist" variable (as the data for the URL's list parameter) and filters out the results by the 11 digit video ID using a Regex String. It then puts each ID as a string into a list called "ids"
  - Randomly selects 3 strings from the "ids" list, while removing the prior selection from the list before each new selection. 
  - Concatenates the YouTube watch URL with the "video" variables (as the data for the "v" parameter) to produce full-length URL's
  - Uses the SimpleGmail module to authenticate your gmail account, and send the 3 randomly generated video links to your desired email address.

## First things, First 
Before you begin, you'll need to setup an OAuthv2 Client-ID in the Google Cloud Console using the email that you intend to use to send messages. That way you can authenticate through this script. This can be done at: https://console.cloud.google.com

If you have not done this before, you can follow this guide:

  1. Log into your Google Cloud Console with the Gmail account you are using to send emails. Select/create the project that we will be using this for (if creating a new project make sure to configure the OAuth consent screen; you only need to set an Application name)

  2. Click on the "Dashboard" tab, then "APIs and Services". Then, click on the Library button and search "Gmail API" Then, select and enable it.

  3. Click on the Credentials tab, then "Create Credentials" --> "OAuth client ID".

  4. Select what kind of application this is for (I chose Desktop App), and name your device. Fill out all necessary information for the credential (e.g. Adding an email account that has permission to utilize the tool. See https://developers.google.com/identity/protocols/oauth2 for more infomation).

  5. Back on the credentials screen, click the download icon next to the credential you just created and choose to download it as a JSON object.

  6. Save this file as "client_secret.json" and place it in the root directory of your application. (The Gmail class takes in an argument for the name of this file if you choose to name it otherwise.)


You are now good to go!

**note:** The first time you run this script, a browser window will pop up via Google and you will authenticate using the gmail account that you'll be sending the emails from. Once you authenticate, it will create a "gmail_token.json" file that Workout-Vid-Selector will use for authentication on all future runs (until the token expires.) 

## Installation
      git install https://github.com/D0p3B34t5/Workout-Vid-Selector.git
  - Edit script to update your scheduled workout days/playlists on lines 33-44 (optional)
![image](https://user-images.githubusercontent.com/98996357/185812114-016f55c1-a3d3-49a4-b5a7-18d2b0298fbd.png)
  - Provide To/From email addresses on lines 64 & 65
![image](https://user-images.githubusercontent.com/98996357/185812654-114eba59-9c25-4c8a-a25f-67ceb3311d3b.png)
  
## Usage
  - I wrote this script to run as a scheduled task and is what I'd recommend for implementation. Set this up however you feel is best. 
  - For single use:
    -     sudo python3 workoutvidselector.py
      
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


