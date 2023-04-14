from speak import speak
import wikipedia

def search_wiki(query):
    speak('Searching Wikipedia')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=5) 
    speak("According to Wikipedia")
    return results

# Thanks to wikipedia api <https://www.wikipedia.org/>