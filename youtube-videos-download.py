# In construction
from tkinter import *
from tkinter import filedialog
import pytube
import pyperclip


def select_folder():
    global directory_label
    directory = filedialog.askdirectory(title="Escolha onde salvar")
    directory_label.destroy()
    directory_label = Label(frame, text=directory)
    directory_label.grid(row=0, column=0)
    return directory


def paste():
    global video_link_entry
    video_link_entry = Entry(frame, font="Helvetica 10")
    video_link_entry.grid(row=1, column=0, ipadx=40, ipady=5)
    video_link_entry.insert(0, pyperclip.paste())


# Main
root = Tk()
root.title("Youtube Videos Download")
root.geometry("500x500+100+100")

frame = LabelFrame(root, padx=5, pady=5)
frame.pack(padx=50, pady=50)

directory_label = Label(frame, text="Select folder")
directory_label.grid(row=0, column=0)

directory_btn = Button(frame, text="SELECT", height=2, width=10, command=select_folder)
directory_btn.grid(row=0, column=1, pady=10, padx=5)

video_link_entry = Entry(frame, font="Helvetica 10")
video_link_entry.grid(row=1, column=0, ipadx=40, ipady=5)

paste_btn = Button(frame, text="PASTE", height=2, width=10, command=paste)
paste_btn.grid(row=1, column=1, pady=10, padx=5)

download_btn = Button(frame, text="DOWNLOAD", height=2, width=20)
download_btn.grid(row=2, column=0, pady=10, padx=5, columnspan=2)

status_label = Label(frame, text="Download status")
status_label.grid(row=3, column=0, columnspan=2, pady=20, padx=10)

downloaded_label = Label(frame, text="Downloaded videos:")
downloaded_label.grid(row=4, column=0, columnspan=2, pady=20, padx=10)

root.mainloop()
