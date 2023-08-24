from pytube import YouTube
import os
from pydub import AudioSegment
import spleeter

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
        print("Enter the destination address (leave blank to save in current directory)")
        destination = str(input(" ")) or '.'
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
    song = spleeter.Spleeter()
    vocals, instruments = song.seperate(filename)

    vocals.write("vocals.wav")
    instruments.write("instruments.wav")


if __name__ == "__main__":
    print("""Begin test
    .
    .
    .
    .
    .
    """)
    getMP3("https://www.youtube.com/watch?v=psuRGfAaju4")
