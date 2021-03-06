# In construction
from tkinter import *
from tkinter import filedialog
import pytube
import pyperclip


# Function to select the folder in which the videos will be saved
def select_folder():
    global directory_label
    directory = filedialog.askdirectory(title="Escolha onde salvar")
    directory_label.destroy()
    directory_label = Label(frame, text=directory)
    directory_label.grid(row=0, column=0)


# Function to allow the paste button to work
def paste():
    global video_link_entry
    video_link_entry = Entry(frame, font="Helvetica 10")
    video_link_entry.grid(row=1, column=0, ipadx=40, ipady=5)
    video_link_entry.insert(0, pyperclip.paste())


# Function to download videos
def download():
    # Imports for the thumbnail
    from PIL import ImageTk, Image
    import requests
    from io import BytesIO

    # Making the variable that represents the image global so the function can call the image on the GUI
    global img

    # In order to the label that shows which video was downloaded to work without problems, this need to be made
    global status_label
    status_label.destroy()

    # Download video
    video_url = video_link_entry.get()
    youtube = pytube.YouTube(video_url)
    video = youtube.streams.get_highest_resolution()
    directory = directory_label.cget("text")
    video.download(directory)
    status_label = Label(frame, text=f"FINISHED: {youtube.title}")
    status_label.grid(row=3, column=0, columnspan=2, pady=5, padx=10)

    # Thumbnail
    img_url = youtube.thumbnail_url
    response = requests.get(img_url)
    img_data = response.content
    img = Image.open(BytesIO(img_data))
    img = img.resize((300, 200), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    thumbnail_label = Label(frame, image=img, height=200, width=300)
    thumbnail_label.grid(row=4, column=0, columnspan=2, pady=10, padx=10)

    # Increment the list of downloaded videos
    downloaded_video_label = Label(frame2, text=youtube.title)
    downloaded_video_label.pack()


# Main
root = Tk()
root.title("Youtube Videos Download")
root.geometry("700x700+100+100")

frame = LabelFrame(root, padx=5, pady=5)
frame.pack(padx=50, pady=50)

frame2 = LabelFrame(frame, padx=5, pady=5)
frame2.grid(row=5, column=0, columnspan=2)

directory_label = Label(frame, text="Select folder")
directory_label.grid(row=0, column=0)

directory_btn = Button(frame, text="SELECT", height=2, width=10, command=select_folder)
directory_btn.grid(row=0, column=1, pady=10, padx=5)

video_link_entry = Entry(frame, font="Helvetica 10")
video_link_entry.grid(row=1, column=0, ipadx=40, ipady=5)

paste_link_btn = Button(frame, text="PASTE", height=2, width=10, command=paste)
paste_link_btn.grid(row=1, column=1, pady=10, padx=5)

download_video_btn = Button(frame, text="DOWNLOAD", command=download, height=2, width=20)
download_video_btn.grid(row=2, column=0, pady=10, padx=5, columnspan=2)

status_label = Label(frame, text="Download status")
status_label.grid(row=3, column=0, columnspan=2, pady=20, padx=10)

downloaded_label = Label(frame2, text="Downloaded videos:")
downloaded_label.pack()

root.mainloop()
