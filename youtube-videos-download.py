import tkinter as tk
from tkinter import filedialog, Text
import os
import pytube


def download_video(directory='C:/Users/David/Desktop/Videos', video_url='0'):
    while True:
        if video_url == '0':
            break
        youtube = pytube.YouTube(video_url)
        video = youtube.streams.get_highest_resolution()
        video.download(directory)


def input_video_url():
    video_url = input()
    return video_url


# Main
vu = input_video_url()
root = tk.Tk()

canvas = tk.Canvas(root, height=200, width=200, bg='black')
canvas.pack()

frame = tk.Frame(root, bg='white')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

youtube_url_label = tk.Label(root, text='Youtube URL: ')
youtube_url_label.pack()
entry = tk.Entry(root)
entry.pack()

download = tk.Button(root, text='Download', padx=10, pady=5, fg='white', bg='black', command=download_video())
download.pack()

root.mainloop()
