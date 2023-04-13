"""
Youtube Downloader
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from toga.style.pack import *
import re
from pytube import YouTube
import os


class YoutubeBuddy(toga.App):

    def startup(self):
        
        main_box = toga.Box(style=Pack(direction=COLUMN))

        name_label = toga.Label(
        "Youtube Buddy",
        style=Pack(
            font_size=24,
            padding=(10, 5),
            color='red',
            font_family='Aachen Bold')
        )
    
        paste_label = toga.Label(
        "Paste the link here:",
        style=Pack(
            font_size=15,
            padding=(8, 5),
            color='black',)
        )


        self.downloaded_label = toga.Label(
            "",
            style=Pack(
                font_size=15,
                padding=(10, 5),
                color='black',
            )
        )

        self.insecure_label = toga.Label(
            "",
            style=Pack(
                font_size=15,
                padding=(10, 5),
                color='black',
            )
        )

        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)

        paste_box = toga.Box(style=Pack(direction=COLUMN, padding=5))
        paste_box.add(paste_label)
        paste_box.add(self.downloaded_label)
        paste_box.add(self.insecure_label)


        self.paste_input = toga.TextInput(style=Pack(flex=1))
        paste_box.add(self.paste_input)

        download = toga.Button(
            "Download",
            on_press=self.Downloader,
            style=Pack(padding=5)
        )

        main_box.add(name_box)
        main_box.add(paste_box)
        main_box.add(download)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()



    def Downloader(self, widget):
        link_text = str(self.paste_input.value)
        if re.match(r'^https://', link_text):
            url = YouTube(link_text)
            video = url.streams.get_highest_resolution()
            download_path = os.path.join(
                os.path.expanduser('~'),
                'DCIM', 'Camera'
            )
            if not os.path.exists(download_path):
                os.makedirs(download_path)
            video_path = video.download(output_path=download_path)
            self.downloaded_label.text = f"Downloaded to {video_path}"
        else:
            self.downloaded_label.text = "Insecure Link"

def main():
    return YoutubeBuddy() 
