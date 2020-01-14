import sys
from PyQt5.QtWidgets import QApplication
import lo

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = lo.LoginDialog()

    win.show()
    sys.exit(app.exec_())
