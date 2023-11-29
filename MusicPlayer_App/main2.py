from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog
from pygame import mixer
import os

root = Tk()
root.title("Music Player")
root.geometry("920x670+290+85")
root.configure(bg="#0f1a2b")
root.resizable(False, False)

mixer.init()

def open_folder():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        print(songs)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END, song)

def play_song():
    music_name = playlist.get(ACTIVE)
    print(music_name[0:-4])
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    music.config(text=music_name[0:-4])

def stop_song():
    mixer.music.stop()
    music.config(text="")

def resume_song():
    mixer.music.unpause()

def pause_song():
    mixer.music.pause()

def set_volume(val):
    volume = int(val) / 100
    mixer.music.set_volume(volume)

def set_pitch(val):
    mixer.music.set_pitch(val)

def set_phase(val):
    mixer.music.set_pos(val)

def set_polarity(val):
    mixer.music.set_pos(val)

def set_equalizer(val):
    mixer.music.set_pos(val)

def record_song():
    pass  # Implement recording functionality

# icon
image_icon = PhotoImage(file="Images/logo.png")
root.iconphoto(False, image_icon)

Top = PhotoImage(file="Images/top.png")
Label(root, image=Top, bg="#0f1a2b").pack()

# logo
Logo = PhotoImage(file="Images/logo.png")
Label(root, image=Logo, bg="#0f1a2b").place(x=65, y=115)

# Buttons
play_button = PhotoImage(file="Images/play.png")
Button(root, image=play_button, bg="#0f1a2b", bd=0, command=play_song).place(x=100, y=400)

stop_button = PhotoImage(file="Images/stop.png")
Button(root, image=stop_button, bg="#0f1a2b", bd=0, command=stop_song).place(x=30, y=500)

resume_button = PhotoImage(file="Images/resume.png")
Button(root, image=resume_button, bg="#0f1a2b", bd=0, command=resume_song).place(x=115, y=500)

pause_button = PhotoImage(file="Images/pause.png")
Button(root, image=pause_button, bg="#0f1a2b", bd=0, command=pause_song).place(x=200, y=500)

record_button = PhotoImage(file="Images/record.png")
Button(root, image=record_button, bg="#0f1a2b", bd=0, command=record_song).place(x=285, y=500)

# Volume Control
volume_label = Label(root, text="Volume", font=("arial", 10), fg="white", bg="#0f1a2b")
volume_label.place(x=430, y=400)

volume_slider = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=set_volume)
volume_slider.set(50)  # Set default volume to 50%
volume_slider.place(x=420, y=430)

# Mixer Controls
pitch_label = Label(root, text="Pitch", font=("arial", 10), fg="white", bg="#0f1a2b")
pitch_label.place(x=520, y=400)

pitch_slider = Scale(root, from_=0.5, to=2.0, resolution=0.1, orient=HORIZONTAL, command=set_pitch)
pitch_slider.set(1.0)  # Set default pitch to 1.0
pitch_slider.place(x=510, y=430)

# Add controls for phase, polarity, equalizer, etc. as needed

# Label
music = Label(root, text="", font=("arial", 15), fg="white", bg="#0f1a2b")
music.place(x=150, y=340, anchor="center")

# Music Playlist
Menu = PhotoImage(file="Images/menu.png")
Label(root, image=Menu, bg="#0f1a2b").pack(padx=10, pady=50, side=RIGHT)

music_frame = Frame(root, bd=2, relief=RIDGE)
music_frame.place(x=350, y=350, width=560, height=250)

Button(root, text="Open Folder", width=15, height=2, font=("arial", 10, "bold"), fg="white", bg="#21b3de", command=open_folder).place(x=330, y=300)

scroll = Scrollbar(music_frame)
playlist = Listbox(music_frame, width=100, font=("arial", 10), bg="#333333", fg="grey", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=scroll.set)
scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT, fill=Y)
playlist.pack(side=LEFT, fill=BOTH)

root.mainloop()
