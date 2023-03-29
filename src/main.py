from speak import speak
from speechrecognition import takeCommand
from email_own import sendEmail, email
from wish_init import wishMe
from webCrawl import *
from youtube import youtubeSearch
import time


if __name__=="__main__" :
    
    # Greet
    wishMe()
    query = "read my recent mail"

    # Email client
    if 'read' in query and 'mails' in query or 'mail' in query:
        print("New Mail?")
        while 1:
            try:
                length = email.checkMail()
                if length > 0:
                    speak(f"You got {length} mails")
                    found = email.readLatest()
                    print(found)
                    speak(found)
                    break
                time.sleep(30)
            except Exception as E:
                speak("Retrying please wait")
                length = email.checkMail()
                if length > 0:
                    speak(f"You got {length} mails")
                    found = email.readLatest()
                    print(found)
                    speak(found)

    elif 'send' in query and 'email' in query:
        try:
            speak("What should I say?")
            content = takeCommand()
            speak("What is the receiver email id. Spell it")
            to = takeCommand().lower()
            to_mail = to.replace(" ", "")
            print(to_mail)
            sendEmail(to_mail, content)
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
    
    # Spotify play
    elif ('play songs' in query and 'spotify' in query):
        speak("Which song to play")
        #song_name = takeCommand()
        song_name="Once upon a time"
        playsong(song_name)

    # Youtube play
    elif ('play videos' in query or 'play songs' in query and 'youtube' in query):
        if('play videos' in query):
            speak("which video to play")
            video_query=takeCommand()
            youtubeSearch(video_query)
        elif('play songs' in query):
            speak("which song to play")
            #video_query=takeCommand()
            video_query="Once upon a time"
            youtubeSearch(video_query)
    
    # Content search will be searched as a final executable
    else:
        searchQuery = query
        gSearch(searchQuery)

