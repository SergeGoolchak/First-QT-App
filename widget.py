from PySide2.QtWidgets import *
from PySide2.QtGui import QIcon
from PySide2.QtCore import Slot, Signal, Qt
import os

class MyWidget(QWidget):

    cnt_signal = Signal(int)

    def __init__(self):
        super().__init__()

        self.cnt = 0
        self.setWindowTitle(self.tr('Settings menu'))
        
        icon = QIcon('/Users/Serge/VS Workspace/newproj/image/settings.png')
        self.setWindowIcon(icon)

        main_layout = QVBoxLayout()

        upper_layout = QHBoxLayout()
        bottom_layout = QHBoxLayout()

        upper_layout = QHBoxLayout()
        bottom_layout = QHBoxLayout()

        left_up_layout = QVBoxLayout()
        
        lcd_layout = QHBoxLayout()
        label = QLabel(self.tr('Counter'))
        self.lcd = QLCDNumber()
        self.lcd.display(0)
        
        lcd_layout.addWidget(label)
        lcd_layout.addWidget(self.lcd)

        self.__add_pushbutton = QPushButton(self.tr('Add'))
        self.__quit_pushbutton = QPushButton(self.tr('Quit'))

        self.__quit_pushbutton.pressed.connect(self.quit)
        self.__add_pushbutton.pressed.connect(self.add)

        left_up_layout.addLayout(lcd_layout)
        left_up_layout.addWidget(self.__add_pushbutton)
        left_up_layout.addWidget(self.__quit_pushbutton)

        
        right_up_layout = QVBoxLayout()

        self.buttons_group = QButtonGroup()
        self.__cursors_button = []
        self.__cursors_button.append(QRadioButton(self.tr('Button 1')))
        self.__cursors_button.append(QRadioButton(self.tr('Button 2')))
        self.__cursors_button.append(QRadioButton(self.tr('Button 3')))

        for button in self.__cursors_button:
            self.buttons_group.addButton(button)
            right_up_layout.addWidget(button)
            button.pressed.connect(self.changeCursor)

        self.menu_buttons_group = QButtonGroup()
        self.__windowButtons = []
        self.__windowButtons.append(QRadioButton(self.tr('Menu 1')))
        self.__windowButtons.append(QRadioButton(self.tr('Menu 2')))

        for button in self.__windowButtons:
            self.menu_buttons_group.addButton(button)
            right_up_layout.addWidget(button)
            button.pressed.connect(self.changeMenu)


        left_bottom_layout = QVBoxLayout()

        check_sound = QCheckBox(self.tr('Sound'))
        check_backlight = QCheckBox(self.tr('Backlight'))
        check_auto = QCheckBox(self.tr('Auto'))

        left_bottom_layout.addWidget(check_sound)
        left_bottom_layout.addWidget(check_backlight)
        left_bottom_layout.addWidget(check_auto)
        
        right_bottom_layout = QFormLayout()

        label = QLabel(self.tr('Color'))
        label1 = QLabel(self.tr('Brightness'))
        label2 =QLabel(self.tr(f'{os.getcwd()}'))
        self.__change_button = QPushButton(self.tr('Change'))
        self.__change_button2 = QPushButton(self.tr('Change'))
        
        right_bottom_layout.addRow(label, self.__change_button)
        right_bottom_layout.addRow(label1, self.__change_button2)
        right_bottom_layout.addRow(label2)



        self.setLayout(main_layout)
        main_layout.addLayout(upper_layout)
        main_layout.addLayout(bottom_layout)
        upper_layout.addLayout(left_up_layout)
        upper_layout.addLayout(right_up_layout)
        bottom_layout.addLayout(left_bottom_layout)
        bottom_layout.addLayout(right_bottom_layout)

        self.cnt_signal.connect(self.lcd.display)

    @Slot()
    def quit(self):
        QApplication.quit()

    @Slot()
    def add(self):
        self.cnt += 1
        self.cnt_signal.emit(self.cnt)
        self.lcd.repaint()

    @Slot()
    def changeCursor(self):
        index = self.__cursors_button.index(self.sender())
        cursors = (Qt.ArrowCursor, Qt.PointingHandCursor, Qt.CrossCursor)
        self.setCursor(cursors[index])

    @Slot()
    def changeMenu(self):
        index = self.__windowButtons.index(self.sender())
        flags = (Qt.Window, Qt.FramelessWindowHint)
        self.setWindowFlags(flags[index])
        self.show()

