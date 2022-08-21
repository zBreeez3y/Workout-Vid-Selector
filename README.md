# Workout-Vid-Selector
A simple script written in Python3 that selects random videos off playlists from the Youtube Channel "Workout" and emails them to you on your schedule. 


## What is Workout-Vid-Selector?
Workout-Vid-Selector is a script written in Python3 and was made to automate finding workout videos for a given set workout schedule. Tweak the script as you'd like to fit your ideal workout days and correspoding Workout types, and enjoy automated workout videos delivered to your email on the days you workout! 

## Pre-Installation
Before you begin, you'll need to setup an OAuthv2 application in Google Cloud so you can authenticate through this script.

This can be done at: https://console.developers.google.com/apis/credentials. For those who haven't created a credential for Google's API, after clicking the link above (and logging in to the appropriate account),

  1. Select/create the project that this authentication is for (if creating a new project make sure to configure the OAuth consent screen; you only need to set an Application name)

  2. Click on the "Dashboard" tab, then "Enable APIs and Services". Search for Gmail and enable.

  3. Click on the Credentials tab, then "Create Credentials" > "OAuth client ID".

  4. Select what kind of application this is for, and give it a memorable name. Fill out all necessary information for the credential (e.g., if choosing "Web Application" make sure to add an Authorized Redirect URI. See https://developers.google.com/identity/protocols/oauth2 for more infomation).

  5. Back on the credentials screen, click the download icon next to the credential you just created to download it as a JSON object.

  6. Save this file as "client_secret.json" and place it in the root directory of your application. (The Gmail class takes in an argument for the name of this file if you choose to name it otherwise.)

You are now good to go!

**note:** The first time you run this script, an authentication window will pop up via Google using the information off the OAuthv2 Client-ID that you created and downloaded. Once you authenticate, it will create a "gmail_token.json" file that it will use for authentication on all future runs (until the token expires.) 

## Installation
      git install https://github.com/D0p3B34t5/Workout-Vid-Selector.git
      
## Dependencies 
  - simplegmail
      -     pip3 install simplegmail
     - https://github.com/jeremyephron/simplegmail
