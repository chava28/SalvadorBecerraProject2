from PyQt6.QtWidgets import *
from gui import *

class Television(QMainWindow, Ui_MainWindow):
    """
    These are the default values for the Tv
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 9
    MIN_CHANNEL = 1
    MAX_CHANNEL = 4

    def __init__(self, *args, **kwargs) -> None:
        '''
        Here we are initializing the variables for the new object
        '''
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.volume_2.setValue(self.MIN_VOLUME)
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

        self.power.clicked.connect(lambda: self.pow())
        self.one.clicked.connect(lambda: self.chan_one())
        self.two.clicked.connect(lambda: self.chan_two())
        self.three.clicked.connect(lambda: self.chan_three())
        self.four.clicked.connect(lambda: self.chan_four())
        self.mute.clicked.connect(lambda: self.mu())
        self.vol_up.clicked.connect(lambda: self.volume_up())
        self.vol_down.clicked.connect(lambda: self.volume_down())
        self.volume_2.valueChanged.connect(lambda: self.vol_slide())
        self.channel_up.clicked.connect(lambda: self.chan_up())
        self.channel_down.clicked.connect(lambda: self.chan_down())

        self.channel_1.setVisible(False)
        self.channel_2.setVisible(False)
        self.channel_3.setVisible(False)
        self.channel_4.setVisible(False)

        self.vol_up.setEnabled(False)
        self.vol_down.setEnabled(False)
        self.channel_up.setEnabled(False)
        self.channel_down.setEnabled(False)
        self.mute.setEnabled(False)
        self.one.setEnabled(False)
        self.two.setEnabled(False)
        self.three.setEnabled(False)
        self.four.setEnabled(False)
        self.volume_2.setEnabled(False)

    def pow(self) -> None:
        '''
        Method to turn on the Tv and re-enable/disable buttons
        '''
        self.__status = not self.__status
        if self.__status:
            self.power_off_screen.setVisible(False)
            self.__muted = False
            self.vol_up.setEnabled(True)
            self.vol_down.setEnabled(True)
            self.channel_up.setEnabled(True)
            self.channel_down.setEnabled(True)
            self.mute.setEnabled(True)
            self.one.setEnabled(True)
            self.two.setEnabled(True)
            self.three.setEnabled(True)
            self.four.setEnabled(True)
            self.volume_2.setEnabled(True)

            self.chan_select()
            self.vol_select()
            self.volume_num.setText(str(self.__volume))
        else:
            self.power_off_screen.setVisible(True)
            self.channel_1.setVisible(False)
            self.channel_2.setVisible(False)
            self.channel_3.setVisible(False)
            self.channel_4.setVisible(False)
            self.vol_up.setEnabled(False)
            self.vol_down.setEnabled(False)
            self.channel_up.setEnabled(False)
            self.channel_down.setEnabled(False)
            self.mute.setEnabled(False)
            self.one.setEnabled(False)
            self.two.setEnabled(False)
            self.three.setEnabled(False)
            self.four.setEnabled(False)
            self.volume_2.setEnabled(False)
            self.volume_num.setText('')
            self.two.setStyleSheet('none')
            self.one.setStyleSheet('none')
            self.four.setStyleSheet('none')
            self.three.setStyleSheet('none')

    def mu(self) -> None:
        '''
        Method to mute the Tv
        '''
        if self.__status:
            self.__muted = not self.__muted
            if self.__muted == True:
                self.volume_num.setText('Mute')
            else:
                self.volume_num.setText(str(self.__volume))

    def chan_select(self) -> None:
        '''
        Method to actually change the channels
        :return:
        '''
        if self.__status:
            if self.__channel == 1:
                self.power_off_screen.setVisible(False)
                self.channel_1.setVisible(True)
                self.channel_2.setVisible(False)
                self.channel_3.setVisible(False)
                self.channel_4.setVisible(False)
                self.one.setStyleSheet('background-color:lime;color:black;')
                self.two.setStyleSheet('none')
                self.three.setStyleSheet('none')
                self.four.setStyleSheet('none')
            elif self.__channel == 2:
                self.power_off_screen.setVisible(False)
                self.channel_1.setVisible(False)
                self.channel_2.setVisible(True)
                self.channel_3.setVisible(False)
                self.channel_4.setVisible(False)
                self.two.setStyleSheet('background-color:lime;color:black;')
                self.one.setStyleSheet('none')
                self.three.setStyleSheet('none')
                self.four.setStyleSheet('none')
            elif self.__channel == 3:
                self.power_off_screen.setVisible(False)
                self.channel_1.setVisible(False)
                self.channel_2.setVisible(False)
                self.channel_3.setVisible(True)
                self.channel_4.setVisible(False)
                self.three.setStyleSheet('background-color:lime;color:black;')
                self.two.setStyleSheet('none')
                self.one.setStyleSheet('none')
                self.four.setStyleSheet('none')
            elif self.__channel == 4:
                self.power_off_screen.setVisible(False)
                self.channel_1.setVisible(False)
                self.channel_2.setVisible(False)
                self.channel_3.setVisible(False)
                self.channel_4.setVisible(True)
                self.four.setStyleSheet('background-color:lime;color:black;')
                self.two.setStyleSheet('none')
                self.three.setStyleSheet('none')
                self.one.setStyleSheet('none')

    def vol_select(self) -> None:
        '''
        Method to actually change the volumes
        :return:
        '''
        if self.__status:
            if self.__volume == 0:
                self.volume_2.setValue(self.__volume)
                self.volume_num.setText(str(self.__volume))
            elif self.__volume == 1:
                self.volume_2.setValue(self.__volume)
                self.volume_num.setText(str(self.__volume))
            elif self.__volume == 2:
                self.volume_2.setValue(self.__volume)
                self.volume_num.setText(str(self.__volume))
            elif self.__volume == 3:
                self.volume_2.setValue(self.__volume)
                self.volume_num.setText(str(self.__volume))
            elif self.__volume == 4:
                self.volume_2.setValue(self.__volume)
                self.volume_num.setText(str(self.__volume))
            elif self.__volume == 5:
                self.volume_2.setValue(self.__volume)
                self.volume_num.setText(str(self.__volume))
            elif self.__volume == 6:
                self.volume_2.setValue(self.__volume)
                self.volume_num.setText(str(self.__volume))
            elif self.__volume == 7:
                self.volume_2.setValue(self.__volume)
                self.volume_num.setText(str(self.__volume))
            elif self.__volume == 8:
                self.volume_2.setValue(self.__volume)
                self.volume_num.setText(str(self.__volume))
            elif self.__volume == 9:
                self.volume_2.setValue(self.__volume)
                self.volume_num.setText(str(self.__volume))
    def chan_one(self) -> None:
        '''
        Changed the channel when button 1 is clicked
        :return:
        '''
        if self.__status:
            self.__channel = 1
            self.chan_select()

    def chan_two(self) -> None:
        '''
        Changed the channel when button 2 is clicked
        :return:
        '''
        if self.__status:
            self.__channel = 2
            self.chan_select()

    def chan_three(self) -> None:
        '''
        Changed the channel when button 3 is clicked
        :return:
        '''
        if self.__status:
            self.__channel = 3
            self.chan_select()

    def chan_four(self) -> None:
        '''
        Changed the channel when button 4 is clicked
        :return:
        '''
        if self.__status:
            self.__channel = 4
            self.chan_select()
    def chan_up(self) -> None:
        '''
        Method to turn up the channel number
        '''
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
                self.chan_select()
            else:
                self.__channel = Television.MIN_CHANNEL
                self.chan_select()

    def chan_down(self) -> None:
        '''
        Method to turn down the channel number
        '''
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
                self.chan_select()
            else:
                self.__channel = Television.MAX_CHANNEL
                self.chan_select()

    def volume_up(self) -> None:
        '''
        Method to turn up the volume of the Tv
        '''
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
                self.vol_select()

    def volume_down(self) -> None:
        '''
        Method to turn down the volume of the Tv
        '''
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
                self.vol_select()

    def vol_slide(self) -> None:
        '''
        Method to enable the slider for the volume
        :return:
        '''
        if self.__status:
            self.__volume = self.volume_2.value()
            self.vol_select()