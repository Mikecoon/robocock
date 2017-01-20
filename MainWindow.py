from config import moderators
from PyQt5.QtWidgets import *

from models.Moderator import ModeratorWidget
from PyQt5.Qt import *


class MainWindow(QWidget):
    moderators = []

    def __init__(self):
        super().__init__()


        self.resize(300, 450)
        self.setWindowTitle('Robocock')
        self.layout = QHBoxLayout()

        self.layout.setAlignment(Qt.AlignTop)
        self.init_ui()
        self.setLayout(self.layout)



    def init_ui(self):
        game_layout = QWidget()
        self.layout.addWidget(game_layout)

        moderators_widget = QWidget()
        moderators_layout = QVBoxLayout()
        moderators_layout.setSpacing(1)
        moderators_widget.setLayout(moderators_layout)

        self.layout.addWidget(moderators_widget)


        self.moderators = []
        for i, moderator in enumerate(moderators):
            moderator_widget = ModeratorWidget(moderator)
            moderator_widget.append_to(moderators_layout)


            self.moderators.append(moderator_widget)




