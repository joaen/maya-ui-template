import sys
import maya.cmds as cmds
import maya.OpenMayaUI as omui
from shiboken2 import wrapInstance
from PySide2 import QtCore, QtGui, QtWidgets


def maya_main_window():
    # Return the Maya main window as QMainWindow
    main_window = omui.MQtUtil.mainWindow()
    if sys.version_info.major >= 3:
        return wrapInstance(int(main_window), QtWidgets.QWidget)
    else:
        return wrapInstance(long(main_window), QtWidgets.QWidget) # type: ignore

class TemplateToolWindow(QtWidgets.QDialog):
    def __init__(self):
        super(TemplateToolWindow, self).__init__(maya_main_window())
        self.setWindowTitle("WINDOW_TITLE")
        
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        self.resize(380, 300)
        self.create_ui_widgets()
        self.create_ui_layout()
        self.create_ui_connections()

        if cmds.about(macOS=True):
            self.setWindowFlags(QtCore.Qt.Tool)
 
    def create_ui_widgets(self):
        self.template_label = QtWidgets.QLabel("TEMPLATE_TEXT_LABEL")
        self.template_button = QtWidgets.QPushButton("TEMPLATE BUTTON")
        self.template_checkbox = QtWidgets.QCheckBox("TEMPLATE_CHECKBOX")
        self.template_combobox = QtWidgets.QComboBox()
        self.template_combobox.addItem("TEMPLATE_COMBOBOX_ITEM")
        self.template_textfield = QtWidgets.QLineEdit()
        self.template_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.template_icon_button = QtWidgets.QPushButton()
        self.template_icon_button.setIcon(QtGui.QIcon(":fileOpen.png"))

    def create_ui_layout(self):
        horizontal_layout = QtWidgets.QHBoxLayout()
        horizontal_layout.addWidget(self.template_textfield)
        horizontal_layout.addWidget(self.template_icon_button)
        horizontal_layout.addWidget(self.template_button)

        vertical_layout = QtWidgets.QVBoxLayout()
        vertical_layout.addWidget(self.template_label)
        vertical_layout.addWidget(self.template_checkbox)
        vertical_layout.addWidget(self.template_combobox)
        vertical_layout.addWidget(self.template_slider)
        vertical_layout.addStretch()

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.addLayout(horizontal_layout)
        main_layout.addLayout(vertical_layout)
 
    def create_ui_connections(self):
        self.template_button.clicked.connect(self.template_command)
        self.template_icon_button.clicked.connect(self.template_command)
        self.template_slider.valueChanged.connect(self.template_command)

    def template_command(self):
        print("TEMPLATE!")

def start():
    global template_tool_ui
    try:
        template_tool_ui.close()
        template_tool_ui.deleteLater()
    except:
        pass
    template_tool_ui = TemplateToolWindow()
    template_tool_ui.show()

if __name__ == "__main__":
    start()