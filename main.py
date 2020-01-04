from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QFileDialog, QLabel, QProgressBar, QComboBox,\
    QGroupBox, QGridLayout, QTextEdit
from PyQt5.QtCore import Qt, QObject, pyqtSignal
from PyQt5.QtGui import QPalette, QColor, QTextCursor
from spleeter.spleeter.separator import Separator
from spleeter.spleeter.utils import logging

import sys

class Stream(QObject):
    newText = pyqtSignal(str)

    def write(self, text):
        self.newText.emit(str(text))

class SpleeterGUI(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.title = 'Spleeter Graphical User Interface'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 240
        self.layout = QVBoxLayout()
        self.mp3file = ""
        print(logging.get_logger())
        sys.stdout = Stream(newText=self.onUpdateText)
        sys.stderr = Stream(newText=self.onUpdateText)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.mystyle()
        
        #buttonsss
        
        self.grid = self.init_grid_layout()
        self.progressbar = self.create_new_progressbar()
        self.console = self.create_new_textedit()
        self.layout.addWidget(self.grid)
        self.layout.addWidget(self.progressbar)
        self.layout.addWidget(self.console)
        self.setLayout(self.layout)
        
        self.show()
    
    def init_grid_layout(self):
        group_box_render = QGroupBox("Render")
        group_box_picker = QGroupBox("Picker")
        group_box_format = QGroupBox("Format")
        group_box_file = QGroupBox("File")
        
        self.render_button = self.create_new_button("Render", self.render_button_click)
        vbox = QVBoxLayout()
        vbox.addWidget(self.render_button)
        group_box_render.setLayout(vbox)
        
        self.file_picker_button = self.create_new_button("Pick a file", self.file_picker_button_click)
        vbox = QVBoxLayout()
        vbox.addWidget(self.file_picker_button)
        group_box_picker.setLayout(vbox)
        
        self.filename_text = self.create_new_text("Your file is:")
        vbox = QVBoxLayout()
        vbox.addWidget(self.filename_text)
        group_box_file.setLayout(vbox)
        
        self.format_render = self.create_new_dropdown(["spleeter:2stems"], self.format_button_click)
        vbox = QVBoxLayout()
        vbox.addWidget(self.format_render)
        group_box_format.setLayout(vbox)
        
        grid = QGridLayout()
        grid.addWidget(group_box_picker, 0, 0)
        grid.addWidget(group_box_file, 0, 1)
        grid.addWidget(group_box_format, 1, 0)
        grid.addWidget(group_box_render, 1, 1)
        
        end_group_box = QGroupBox()
        end_group_box.setLayout(grid)
        
        return end_group_box
    
    # Console stuffs
    def onUpdateText(self, text):
        cursor = self.console.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.console.setTextCursor(cursor)
        self.console.ensureCursorVisible()
    
    def __del__(self):
        sys.stdout = sys.__stdout__
    ####################
    
    def mystyle(self):
        self.app.setStyle("Fusion")
    
        dark_palette = QPalette()
        
        dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.WindowText, Qt.white)
        dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
        dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
        dark_palette.setColor(QPalette.ToolTipText, Qt.white)
        dark_palette.setColor(QPalette.Text, Qt.white)
        dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ButtonText, Qt.white)
        dark_palette.setColor(QPalette.BrightText, Qt.red)
        dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.HighlightedText, Qt.black)
        self.app.setPalette(dark_palette)
        self.app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
        
    def create_new_button(self, text, function):
        button = QPushButton(str(text))
        button.clicked.connect(function)
        #self.vlayout1.addWidget(button)
        return button
    
    def create_new_dropdown(self, text_list, function=None):
        combo_box = QComboBox()
        for i in text_list:
            combo_box.addItem(str(i))
        combo_box.currentIndexChanged.connect(function)
        #self.vlayout1.addWidget(combo_box)
        return combo_box
        
    def create_new_text(self, text):
        line = QLabel()
        line.setText(str(text))
        #self.vlayout1.addWidget(line)
        return line
    
    def create_new_textedit(self):
        box = QTextEdit()
        box.moveCursor(QTextCursor.Start)
        box.ensureCursorVisible()
        box.setLineWrapColumnOrWidth(500)
        box.setLineWrapMode(QTextEdit.FixedPixelWidth)
        return box
    
    def update_text(self, qtext, new_text):
        qtext.setText(str(new_text))
        #self.update()
        return qtext
    
    def create_new_progressbar(self):
        progress = QProgressBar()
        progress.setValue(0)
        #self.vlayout1.addWidget(progress)
        return progress
        
    def file_picker_button_click(self):
        the_file = QFileDialog.Options()
        the_file |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=the_file)
        if file_name:
            self.mp3file = file_name
            print(self.mp3file)
            self.update_text(self.filename_text, "Your file is:" + file_name)
    
    def render_button_click(self):
        alert = QMessageBox()
        logging.enable_logging()
        separator = Separator(self.format_render.currentText())
        separator.separate_to_file(self.mp3file, "out")
        
        alert.setText("Done!")
        alert.exec_()
    
    def format_button_click(self):
        print("Chosen index is: ", self.format_render.currentText())
    
if __name__ == '__main__':
    app = QApplication([])
    my_app = SpleeterGUI(app)
    my_app.app.exec_()