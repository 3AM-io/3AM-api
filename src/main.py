from speak import speak
from speechrecognition import takeCommand
from email_own import sendEmail
from wish_init import wishMe
from music import playmusic
from webCrawl import *

if __name__=="__main__" :
    # Get query
    wishMe()
    # query = list(takeCommand()).lower()
    query = "say my name"
    
    # Email client
    if 'send' in query and 'email' in query:
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
    

    # Content search will be searched as a final executable
    else:
        searchQuery = query
        gSearch(searchQuery)

