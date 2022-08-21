# Workout-Vid-Selector
A simple script written in Python3 that selects random videos off playlists from the Youtube Channel "Workout" and emails them to you on your schedule. 


## What is Workout-Vid-Selector?
Workout-Vid-Selector is a script written in Python3 and was made to automate finding workout videos for a given set workout schedule. Tweak the script as you'd like to fit your ideal workout days and correspoding Workout types, and enjoy automated workout videos delivered to your email on the days you workout! 

## How Does It Work? 
  - Workout-Vid-Selector will call the sys.platform method to get the OS type. It will then query the date and filter the output with just the day using the OS's respective commands
  - Depending on which date it is, it will set the Playlist and Day variables with the corresponding Youtube Playlist ID string, and the days Full name respectively
      - **note:** If you'd like to change the playlists to a different YouTube channel, edit the script to provide your own playlist IDs.
  - WVD will then grab the HTML response of the YouTube playlist by concatenating the Youtube playlist URL and the playlist variable (as the data for the URL's list parameter) and filters out the results by the 11 digit video ID (using a Regex String.) It then puts each ID as a string into a list called "ids"
  - Randomly selects 3 strings from the ids list, while removing the prior selection before each new one. 
  - Concatenates the YouTube watch URL with the final (full-length URL) variable 
  - Uses the SimpleGmail module to authenticate your gmail account, and send the 3 randomly generated video links to your desired email address.

## Pre-Installation
Before you begin, you'll need to setup an OAuthv2 application in the Google Cloud Console using the email that you intend to use to send messages. That way you can authenticate through this script. This can be done at: https://console.cloud.google.com

This can be done at: https://console.developers.google.com/apis/credentials. For those who haven't created a credential for Google's API, after clicking the link above (and logging in to the appropriate account),

  1. Select/create the project that this authentication is for (if creating a new project make sure to configure the OAuth consent screen; you only need to set an Application name)

  2. Click on the "Dashboard" tab, then "Enable APIs and Services". Search for Gmail and enable.

  3. Click on the Credentials tab, then "Create Credentials" > "OAuth client ID".

  4. Select what kind of application this is for, and give it a memorable name. Fill out all necessary information for the credential (e.g. Adding an email account that has permission to utilize the tool. See https://developers.google.com/identity/protocols/oauth2 for more infomation).

  5. Back on the credentials screen, click the download icon next to the credential you just created to download it as a JSON object.

  6. Save this file as "client_secret.json" and place it in the root directory of your application. (The Gmail class takes in an argument for the name of this file if you choose to name it otherwise.)

You are now good to go!

**note:** The first time you run this script, an authentication window will pop up via Google using the information off the OAuthv2 Client-ID that you created and downloaded. You will sign in using the gmail account that you'll be sending the emails from. Once you authenticate, it will create a "gmail_token.json" file that it will use for authentication on all future runs (until the token expires.) 

## Installation
      git install https://github.com/D0p3B34t5/Workout-Vid-Selector.git
      
## Dependencies 
  - simplegmail
      -     pip3 install simplegmail
     - https://github.com/jeremyephron/simplegmail
