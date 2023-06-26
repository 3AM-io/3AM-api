from speak import speak
from speechrecognition import takeCommand
from email_own import sendEmail, email
from wish_init import wishMe
from webCrawl import *
from youtube import youtubeSearch
from wikipedia_search import search_wiki
import time

def responseGen(query : str):
    if 'say my name' in query:
        return 'surya'
    
    if 'read' in query and ('mails' in query or 'mail' in query):
        SEARCH_LIMIT = 5
        for i in range(SEARCH_LIMIT):
            response = "No new mails"
            try:
                length = email.checkMail()
                if length > 0:
                    status = f"You got {length} mails"
                    response = email.readLatest()
                    print(response)
                    speak(status + response)
                    return status + response
                time.sleep(60)
            except Exception as E:
                speak("Retrying please wait")
                length = email.checkMail()
                if length > 0:
                    status = f"You got {length} mails"
                    response = email.readLatest()
                    print(response)
                    speak(status + response)
                    return status + response

    elif 'send' in query and ('email' in query or 'mail' in query):
        try:
            speak("What is the content of the mail")
            content = takeCommand()
            speak("Please Spell the receiver mail id")
            to = takeCommand()
            to_mail = to.replace(" ", "")
            sendEmail(to_mail, content)
            speak("Email has been sent")
            return "Email has been sent"
        except Exception as e:
            speak("Sorry sir. I am not able to send this email")

    # Spotify play
    elif ('song' in query or 'spotify' in query):
        speak("Which song to play")
        song_name = takeCommand()
        playsong(song_name)

    # Youtube play
    elif (('video' in query or 'song' in query) and 'youtube' in query):
        if ('video' in query):
            speak("which video to play")
            query = takeCommand()
            youtubeSearch(query)
            return "Playing " + query
        elif ('song' in query):
            speak("which song to play")
            return "Playing " + query
        
    # Wiki Search
    elif ('wiki' in query or 'wikipedia' in query):
        speak('What to search')
        query = takeCommand()
        result = search_wiki(query)
        speak(result)
        return result
    
    # Site Search
    elif ('go to' in query):
        site = query.replace("go to", "").strip()
        try:
            webbrowser.open_new_tab(site)
            getSummeryFromURL(site)
            return "Opening " + site
        except Exception as e:
            speak("That web page does not exist")
            return "That web page does not exist"

    # Content search will be searched as a final executable
    else:
        searchQuery = query.replace("search", "").strip()
        result = gSearch(searchQuery)
        speak(result)
        return result
