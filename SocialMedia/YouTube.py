from pytube import YouTube
import os

title = 'https://youtu.be/qswwVzMkLns'


def mp4():
    Download_Location = 'E:\\YT\\MP4'

    yt = YouTube(title)

    resolutions = [stream.resolution for stream in yt.streams.filter(progressive=True)]
    print(resolutions)

    max_res = max(resolutions)

    os.chdir(Download_Location)

    download = YouTube(title).streams.filter(res=max_res).first().download()


######################

def mp3():
    Download_Location = 'E:\\YT\\MP3'
    yt = YouTube(title)

    os.chdir(Download_Location)

    download = YouTube(title).streams.filter(only_audio=True).first().download()
    #yt.streams.get_audio_only().download(output_path=Download_Location, filename=yt.title)


if __name__ == '__main__':
    #mp3()
    mp4()
