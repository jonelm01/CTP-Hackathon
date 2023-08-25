from pytube import YouTube
import os
from pydub import AudioSegment
import spleeter
from IPython.display import Audio

#NOTE: BPM detection uses WAV format, MP3 needs conversion
#Fetch/download .mp3 of YouTube video at provided URL
def getMP3(url):
    try:
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()
        destination = '.'
        out_file = video.download(output_path=destination)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        print(yt.title + " has been successfully downloaded.")
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


#Splits "filename" song into filename_accompaniment.wav and filename_vocals.wav
def splitter(filename): 
    os.system("spleeter separate -o " + "split_songs/ " + filename + ".mp3")
    os.system("mv accompaniment.wav " + filename + "_accompaniment.wav")
    os.system("mv vocals.wav " + filename + "_vocals.wav")
#######USE CLI -> spleeter separate -o direct/ filename.mp3


#UNTESTED
#Clear songs in directory on refresh, opem, close, or manual refresh button
def clearSongs():
    os.system("rm -r /split_songs")


def merger(song1, song2):
    #merge 
    return 1


if __name__ == "__main__":
    print("""Begin test
    .
    .
    .
    .
    .
    """)

    #splitter("Fireflies")

    
    
