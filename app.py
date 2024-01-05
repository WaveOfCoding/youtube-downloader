import customtkinter as ctk
from tkinter import ttk
from pytube import YouTube
import os


# create a root window
root = ctk.CTk()
ctk.get_appearance_mode("System")
ctk.set_default_color_theme("blue")


# title of the window
root.title("Youtube Downloader!")


# set min and max width and height
root.geometry("720x480")
root.minsize(720, 480)
root.maxsize(1080, 720)


