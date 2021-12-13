#MP4TOMP3
#Filip Rokita
#www.filiprokita.com

import tkinter as tk
from tkinter import filedialog as fd
import os
from moviepy.editor import *

root = tk.Tk()
root.title("MP4TOMP3")
root.geometry("300x100")
root.resizable(False, False)

def getFile():
    filetypes = (
        ("mp4", "*.mp4"),
        ("All files", "*.*")
    )
    global mp4Path; mp4Path = fd.askopenfilename(title="Choose MP4", filetypes=filetypes)
    global mp3Path; mp3Path = mp4Path[:-4]+".mp3"
    convertB["state"] = tk.NORMAL

def convert():
    video = VideoFileClip(os.path.join(mp4Path))
    video.audio.write_audiofile(os.path.join(mp3Path))


getFileB = tk.Button(text="Choose MP4", width="15", command=getFile); getFileB.pack()
convertB = tk.Button(text="Convert to MP3", width="15", stat=tk.DISABLED, command=convert); convertB.pack()
authorL = tk.Label(text="www.filiprokita.com", pady="10"); authorL.pack()


root.mainloop()