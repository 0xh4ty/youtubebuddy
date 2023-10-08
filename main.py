from tkinter import *
import re
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title("Youtube Buddy")

Label(root, text='Youtube Video Downloader', font='arial 20 bold').pack()

##enter link
link = StringVar()

Label(root, text='Paste Link Here:', font='arial 15 bold').place(x=160, y=60)
link_enter = Entry(root, width=70, textvariable=link)
link_enter.place(x=32, y=90)

# function to download video
def Downloader():
    link_text = str(link.get())
    if re.match(r'^https://', link_text):
        url = YouTube(link_text)
        video = url.streams.get_highest_resolution()
        video.download()
        Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)
    else:
        Label(root, text = 'INSECURE URL', font = 'arial 15').place(x= 180 , y = 210)

# function to paste clipboard contents on right click
def right_click(event):
    event.widget.event_generate('<Control-v>')

link_enter.bind('<Button-3>', right_click)

Button(root, text='DOWNLOAD', font='arial 15 bold', bg='pale violet red', padx=2, command=Downloader).place(x=180, y=150)

root.mainloop()
