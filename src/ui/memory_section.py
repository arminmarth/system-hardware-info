#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Memory section UI component for the System Hardware Info application.

This module defines the UI component for displaying memory information.
"""

from PyQt5 import QtWidgets, QtCore, QtGui
from src.utils.config import Config
from src.collectors.memory_collector import MemoryCollector

class MemorySection(QtWidgets.QWidget):
    """UI component for displaying memory information."""
    
    def __init__(self):
        """Initialize the memory section."""
        super().__init__()
        
        # Create layout
        self.layout = QtWidgets.QVBoxLayout(self)
        
        # Section header
        self.header_label = QtWidgets.QLabel("Memory Information:")
        self.header_label.setAlignment(QtCore.Qt.AlignLeft)
        self.header_label.setFont(QtGui.QFont(Config.FONT_FAMILY, Config.SECTION_HEADER_SIZE, QtGui.QFont.Bold))
        self.layout.addWidget(self.header_label)
        
        # Total memory information
        self.total_memory_label = QtWidgets.QLabel()
        self.layout.addWidget(self.total_memory_label)
        
        # Used memory information
        self.used_memory_label = QtWidgets.QLabel()
        self.layout.addWidget(self.used_memory_label)
        
        # Available memory information
        self.available_memory_label = QtWidgets.QLabel()
        self.layout.addWidget(self.available_memory_label)
        
        # Memory usage percentage
        self.memory_percent_label = QtWidgets.QLabel()
        self.layout.addWidget(self.memory_percent_label)
        
        # Add a spacer
        self.layout.addSpacing(10)
        
        # Initialize with data
        self.refresh()
    
    def refresh(self):
        """Refresh memory information."""
        # Update total memory information
        self.total_memory_label.setText(f"Total: {MemoryCollector.get_total_memory()}")
        
        # Update used memory information
        self.used_memory_label.setText(f"Used: {MemoryCollector.get_used_memory()}")
        
        # Update available memory information
        self.available_memory_label.setText(f"Available: {MemoryCollector.get_available_memory()}")
        
        # Update memory usage percentage
        self.memory_percent_label.setText(f"Usage: {MemoryCollector.get_memory_percent():.1f}%")
