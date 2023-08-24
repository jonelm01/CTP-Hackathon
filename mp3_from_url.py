from pytube import YouTube
import os
from pydub import AudioSegment
import spleeter
from IPython.display import Audio

#NOTE: BPM detection uses WAV format, MP3 needs conversion
def getMP3(url):
    try:
        #song = YouTube(url)
        #audio = song.streams.filter(only_audio=True).first()
       # dest = "."
        #out_file = audio.download(output_path=dest)
        #base, ext = os.path.splitext(out_file)
       # new_file = base + '.mp3'
        #os.rename(out_file, new_file)
       # print(song.title + " downloaded to MP3")
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

def splitter(filename): #not sure how to use this yet
    os.system("spleeter separate -o " + "split_songs/ " + filename + ".mp3")
    
#######USE CLI -> spleeter separate -o direct/ filename.mp3


if __name__ == "__main__":
    print("""Begin test
    .
    .
    .
    .
    .
    """)

    splitter("Fireflies")

    
    
