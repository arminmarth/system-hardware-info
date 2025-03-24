#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
CPU section UI component for the System Hardware Info application.

This module defines the UI component for displaying CPU information.
"""

from PyQt5 import QtWidgets, QtCore, QtGui
from src.utils.config import Config
from src.collectors.cpu_collector import CPUCollector

class CPUSection(QtWidgets.QWidget):
    """UI component for displaying CPU information."""
    
    def __init__(self):
        """Initialize the CPU section."""
        super().__init__()
        
        # Create layout
        self.layout = QtWidgets.QVBoxLayout(self)
        
        # Section header
        self.header_label = QtWidgets.QLabel("CPU Information:")
        self.header_label.setAlignment(QtCore.Qt.AlignLeft)
        self.header_label.setFont(QtGui.QFont(Config.FONT_FAMILY, Config.SECTION_HEADER_SIZE, QtGui.QFont.Bold))
        self.layout.addWidget(self.header_label)
        
        # CPU core information
        self.cores_label = QtWidgets.QLabel()
        self.layout.addWidget(self.cores_label)
        
        # CPU frequency information
        self.frequency_label = QtWidgets.QLabel()
        self.layout.addWidget(self.frequency_label)
        
        # CPU usage information
        self.usage_label = QtWidgets.QLabel()
        self.layout.addWidget(self.usage_label)
        
        # Add a spacer
        self.layout.addSpacing(10)
        
        # Initialize with data
        self.refresh()
    
    def refresh(self):
        """Refresh CPU information."""
        # Update CPU core information
        physical_cores = CPUCollector.get_cpu_count(logical=False)
        logical_cores = CPUCollector.get_cpu_count(logical=True)
        self.cores_label.setText(f"Cores: {physical_cores} physical, {logical_cores} logical")
        
        # Update CPU frequency information
        self.frequency_label.setText(f"Frequency: {CPUCollector.get_cpu_frequency()}")
        
        # Update CPU usage information
        self.usage_label.setText(f"Usage: {CPUCollector.get_cpu_usage()}%")
