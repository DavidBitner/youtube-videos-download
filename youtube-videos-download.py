# In construction
from tkinter import *

# Main
root = Tk()
root.title("Youtube Videos Download")
root.geometry("500x500+200+200")

frame = LabelFrame(root, padx=5, pady=5)
frame.pack(padx=100, pady=100)

directory_label = Label(frame, text="Select folder")
directory_label.grid(row=0, column=0)

directory_btn = Button(frame, text="SELECT")
directory_btn.grid(row=0, column=1)

video_link_entry = Entry(frame)
video_link_entry.grid(row=1, column=0)

paste_btn = Button(frame, text="PASTE")
paste_btn.grid(row=1, column=1)

download_btn = Button(frame, text="DOWNLOAD")
download_btn.grid(row=2, column=0)

status_label = Label(frame, text="Download status")
status_label.grid(row=3, column=0)

downloaded_label = Label(root, text="Downloaded videos:")
downloaded_label.pack()

root.mainloop()
