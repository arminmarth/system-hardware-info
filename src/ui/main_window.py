#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Main window module for the System Hardware Info application.

This module defines the main application window and UI components.
"""

import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from src.utils.config import Config
from src.ui.cpu_section import CPUSection
from src.ui.memory_section import MemorySection
from src.ui.disk_section import DiskSection

class SystemHardwareInfoWindow(QtWidgets.QMainWindow):
    """Main window for the System Hardware Info application."""
    
    def __init__(self):
        """Initialize the main window."""
        super().__init__()
        
        # Set up the window
        self.setWindowTitle(Config.WINDOW_TITLE)
        self.resize(Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT)
        if Config.WINDOW_ICON:
            self.setWindowIcon(QtGui.QIcon(Config.WINDOW_ICON))
        
        # Create central widget and layout
        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QtWidgets.QVBoxLayout(self.central_widget)
        
        # Add application title
        self.title_label = QtWidgets.QLabel("System Hardware Information")
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setFont(QtGui.QFont(Config.FONT_FAMILY, 18, QtGui.QFont.Bold))
        self.main_layout.addWidget(self.title_label)
        
        # Add a separator line
        self.separator = QtWidgets.QFrame()
        self.separator.setFrameShape(QtWidgets.QFrame.HLine)
        self.separator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.main_layout.addWidget(self.separator)
        self.main_layout.addSpacing(10)
        
        # Add information sections
        self.cpu_section = CPUSection()
        self.main_layout.addWidget(self.cpu_section)
        
        self.memory_section = MemorySection()
        self.main_layout.addWidget(self.memory_section)
        
        self.disk_section = DiskSection()
        self.main_layout.addWidget(self.disk_section)
        
        # Add refresh button
        self.refresh_button = QtWidgets.QPushButton("Refresh Information")
        self.refresh_button.clicked.connect(self.refresh_info)
        self.main_layout.addWidget(self.refresh_button)
        
        # Set up auto-refresh timer
        if Config.ENABLE_AUTO_REFRESH:
            self.timer = QtCore.QTimer(self)
            self.timer.timeout.connect(self.refresh_info)
            self.timer.start(Config.AUTO_REFRESH_INTERVAL)
    
    def refresh_info(self):
        """Refresh all information sections."""
        self.cpu_section.refresh()
        self.memory_section.refresh()
        self.disk_section.refresh()
