from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from urllib import request
import vk_api
from config import vk_login, vk_password
from PyQt5.Qt import *
from utils import set_interval

class ModeratorWidget:
    name = ""
    id = ""

    def __init__(self, info):
        # Save moderator's info
        self.info = info

        # Create a widget for moderator's info
        self.widget = QWidget()

        self.widget.move(0,0)
        self.layout = QHBoxLayout()
        self.layout.setAlignment(Qt.AlignLeft)
        self.widget.setLayout(self.layout)

        # Label with moderator's avatar
        self.avatarLabel = QLabel()
        self.avatarLabel.resize(50, 50)
        self.layout.addWidget(self.avatarLabel)

        # layout for name and status
        info_layout = QVBoxLayout()
        info_layout.setAlignment(Qt.AlignTop)
        info_layout.setContentsMargins(0, 8, 0, 0)

        # Label with moderator's name
        self.nameLabel = QLabel()
        font = QFont()
        font.setFamily("Tahoma")
        font.setBold(True)
        self.nameLabel.setFont(font)
        self.nameLabel.setText(info['name'])

        # label with moderator's status
        self.statusLabel = QLabel()
        self.statusLabel.setText("Status")
        info_layout.addWidget(self.nameLabel)
        info_layout.addWidget(self.statusLabel)
        self.layout.addLayout(info_layout)

        vk_session = vk_api.VkApi(vk_login, vk_password)
        try:
            vk_session.authorization()
        except vk_api.AuthorizationError as error_msg:
            print(error_msg)
            return

        self.vk = vk_session.get_api()
        self.update()

        set_interval(self.update, 1.0)

    def update(self):
        response = self.vk.users.get(
            user_id=self.info['id'],
            fields="photo_50, online"
        )

        if response:
            data = request.urlopen(response[0]['photo_50']).read()

            # Update Moderator's photo
            pixelmap = QPixmap()
            pixelmap.loadFromData(data)
            self.avatarLabel.setPixmap(pixelmap)

            # Update moderator's status
            if response[0]['online'] == 1:
                self.statusLabel.setText("Онлайн")
                self.statusLabel.setStyleSheet("color: #ff6666")
            else:
                self.statusLabel.setText("Оффлайн")
                self.statusLabel.setStyleSheet("color: #669966")

    def append_to(self, layout):
        layout.addWidget(self.widget)



