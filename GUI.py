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
        pass

    def button_clicked(self):
        pass

def change_theme():
    pass

if __name__ == "__main__":
    pass
