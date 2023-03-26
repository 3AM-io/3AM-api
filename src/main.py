from speak import speak
from speechrecognition import takeCommand
from email_own import sendEmail
from wish_init import wishMe
from music import playmusic
if __name__=="__main__" :
    wishMe()
    #speak("Listening")
    #query = takeCommand()
    # print(query)
    query = "send a email"
    #query="play music"
    speak(f"The recognized text is{query}")
    if 'send a email' in query:
        try:
            speak("What should I say?")
            #content = takeCommand()
            content="hi"
            speak("What is the receiver email id")
            #to = takeCommand()    
            to="rameshnagarajan09@gmail.com"
            sendEmail(to, content)
            print("Email has been sent")
            speak("Email has been sent")
        except Exception as e:
            print(e)
            speak("Sorry sir. I am not able to send this email")
    # elif 'play music' in query:
    #     playmusic()