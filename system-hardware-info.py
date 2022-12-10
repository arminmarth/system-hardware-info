# Import the required modules
import psutil
from PyQt5 import QtCore, QtGui, QtWidgets

class SystemHardwareInfo(QtWidgets.QMainWindow):
    # Initialize the window
    def __init__(self):
        super().__init__()

        # Set the window title
        self.setWindowTitle("System Hardware Information")

        # Create a vertical layout to hold the labels
        layout = QtWidgets.QVBoxLayout()

        # Create a label for the CPU information
        self.cpu_label = QtWidgets.QLabel()
        self.cpu_label.setText("CPU Information:")
        self.cpu_label.setAlignment(QtCore.Qt.AlignLeft)
        self.cpu_label.setFont(QtGui.QFont("Arial", 14))
        layout.addWidget(self.cpu_label)

#        # Create a label to show the CPU model
#        self.cpu_model_label = QtWidgets.QLabel()
#        self.cpu_model_label.setText("Model: " + self.get_cpu_model())
#        self.cpu_model_label.setAlignment(QtCore.Qt.AlignLeft)
#        layout.addWidget(self.cpu_model_label)

        # Create a label to show the CPU frequency
        self.cpu_frequency_label = QtWidgets.QLabel()
        self.cpu_frequency_label.setText("Frequency: " + self.get_cpu_frequency())
        self.cpu_frequency_label.setAlignment(QtCore.Qt.AlignLeft)
        layout.addWidget(self.cpu_frequency_label)

        # Create a label to show the CPU usage
        self.cpu_usage_label = QtWidgets.QLabel()
        self.cpu_usage_label.setText("Usage: " + self.get_cpu_usage() + "%")
        self.cpu_usage_label.setAlignment(QtCore.Qt.AlignLeft)
        layout.addWidget(self.cpu_usage_label)

        # Create a label for the memory information
        self.memory_label = QtWidgets.QLabel()
        self.memory_label.setText("Memory Information:")
        self.memory_label.setAlignment(QtCore.Qt.AlignLeft)
        self.memory_label.setFont(QtGui.QFont("Arial", 14))
        layout.addWidget(self.memory_label)

        # Create a label to show the total memory
        self.total_memory_label = QtWidgets.QLabel()
        self.total_memory_label.setText("Total: " + self.get_total_memory())
        self.total_memory_label.setAlignment(QtCore.Qt.AlignLeft)
        layout.addWidget(self.total_memory_label)

        # Create a label to show the used memory
        self.used_memory_label = QtWidgets.QLabel()
        self.used_memory_label.setText("Used: " + self.get_used_memory())
        self.used_memory_label.setAlignment(QtCore.Qt.AlignLeft)
        layout.addWidget(self.used_memory_label)

        # Create a label to show the available memory
        self.available_memory_label = QtWidgets.QLabel()
        self.available_memory_label.setText("Available: " + self.get_available_memory())
        self.available_memory_label.setAlignment(QtCore.Qt.AlignLeft)
        layout.addWidget(self.available_memory_label)

        # Set the central widget of the window to a widget containing the layout
        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

#    # Get the CPU model
#    def get_cpu_model(self):
#        # Use the psutil module to get the CPU model
#        return psutil.cpu_freq().model

    # Get the CPU frequency
    def get_cpu_frequency(self):
        # Use the psutil module to get the CPU frequency
        return str(psutil.cpu_freq().current) + " MHz"

    # Get the CPU usage
    def get_cpu_usage(self):
        # Use the psutil module to get the CPU usage
        return str(psutil.cpu_percent())

    # Get the total memory
    def get_total_memory(self):
        # Use the psutil module to get the total memory
        total_memory = psutil.virtual_memory().total
        # Convert the memory to the appropriate unit
        if total_memory >= 1073741824:
            total_memory = str(round(total_memory / 1073741824, 2)) + " GB"
        elif total_memory >= 1048576:
            total_memory = str(round(total_memory / 1048576, 2)) + " MB"
        elif total_memory >= 1024:
            total_memory = str(round(total_memory / 1024, 2)) + " KB"
        else:
            total_memory = str(total_memory) + " B"
        return total_memory

    # Get the used memory
    def get_used_memory(self):
        # Use the psutil module to get the used memory
        used_memory = psutil.virtual_memory().used
        # Convert the memory to the appropriate unit
        if used_memory >= 1073741824:
            used_memory = str(round(used_memory / 1073741824, 2)) + " GB"
        elif used_memory >= 1048576:
            used_memory = str(round(used_memory / 1048576, 2)) + " MB"
        elif used_memory >= 1024:
            used_memory = str(round(used_memory / 1024, 2)) + " KB"
        else:
            used_memory = str(used_memory) + " B"
        return used_memory

    # Get the available memory
    def get_available_memory(self):
        # Use the psutil module to get the available memory
        available_memory = psutil.virtual_memory().available
        # Convert the memory to the appropriate unit
        if available_memory >= 1073741824:
            available_memory = str(round(available_memory / 1073741824, 2)) + " GB"
        elif available_memory >= 1048576:
            available_memory = str(round(available_memory / 1048576, 2)) + " MB"
        elif available_memory >= 1024:
            available_memory = str(round(available_memory / 1024, 2)) + " KB"
        else:
            available_memory = str(available_memory) + " B"
        return available_memory


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = SystemHardwareInfo()
    window.show()
    app.exec_()
