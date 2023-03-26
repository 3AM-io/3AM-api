import os
def playmusic():
    music_dir = "C:\\Users\\rames\\Videos\\y2mate.com - Thee Thalapathy  Thalapathy Vijay  STR  Vamshi Paidipally  Thaman_1080p.mp4"
    songs = os.listdir(music_dir)
    print(songs)    
    os.startfile(os.path.join(music_dir, songs[0]))