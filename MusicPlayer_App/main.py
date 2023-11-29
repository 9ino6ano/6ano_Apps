import os
import pygame
from tkinter import Tk, Label, Button, filedialog

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("9ino6ano Productions Music Player")
        self.master.geometry("400x200")

        self.current_song_label = Label(master, text="No song selected")
        self.current_song_label.pack(pady=10)

        self.select_button = Button(master, text="Select Song", command=self.select_song)
        self.select_button.pack(pady=10)

        self.play_button = Button(master, text="Play", state="disabled", command=self.play_music)
        self.play_button.pack(pady=5)

        self.stop_button = Button(master, text="Stop", state="disabled", command=self.stop_music)
        self.stop_button.pack(pady=5)

        self.music_path = ""

    def select_song(self):
        self.music_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
        if self.music_path:
            self.current_song_label.config(text=os.path.basename(self.music_path))
            self.play_button["state"] = "normal"
            self.stop_button["state"] = "normal"

    def play_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.music_path)
        pygame.mixer.music.play()

    def stop_music(self):
        pygame.mixer.music.stop()

if __name__ == "__main__":
    root = Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
