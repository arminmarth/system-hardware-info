#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
System Hardware Info - Main Application

This module serves as the entry point for the System Hardware Info application.
It initializes the application and launches the main window.
"""

import sys
from PyQt5 import QtWidgets
from src.ui.main_window import SystemHardwareInfoWindow

def main():
    """Initialize and run the application."""
    # Create the application
    app = QtWidgets.QApplication(sys.argv)
    
    # Set application style
    app.setStyle('Fusion')
    
    # Create and show the main window
    window = SystemHardwareInfoWindow()
    window.show()
    
    # Start the application event loop
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
