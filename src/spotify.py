import os
import spotipy
import webbrowser
from speak import speak
from dotenv import load_dotenv

load_dotenv()
username = os.environ.get('SPOTIFY_USERNAME')
clientID = os.environ.get('SPOTIFY_CLIENT_ID')
clientSecret = os.environ.get('SPOTIFY_SECRET')

redirect_uri = 'http://google.com/callback/'
oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri)
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
spotifyObject = spotipy.Spotify(auth=token)
user_name = spotifyObject.current_user()
  

def playsong(song_name):
    try:
        results = spotifyObject.search(song_name, 1, 0, "track")
        songs_dict = results['tracks']
        song_items = songs_dict['items']
        song = song_items[0]['external_urls']['spotify']
        webbrowser.open(song)
        speak("The song is opening")
    except:
        speak("No song found")
