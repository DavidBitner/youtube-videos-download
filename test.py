import tkinter as tk
from PIL import ImageTk, Image
import requests
from io import BytesIO


# Show image function
def show():
    global img
    img_url = "https://www.pngfind.com/pngs/m/7-73311_view-sad-pepe-xqc-pepehands-hd-png-download.png"
    response = requests.get(img_url)
    img_data = response.content
    img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
    thumbnail_label = tk.Label(root, image=img)
    thumbnail_label.pack(pady=10, padx=10)


# Main
root = tk.Tk()
root.title("test")
root.geometry("400x400")

show_btn = tk.Button(root, text="SHOW IMAGE", command=show)
show_btn.pack()

root.mainloop()
