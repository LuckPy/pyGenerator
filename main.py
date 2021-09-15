from PySide6 import QtWidgets
from qt_material import apply_stylesheet


from generator import passwords_generator


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.setWindowTitle("pyGenerator")
        apply_stylesheet(app, theme='dark_red.xml')

    def setup_ui(self):
        self.create_widgets()
        self.modify_widgets()
        self.create_layouts()
        self.add_widgets_to_layouts()
        self.setup_connections()

    def create_widgets(self):
        self.lbl_letters = QtWidgets.QLabel("Lettres :")
        self.cb_letters = QtWidgets.QComboBox()
        self.lbl_numbers = QtWidgets.QLabel("Nombres :")
        self.cb_numbers = QtWidgets.QComboBox()
        self.lbl_special = QtWidgets.QLabel("Caractères spéciaux :")
        self.cb_special = QtWidgets.QComboBox()
        self.btn_confirm = QtWidgets.QPushButton("Générer")
        self.le_passwd = QtWidgets.QLineEdit("")
        self.lw_history = QtWidgets.QListWidget()
        self.btn_clear = QtWidgets.QPushButton("Clear")
        self.spacer = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

    def modify_widgets(self):
        self.cb_letters.addItems([str(i) for i in range(1, 25)])
        self.cb_letters.setCurrentText("10")
        self.cb_numbers.addItems([str(i) for i in range(1, 13)])
        self.cb_numbers.setCurrentText("4")
        self.cb_special.addItems([str(i) for i in range(1, 9)])
        self.cb_special.setCurrentText("2")
        self.setStyleSheet("QComboBox {width: 60px; border: none;}"
                           "QLineEdit {border: none; font-weight: bold;}")
        self.lw_history.setFixedHeight(200)
        self.lw_history.hide()
        self.btn_clear.hide()
        self.btn_clear.setFixedSize(100, 200)

    def create_layouts(self):
        self.layout = QtWidgets.QVBoxLayout(self)
        self.top_layout = QtWidgets.QHBoxLayout()
        self.bot_layout = QtWidgets.QHBoxLayout()
        self.clear_layout = QtWidgets.QHBoxLayout()

    def add_widgets_to_layouts(self):
        self.layout.addLayout(self.top_layout)
        self.layout.addLayout(self.bot_layout)
        self.layout.addWidget(self.lw_history)
        self.layout.addLayout(self.clear_layout)
        self.top_layout.addWidget(self.lbl_letters)
        self.top_layout.addWidget(self.cb_letters)
        self.top_layout.addWidget(self.lbl_numbers)
        self.top_layout.addWidget(self.cb_numbers)
        self.top_layout.addWidget(self.lbl_special)
        self.top_layout.addWidget(self.cb_special)
        self.bot_layout.addWidget(self.btn_confirm)
        self.bot_layout.addWidget(self.le_passwd)
        self.clear_layout.addSpacerItem(self.spacer)
        self.clear_layout.addWidget(self.btn_clear)
        self.clear_layout.addSpacerItem(self.spacer)

    def setup_connections(self):
        self.btn_confirm.clicked.connect(self.generate_passwd)
        self.btn_clear.clicked.connect(lambda : self.lw_history.clear())

    def generate_passwd(self):
        self.passwd = passwords_generator()
        passwd = self.passwd.gen_passwd(int(self.cb_letters.currentText()),
                                        int(self.cb_numbers.currentText()),
                                        int(self.cb_special.currentText()))
        self.le_passwd.setText(passwd)
        self.lw_history.show()
        self.btn_clear.show()
        self.history = QtWidgets.QListWidgetItem(passwd)
        self.lw_history.addItem(self.history)


app = QtWidgets.QApplication([])
window = MainWindow()
window.show()
app.exec_()
