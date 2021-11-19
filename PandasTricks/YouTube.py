from pytube import YouTube
import os

title = 'https://youtu.be/ADTW-zhnLw4'


def mp4():
    Download_Location = 'D:\\Downloads\\YT\\MP4'

    yt = YouTube(title)

    resolutions = [stream.resolution for stream in yt.streams.filter(progressive=True)]

    max_res = max(resolutions)

    os.chdir(Download_Location)

    download = YouTube(title).streams.filter(res=max_res).first().download()


######################

def mp3(title):
    Download_Location = 'D:\\Downloads\\YT\\MP3'
    yt = YouTube(title)

    os.chdir(Download_Location)

    download = YouTube(title).streams.filter(only_audio=True).first().download()


if __name__ == '__main__':
    mp3(title)
