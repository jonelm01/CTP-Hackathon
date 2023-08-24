from pytube import YouTube
from os import path
from pydub import AudioSegment
import spleeter

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


def MP3toWav(MP3_filename): #name of file without .mp3 extension
    inFile = f"{MP3_filename}.mp3"
    outFile = f"{MP3_filename}.wav"

    try:
        sound = AudioSegment.from_mp3(inFile)
        sound.export(outFile, format="wav")
        print("Successfully converted to WAV format")
        return True

    except KeyError:
        print("Unable to convert MP3 file")
        return False

def splitter(filename): #not sure how to use this yet
    song = spleeter.Spleeter()
    vocals, instruments = song.seperate(filename)

    vocals.write("vocals.wav")
    instruments.write("instruments.wav")
