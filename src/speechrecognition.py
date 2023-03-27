import speech_recognition as sr

query = ""
def takeCommand():
     '''
        recognise the mic from the 
     '''
     r = sr.Recognizer()
     with sr.Microphone() as source:
         global query
         print("Listening...")
         r.pause_threshold = 1
         audio = r.listen(source)
         try:
            print("Please wait!")    
            query= r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
         except:
             print("No voice found")    
         #query_new = query  
     return query