import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel
from PyQt5.QtGui import QIcon
import psutil

class SystemHardwareInfo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # Create a grid layout to arrange the widgets
        grid = QGridLayout()
        self.setLayout(grid)
        
        # Create a label for each piece of hardware information
        cpu_label = QLabel('CPU:')
        mem_label = QLabel('Memory:')
        disk_label = QLabel('Disk:')
        
        # Retrieve the hardware information using the psutil library
        cpu_percent = psutil.cpu_percent()
        mem_info = psutil.virtual_memory()
        disk_info = psutil.disk_usage('/')
        
        # Format the hardware information as strings
        cpu_text = f'{cpu_percent}%'
        mem_text = f'{mem_info.used / 1024**3:.1f} GB / {mem_info.total / 1024**3:.1f} GB'
        disk_text = f'{disk_info.used / 1024**3:.1f} GB / {disk_info.total / 1024**3:.1f} GB'
        
        # Create labels to display the hardware information
        cpu_value_label = QLabel(cpu_text)
        mem_value_label = QLabel(mem_text)
        disk_value_label = QLabel(disk_text)
        
        # Add the labels to the grid layout
        grid.addWidget(cpu_label, 0, 0)
        grid.addWidget(mem_label, 1, 0)
        grid.addWidget(disk_label, 2, 0)
        grid.addWidget(cpu_value_label, 0, 1)
        grid.addWidget(mem_value_label, 1, 1)
        grid.addWidget(disk_value_label, 2, 1)
        
        # Set the window title and icon
        self.setWindowTitle('System Hardware Info')
        self.setWindowIcon(QIcon('icon.png'))
        
        # Show the window
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SystemHardwareInfo()
    sys.exit(app.exec_())
