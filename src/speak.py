import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') #gets you the details of the current voice
engine.setProperty('voice', voices[1].id)  # 0-male voice , 1-female voice


def speak(audio):  
     
    engine.say(audio)    
    engine.runAndWait()

