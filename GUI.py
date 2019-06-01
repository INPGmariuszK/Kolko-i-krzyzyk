#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *

from pygame import mixer

# import nieaktywny do czasu nowej implementacji silnika gry
# from engine import *

class WindowWithButtons(QWidget):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        QApplication.setStyle(QStyleFactory.create("Fusion"))

        mixer.init()

        # dopóki nie istnieje plik w tej lokalizacji, dopóty ta linijka powinna być nieaktywna
        # self.press_sound = mixer.Sound("music/press_effect.wav")

        self.buttons = []

        # kawałek nieaktywny do czasu nowej implementacji silnika
        #
        # self.board = Board()
        #
        # self.turn = Turn()

        self.main_structure()

    def main_structure(self):

        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('Kółko i krzyżyk')

        # Do czasu znalezienia ikon, linijka nieaktywna
        # self.setWindowIcon(QIcon("graphics/krzyz.ico"))

        for button_nmb in range(0, 9):
            self.buttons.append(QPushButton(EMPTY, self))
            self.buttons[button_nmb].clicked.connect(self.button_clicked)
            self.buttons[button_nmb].setObjectName("button%d" % button_nmb)
            self.buttons[button_nmb].resize(100, 100)

            # Do czasu znalezienia ikon, linijki nieaktywne
            # self.buttons[button_nmb].setIcon(QIcon("EMPTY_ICON.ico"))
            # self.buttons[button_nmb].setIconSize(QtCore.QSize(50, 50))

        self.buttons[0].move(50, 50)

        self.buttons[1].move(200, 50)

        self.buttons[2].move(350, 50)

        self.buttons[3].move(50, 200)

        self.buttons[4].move(200, 200)

        self.buttons[5].move(350, 200)

        self.buttons[6].move(50, 350)

        self.buttons[7].move(200, 350)

        self.buttons[8].move(350, 350)

        self.show()


        # Do czasu znalezienia dzwięków, linijki nieaktywne
        # mixer.music.load('music/background_music.wav')
        # mixer.music.play(-1)


    def button_clicked(self):
        pass

def change_theme():
    pass

if __name__ == "__main__":
    pass
