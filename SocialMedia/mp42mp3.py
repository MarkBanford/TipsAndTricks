from moviepy import *
from moviepy.editor import *
import os

path = r'E:\YT\MP3'
fileformat = "mp3"

os.chdir(path)

for file in os.listdir(path):
    file_format = ".mp3"
    if file.endswith(".mp4"):
        full_path = os.path.join(path, file)
        print(full_path)
        videoclip = VideoFileClip(full_path)
        audioclip = videoclip.audio
        mp3_file = full_path[:-3]
        mp3_file = mp3_file + fileformat
        print(mp3_file)
        audioclip.write_audiofile(mp3_file)
        audioclip.close()
        videoclip.close()
