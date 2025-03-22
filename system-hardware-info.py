#!/usr/bin/env python3
"""
System Hardware Information
A simple Python program that displays system hardware information using a PyQt GUI.
"""
import sys
import psutil
from PyQt5 import QtCore, QtGui, QtWidgets


class SystemHardwareInfo(QtWidgets.QMainWindow):
    """Main application window for displaying system hardware information."""
    
    def __init__(self):
        """Initialize the application window and UI components."""
        super().__init__()

        # Set the window title and size
        self.setWindowTitle("System Hardware Information")
        self.resize(400, 500)

        # Create a vertical layout to hold the labels
        layout = QtWidgets.QVBoxLayout()
        
        # Add CPU information section
        self._add_cpu_section(layout)
        
        # Add Memory information section
        self._add_memory_section(layout)
        
        # Add Disk information section (new)
        self._add_disk_section(layout)
        
        # Add refresh button
        self._add_refresh_button(layout)

        # Set the central widget of the window to a widget containing the layout
        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
        # Set up a timer to refresh the information every 2 seconds
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.refresh_info)
        self.timer.start(2000)  # 2000 milliseconds = 2 seconds

    def _add_cpu_section(self, layout):
        """Add CPU information section to the layout."""
        # Section header
        self.cpu_label = QtWidgets.QLabel("CPU Information:")
        self.cpu_label.setAlignment(QtCore.Qt.AlignLeft)
        self.cpu_label.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Bold))
        layout.addWidget(self.cpu_label)
        
        # CPU count
        self.cpu_count_label = QtWidgets.QLabel()
        self.cpu_count_label.setText(f"Cores: {psutil.cpu_count(logical=True)} (Logical), {psutil.cpu_count(logical=False)} (Physical)")
        self.cpu_count_label.setAlignment(QtCore.Qt.AlignLeft)
        layout.addWidget(self.cpu_count_label)

        # CPU frequency
        self.cpu_frequency_label = QtWidgets.QLabel()
        self.cpu_frequency_label.setText(f"Frequency: {self._get_cpu_frequency()}")
        self.cpu_frequency_label.setAlignment(QtCore.Qt.AlignLeft)
        layout.addWidget(self.cpu_frequency_label)

        # CPU usage
        self.cpu_usage_label = QtWidgets.QLabel()
        self.cpu_usage_label.setText(f"Usage: {self._get_cpu_usage()}%")
        self.cpu_usage_label.setAlignment(QtCore.Qt.AlignLeft)
        layout.addWidget(self.cpu_usage_label)
        
        # Add a spacer
        layout.addSpacing(10)

    def _add_memory_section(self, layout):
        """Add Memory information section to the layout."""
        # Section header
        self.memory_label = QtWidgets.QLabel("Memory Information:")
        self.memory_label.setAlignment(QtCore.Qt.AlignLeft)
        self.memory_label.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Bold))
        layout.addWidget(self.memory_label)

        # Total memory
        self.total_memory_label = QtWidgets.QLabel()
        self.total_memory_label.setText(f"Total: {self._get_total_memory()}")
        self.total_memory_label.setAlignment(QtCore.Qt.AlignLeft)
        layout.addWidget(self.total_memory_label)

        # Used memory
        self.used_memory_label = QtWidgets.QLabel()
        self.used_memory_label.setText(f"Used: {self._get_used_memory()}")
        self.used_memory_label.setAlignment(QtCore.Qt.AlignLeft)
        layout.addWidget(self.used_memory_label)

        # Available memory
        self.available_memory_label = QtWidgets.QLabel()
        self.available_memory_label.setText(f"Available: {self._get_available_memory()}")
        self.available_memory_label.setAlignment(QtCore.Qt.AlignLeft)
        layout.addWidget(self.available_memory_label)
        
        # Memory usage percentage
        self.memory_percent_label = QtWidgets.QLabel()
        self.memory_percent_label.setText(f"Usage: {psutil.virtual_memory().percent}%")
        self.memory_percent_label.setAlignment(QtCore.Qt.AlignLeft)
        layout.addWidget(self.memory_percent_label)
        
        # Add a spacer
        layout.addSpacing(10)
    
    def _add_disk_section(self, layout):
        """Add Disk information section to the layout."""
        # Section header
        self.disk_label = QtWidgets.QLabel("Disk Information:")
        self.disk_label.setAlignment(QtCore.Qt.AlignLeft)
        self.disk_label.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Bold))
        layout.addWidget(self.disk_label)
        
        # Get disk partitions
        partitions = psutil.disk_partitions()
        
        # Create a scrollable area for disk information
        scroll_area = QtWidgets.QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_content = QtWidgets.QWidget()
        scroll_layout = QtWidgets.QVBoxLayout(scroll_content)
        
        # Add information for each partition
        self.partition_labels = []
        for partition in partitions:
            try:
                usage = psutil.disk_usage(partition.mountpoint)
                label = QtWidgets.QLabel()
                label.setText(f"Partition: {partition.mountpoint}\n"
                             f"  Total: {self._format_bytes(usage.total)}\n"
                             f"  Used: {self._format_bytes(usage.used)} ({usage.percent}%)\n"
                             f"  Free: {self._format_bytes(usage.free)}")
                scroll_layout.addWidget(label)
                self.partition_labels.append(label)
            except PermissionError:
                # Skip partitions we can't access
                pass
        
        scroll_content.setLayout(scroll_layout)
        scroll_area.setWidget(scroll_content)
        scroll_area.setMaximumHeight(150)
        layout.addWidget(scroll_area)
        
        # Add a spacer
        layout.addSpacing(10)
    
    def _add_refresh_button(self, layout):
        """Add a refresh button to manually update information."""
        self.refresh_button = QtWidgets.QPushButton("Refresh Information")
        self.refresh_button.clicked.connect(self.refresh_info)
        layout.addWidget(self.refresh_button)

    def refresh_info(self):
        """Update all displayed information."""
        # Update CPU information
        self.cpu_frequency_label.setText(f"Frequency: {self._get_cpu_frequency()}")
        self.cpu_usage_label.setText(f"Usage: {self._get_cpu_usage()}%")
        
        # Update memory information
        self.total_memory_label.setText(f"Total: {self._get_total_memory()}")
        self.used_memory_label.setText(f"Used: {self._get_used_memory()}")
        self.available_memory_label.setText(f"Available: {self._get_available_memory()}")
        self.memory_percent_label.setText(f"Usage: {psutil.virtual_memory().percent}%")
        
        # Update disk information
        partitions = psutil.disk_partitions()
        for i, partition in enumerate(partitions):
            if i < len(self.partition_labels):
                try:
                    usage = psutil.disk_usage(partition.mountpoint)
                    self.partition_labels[i].setText(
                        f"Partition: {partition.mountpoint}\n"
                        f"  Total: {self._format_bytes(usage.total)}\n"
                        f"  Used: {self._format_bytes(usage.used)} ({usage.percent}%)\n"
                        f"  Free: {self._format_bytes(usage.free)}"
                    )
                except PermissionError:
                    # Skip partitions we can't access
                    pass

    def _get_cpu_frequency(self):
        """Get the CPU frequency."""
        freq = psutil.cpu_freq()
        if freq is None:
            return "N/A"
        return f"{freq.current:.2f} MHz"

    def _get_cpu_usage(self):
        """Get the CPU usage percentage."""
        return f"{psutil.cpu_percent():.1f}"

    def _get_total_memory(self):
        """Get the total memory."""
        total_memory = psutil.virtual_memory().total
        return self._format_bytes(total_memory)

    def _get_used_memory(self):
        """Get the used memory."""
        used_memory = psutil.virtual_memory().used
        return self._format_bytes(used_memory)

    def _get_available_memory(self):
        """Get the available memory."""
        available_memory = psutil.virtual_memory().available
        return self._format_bytes(available_memory)
    
    def _format_bytes(self, bytes_value):
        """Format bytes to appropriate unit (B, KB, MB, GB, TB)."""
        units = ['B', 'KB', 'MB', 'GB', 'TB']
        unit_index = 0
        value = float(bytes_value)
        
        while value >= 1024 and unit_index < len(units) - 1:
            value /= 1024
            unit_index += 1
            
        return f"{value:.2f} {units[unit_index]}"


if __name__ == "__main__":
    # Create the application
    app = QtWidgets.QApplication(sys.argv)
    
    # Set application style
    app.setStyle('Fusion')
    
    # Create and show the main window
    window = SystemHardwareInfo()
    window.show()
    
    # Start the application event loop
    sys.exit(app.exec_())
