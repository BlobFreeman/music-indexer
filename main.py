import os
from tkinter.filedialog import askdirectory
import mutagen
from mutagen.flac import FLAC
from mutagen.id3 import ID3
from mutagen.mp4 import MP4


def directorychooser():
    directory = askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".flac"):
            flac_metadata = ['title', 'artist', 'album']
            realdir = os.path.realpath(files)
            audiofile = FLAC(realdir)
            # title, artist, album
            flac_metadata.insert(1, audiofile['title'])
            flac_metadata.insert(3, audiofile['artist'])
            flac_metadata.insert(5, audiofile['album'])
            print(flac_metadata)
        elif files.endswith(".mp3"):
            mp3_metadata = ['title', 'artist', 'album']
            realdir2 = os.path.realpath(files)
            audiofile_1 = ID3(realdir2)
            # TIT2, TPE1, TALB
            mp3_metadata.insert(1, audiofile_1['TIT2'].text[0])
            mp3_metadata.insert(3, audiofile_1['TPE1'].text[0])
            mp3_metadata.insert(5, audiofile_1['TALB'].text[0])
            print(mp3_metadata)
        elif files.endswith(".ogg"):
            ogg_metadata = ['title', 'artist', 'album']
            realdir3 = os.path.realpath(files)
            audiofile_2 = mutagen.File(realdir3)
            # title, artist, album
            ogg_metadata.insert(1, audiofile_2['title'])
            ogg_metadata.insert(3, audiofile_2['artist'])
            ogg_metadata.insert(5, audiofile_2['album'])
            print(ogg_metadata)
        elif files.endswith(".mp4"):
            mp4_metadata = ['title', 'artist', 'album']
            realdir4 = os.path.realpath(files)
            audiofile_3 = MP4(realdir4)
            # title, artist, album
            mp4_metadata.insert(1, audiofile_3['title'])
            mp4_metadata.insert(3, audiofile_3['artist'])
            mp4_metadata.insert(5, audiofile_3['album'])
            print(mp4_metadata)


directorychooser()
