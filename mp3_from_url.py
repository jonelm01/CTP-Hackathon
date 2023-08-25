from pytube import YouTube
from pythumb import Thumbnail
import os
from pydub import AudioSegment
import spleeter
from IPython.display import Audio
import librosa

#NOTE: BPM detection uses WAV format, MP3 needs conversion

#Fetch/download .mp3 of YouTube video at provided URL
def getMP3andThumbnail(url):
    try:
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()
        destination = '.'
        out_file = video.download(output_path=destination)
        base, ext = os.path.splitext(out_file)
        #base.replace(" ", "_")
        name = base.replace(" ", "-")
        print(name)
        new_file = name + '.mp3'
        os.rename(out_file, new_file)
        print(yt.title + " has been successfully downloaded.")

        img = Thumbnail(url)
        img.fetch()
        img.save('.', name)

        return name, yt.title #path and song name

    except KeyError:
        print("Unable to retrieve stream")
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


#Splits "file" song at "path" into file_accompaniment.wav and file_vocals.wav
def splitter(path, file): 
    file = file.replace(" ", "-")
    print(path)
    print(file)
    os.system("spleeter separate -o " + "split_songs/ " + path + ".mp3")
    #os.system("cd split_songs")
    os.system("mv ./split_songs/" + file + "/" + "accompaniment.wav " + "./split_songs/" + file + "/" + file + "_accompaniment.wav")
    os.system("mv ./split_songs/" + file + "/" + "vocals.wav " + "./split_songs/" + file + "/" + file + "_vocals.wav")
    #os.system("mv vocals.wav " + filename + "_vocals.wav")
#######USE CLI -> spleeter separate -o direct/ filename.mp3


#UNTESTED
#Clear songs in directory on refresh, open, close, or manual refresh button
def clearSongs():
    os.system("rm -r /split_songs")


#Estimate BPM of "filename" song
#More accurate than bpm_detection.py, but still noticably off
def BPMest(filename):
    audio_file = librosa.load(filename)
    y, sr = audio_file
    bpm, frames = librosa.beat.beat_track(y=y, sr=sr)
    print("Estimated bpm: " + bpm)
    

#Pass the song whose speed will change, its BPM, and the BPM of the dependent song
def playbackSpeed(filename, mainBPM, modBPM):
    audio = AudioSegment.from_file(filename, format="wav")
    mod = float(mainBPM / modBPM)
    audio.speedup(playbackSpeed=mod)

if __name__ == "__main__":
    print("""Begin test
    .
    .
    .
    .
    .
    """)

    #name, base = getMP3andThumbnail("https://www.youtube.com/watch?v=NUUpIuspG5E")
    #splitter(name, base)
    BPMest("Yellowman_accompaniment.wav")

    
    
