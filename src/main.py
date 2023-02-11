import speech_recognition as sr
def takeCommand():
    #It takes microphone input from the user and returns string output    
     r = sr.Recognizer()
     with sr.Microphone() as source:
         print("Listening...")
         r.pause_threshold = 1
         audio = r.listen(source)

         print("Recognizing...")    
         query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
         print(f"User said: {query}\n")  #User query will be printed.    
        
     return query

takeCommand()
