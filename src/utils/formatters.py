#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Utility functions for formatting data.

This module provides utility functions for formatting various types of data.
"""

def format_bytes(bytes_value):
    """
    Format bytes to appropriate unit (B, KB, MB, GB, TB).
    
    Args:
        bytes_value (int): The value in bytes to format.
        
    Returns:
        str: The formatted string with appropriate unit.
    """
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    unit_index = 0
    value = float(bytes_value)
    
    while value >= 1024 and unit_index < len(units) - 1:
        value /= 1024
        unit_index += 1
        
    return f"{value:.2f} {units[unit_index]}"
