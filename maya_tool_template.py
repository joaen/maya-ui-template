import sys
import maya.cmds as cmds
import maya.OpenMayaUI as omui
from shiboken2 import wrapInstance
from PySide2 import QtCore
from PySide2 import QtWidgets


def maya_main_window():
    # Return the Maya main window as QMainWindow
    main_window = omui.MQtUtil.mainWindow()
    if sys.version_info.major >= 3:
        return wrapInstance(int(main_window), QtWidgets.QWidget)
    else:
        return wrapInstance(long(main_window), QtWidgets.QWidget)

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
        self.template_button = QtWidgets.QPushButton("TEMPLATE BUTTON")
        
    def create_ui_layout(self):

        lower_row_buttons = QtWidgets.QHBoxLayout()
        lower_row_buttons.addWidget(self.template_button)
 
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.addLayout(lower_row_buttons)
 
    def create_ui_connections(self):
        self.template_button.clicked.connect(self.template_command)

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