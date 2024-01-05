import customtkinter as ctk
from tkinter import ttk
from pytube import YouTube
import os


# create a root window
root = ctk.CTk()
ctk.get_appearance_mode()
ctk.set_default_color_theme("blue")


# title of the window
root.title("Youtube Downloader!")


# set min and max width and height
root.geometry("720x480")
root.minsize(720, 480)
root.maxsize(1080, 720)


# create a frame to hold the content
content_frame = ctk.CTkFrame(root)
content_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)


# create a label and the entry widget for the video url
url_label = ctk.CTkLabel(content_frame, text="Enter the youtube url here : ")
entry_url = ctk.CTkEntry(content_frame, width=400, height=40)
url_label.pack(pady=10)
entry_url.pack(pady=10)


# create a download button
download_button = ctk.CTkButton(content_frame, text="Download")
download_button.pack(pady=10)


# to start the app
root.mainloop()


