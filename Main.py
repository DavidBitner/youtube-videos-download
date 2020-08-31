import pytube
import tkinter as tk
from tkinter import filedialog


def choose_directory():
    root = tk.Tk()
    root.withdraw()
    directory = filedialog.askdirectory(initialdir="C://Users//David//Desktop", title="Escolha onde salvar")
    return directory


def download(directory):
    while True:
        video_url = input('Youtube URL: [0 to end] ')
        if video_url == '0':
            break
        youtube = pytube.YouTube(video_url)
        print(f'Downloading: {youtube.title}')
        video = youtube.streams.get_highest_resolution()
        video.download(directory)
        print('Download finished')


# main
d = choose_directory()
download(d)
print('Goodbye')
