from pytube import YouTube

#NOTE: BPM detection uses WAV format, MP3 needs conversion
def getMP3(url):
    try:
        song = YouTube(url)
        stream = song.streams.filter(only_audio=True).first()
        stream.download(filename=f"{song.title}.mp3")
        print("Song downloaded to MP3")
        return True

    except KeyError:
        print("Unable to retrieve stream")
        return False
        #Bad url

