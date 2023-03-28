from speak import speak
from speechrecognition import takeCommand
from email_own import sendEmail, email
from wish_init import wishMe
from music import playmusic
from webCrawl import *
# from spotify import playsong

import time

if __name__=="__main__" :
    # Get query
    wishMe()
    # query = list(takeCommand()).lower()
    query = "read my new mails"
    
    # Email client
    if 'read' in query and 'mails' in query:
        print("New Mail?")
        while 1:
            length = email.checkMail()
            if length > 0:
                speak(f"You got {length} mails")
                print(email.readLatest())
                break
            time.sleep(60)

    elif 'send' in query and 'email' in query:
        try:
            speak("What should I say?")
            content = takeCommand()
            # content="hi"
            speak("What is the receiver email id")
            to = takeCommand()
            # to="rameshnagarajan09@gmail.com"
            sendEmail(to, content)
            print("Email has been sent")
            speak("Email has been sent")
        except Exception as e:
            print(e)
            speak("Sorry sir. I am not able to send this email")
            
    # Site Search
    elif ('go to' in query):
        site = query.replace("go to", "").strip()
        try:
            getSummeryFromURL(site)
        except Exception as e:
            speak("That web page does not exist")
    
    elif 'play music' in query:
        speak("Which song to play")
        song_name = takeCommand()
        playsong(song_name)

    # Content search will be searched as a final executable
    else:
        searchQuery = query
        gSearch(searchQuery)

