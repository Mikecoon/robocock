from MainWindow import MainWindow
import sys
from PyQt5.QtWidgets import *
import vk_api




if __name__ == '__main__':
    app = QApplication(sys.argv)




    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())

