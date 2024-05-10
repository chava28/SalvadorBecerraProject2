from PyQt6.QtWidgets import *
from gui import *


class Logic(QMainWindow, Ui_MainWindow):
    MIN_VOLUME = 0
    MAX_VOLUME = 9
    MIN_CHANNEL = 0
    MAX_CHANNEL = 9

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Logic.MIN_VOLUME
        self.__channel: int = Logic.MIN_CHANNEL

        self.chan_up.clicked.connect(lambda : self.channel_up())
        self.chan_down.clicked.connect(lambda: self.channel_down())
        self.vol_up.clicked.connect(lambda: self.volume_up())
        self.vol_down.clicked.connect(lambda: self.volume_down())
        self.mu.clicked.connect(lambda: self.mute())
        self.power.clicked.connect(lambda: self.on())

    def on(self):
        '''
        Method to turn on the Tv
        '''
        if not self.__status:
            self.__status = True
        else:
            self.__status = Fals
    def mute(self):
        '''
        Method to mute the Tv
        '''
        if self.__status:
            self.__muted = not self.__muted
    def channel_up(self):
        '''
        Method to turn up the channel number
        '''
        if self.__status:
            if self.__channel < Logic.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Logic.MIN_CHANNEL
    def channel_down(self):
        '''
        Method to turn down the channel number
        '''
        if self.__status:
            if self.__channel > Logic.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Logic.MAX_CHANNEL
    def volume_up(self):
        '''
        Method to turn up the volume of the Tv
        '''
        if self.__status:
            self.__muted = False
            if self.__volume < Logic.MAX_VOLUME:
                self.__volume += 1
    def volume_down(self):
        '''
        Method to turn down the volume of the Tv
        '''
        if self.__status:
            self.__muted = False
            if self.__volume > Logic.MIN_VOLUME:
                self.__volume -= 1