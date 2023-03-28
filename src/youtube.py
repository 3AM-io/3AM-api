from youtubesearchpython import VideosSearch
from speak import speak
import webbrowser

def youtubeSearch(searchQuery:str) -> bool:
    try:
        results = VideosSearch(searchQuery, limit=2)

        results_dict = results.result()
        url= results_dict['result'][0]['link']

        webbrowser.open(url)

        speak("The song is opening")

        return True
    except Exception as E:
        return False
