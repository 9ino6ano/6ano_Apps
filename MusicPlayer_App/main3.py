import os
import pygame
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QFileDialog, QSlider, QHBoxLayout


class MusicPlayer(QWidget):
    def __init__(self):
        super().__init__()

        self.music_path = ""
        self.current_volume = 50

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("9ino6ano Productions Music Player")
        self.setGeometry(100, 100, 400, 200)

        self.current_song_label = QLabel("No song selected")
        self.select_button = QPushButton("Select Song", self)
        self.select_button.clicked.connect(self.select_song)

        self.play_button = QPushButton("Play", self)
        self.play_button.clicked.connect(self.play_music)

        self.stop_button = QPushButton("Stop", self)
        self.stop_button.clicked.connect(self.stop_music)

        self.volume_slider = QSlider()
        self.volume_slider.setOrientation(1)  # Vertical orientation
        self.volume_slider.setMinimum(0)
        self.volume_slider.setMaximum(100)
        self.volume_slider.setValue(self.current_volume)
        self.volume_slider.valueChanged.connect(self.set_volume)

        self.next_button = QPushButton("Next", self)
        self.prev_button = QPushButton("Previous", self)

        hbox = QHBoxLayout()
        hbox.addWidget(self.prev_button)
        hbox.addWidget(self.play_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.next_button)

        vbox = QVBoxLayout()
        vbox.addWidget(self.current_song_label)
        vbox.addWidget(self.select_button)
        vbox.addWidget(self.volume_slider)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.show()

    def select_song(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Audio Files (*.mp3 *.wav)")
        selected_file, _ = file_dialog.getOpenFileName()
        if selected_file:
            self.music_path = selected_file
            self.current_song_label.setText(os.path.basename(self.music_path))

    def play_music(self):
        if self.music_path:
            pygame.mixer.init()
            pygame.mixer.music.load(self.music_path)
            pygame.mixer.music.play()

    def stop_music(self):
        pygame.mixer.music.stop()

    def set_volume(self, value):
        self.current_volume = value
        pygame.mixer.music.set_volume(value / 100)


if __name__ == "__main__":
    app = QApplication([])
    player = MusicPlayer()
    app.exec_()
