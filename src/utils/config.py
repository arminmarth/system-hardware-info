#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Configuration module for the System Hardware Info application.

This module provides configuration settings for the application.
"""

class Config:
    """Configuration settings for the application."""
    
    # UI settings
    WINDOW_TITLE = "System Hardware Info"
    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 700
    WINDOW_ICON = None  # Path to icon file if available
    
    # Refresh settings
    AUTO_REFRESH_INTERVAL = 2000  # milliseconds
    ENABLE_AUTO_REFRESH = True
    
    # Display settings
    FONT_FAMILY = "Arial"
    SECTION_HEADER_SIZE = 14
    NORMAL_TEXT_SIZE = 10
    
    # Disk display settings
    MAX_DISK_SECTION_HEIGHT = 150
