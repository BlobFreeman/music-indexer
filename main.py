import os
from tkinter.filedialog import askdirectory
import mutagen
from mutagen.flac import FLAC
from mutagen.id3 import ID3
from mutagen.mp4 import MP4

list_of_song = []

def directorychooser():
    directory = askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".flac"):
            realdir = os.path.realpath(files)
            audiofile = FLAC(realdir)
            # title, artist, album
            title = ''.join(audiofile['title'])
            artist = ''.join(audiofile['artist'])
            album = ''.join(audiofile['album'])
            flac_metadata = {'title': title, 'artist': artist, 'album': album}
            list_of_song.append(flac_metadata)
        elif files.endswith(".mp3"):
            realdir = os.path.realpath(files)
            audiofile = ID3(realdir)
            # TIT2, TPE1, TALB
            title = audiofile['TIT2'].text[0]
            artist = audiofile['TPE1'].text[0]
            album = audiofile['TALB'].text[0]
            mp3_metadata = {'title': title, 'artist': artist, 'album': album}
            list_of_song.append(mp3_metadata)
        elif files.endswith(".ogg"):
            realdir = os.path.realpath(files)
            audiofile = mutagen.File(realdir)
            # title, artist, album
            title = ''.join(audiofile['title'])
            artist = ''.join(audiofile['artist'])
            album = ''.join(audiofile['album'])
            ogg_metadata = {'title': title, 'artist': artist, 'album': album}
            list_of_song.append(ogg_metadata)
        elif files.endswith(".mp4"):
            realdir4 = os.path.realpath(files)
            audiofile_3 = MP4(realdir4)
            # title, artist, album
            title = audiofile_3['title']
            artist = audiofile_3['artist']
            album = audiofile_3['album']
            mp4_metadata = {'title': title, 'artist': artist, 'album': album}
            list_of_song.append(mp4_metadata)


directorychooser()

print(list_of_song)
