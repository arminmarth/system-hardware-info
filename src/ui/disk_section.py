#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Disk section UI component for the System Hardware Info application.

This module defines the UI component for displaying disk information.
"""

from PyQt5 import QtWidgets, QtCore, QtGui
from src.utils.config import Config
from src.collectors.disk_collector import DiskCollector

class DiskSection(QtWidgets.QWidget):
    """UI component for displaying disk information."""
    
    def __init__(self):
        """Initialize the disk section."""
        super().__init__()
        
        # Create layout
        self.layout = QtWidgets.QVBoxLayout(self)
        
        # Section header
        self.header_label = QtWidgets.QLabel("Disk Information:")
        self.header_label.setAlignment(QtCore.Qt.AlignLeft)
        self.header_label.setFont(QtGui.QFont(Config.FONT_FAMILY, Config.SECTION_HEADER_SIZE, QtGui.QFont.Bold))
        self.layout.addWidget(self.header_label)
        
        # Create a scrollable area for disk information
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_content = QtWidgets.QWidget()
        self.scroll_layout = QtWidgets.QVBoxLayout(self.scroll_content)
        
        # Initialize partition labels list
        self.partition_labels = []
        
        # Set up scroll area
        self.scroll_content.setLayout(self.scroll_layout)
        self.scroll_area.setWidget(self.scroll_content)
        self.scroll_area.setMaximumHeight(Config.MAX_DISK_SECTION_HEIGHT)
        self.layout.addWidget(self.scroll_area)
        
        # Add a spacer
        self.layout.addSpacing(10)
        
        # Initialize with data
        self.refresh()
    
    def refresh(self):
        """Refresh disk information."""
        # Clear existing partition labels
        for label in self.partition_labels:
            label.deleteLater()
        self.partition_labels.clear()
        
        # Get disk partitions
        partitions = DiskCollector.get_disk_partitions()
        
        # Add information for each partition
        for partition in partitions:
            usage_info = DiskCollector.get_disk_usage(partition.mountpoint)
            if usage_info:
                total, used, free, percent = usage_info
                label = QtWidgets.QLabel()
                label.setText(f"Partition: {partition.mountpoint}\n"
                             f"  Total: {total}\n"
                             f"  Used: {used} ({percent:.1f}%)\n"
                             f"  Free: {free}")
                self.scroll_layout.addWidget(label)
                self.partition_labels.append(label)
