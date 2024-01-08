import customtkinter as ctk
from tkinter import ttk
from pytube import YouTube
import os


def download_video():
    print("Clicked")


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
download_button = ctk.CTkButton(content_frame, text="Download", command=download_video)
download_button.pack(pady=10)

# create a resolution combo box
resolutions = ["720px", "360px", "240px"]
resolution_var = ctk.StringVar()
resolution_combobox = ttk.Combobox(content_frame, values=resolutions, textvariable=resolution_var)
resolution_combobox.pack(pady=10)
resolution_combobox.set("720px")


# create a label and the progress bar to display the download progress
progress_label = ctk.CTkLabel(content_frame, text="%0")
progress_label.pack(pady=10)

progress_bar = ctk.CTkProgressBar(content_frame, width=400)
progress_bar.set(0.6)
progress_bar.pack(pady=10)


# create the status label
status_label = ctk.CTkLabel(content_frame, text="Downloaded")
status_label.pack(pady=10)


# to start the app
root.mainloop()
