import eyed3
import os

files = os.listdir()
for _ ,file in enumerate(files):
    if file.lower().endswith('.mp3'):
        audiofile = eyed3.load(file)

        if not audiofile.tag:
            audiofile.initTag()

        title = audiofile.tag.title
        artist = audiofile.tag.artist
        audiofile.tag.clear()
        if title:
            audiofile.tag.title = title
        if artist:
            audiofile.tag.artist = artist

        audiofile.tag.album = "my_album"
        try:
            audiofile.tag.save()
        except NotImplementedError:
            audiofile.tag.clear()
            audiofile.tag.album = "my_album"
            audiofile.tag.save()
