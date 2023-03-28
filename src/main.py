from speak import speak
from speechrecognition import takeCommand
from email_own import sendEmail
from wish_init import wishMe
from webCrawl import *
from spotify import playsong
from youtube import youtubeSearch

if __name__=="__main__" :
    
    # Greet
    wishMe()

    # Get query
    #query = list(takeCommand()).lower()
    
    query = "play songs"

    # Email client
    if 'send' in query and 'email' in query:
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

