#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Memory information collector module.

This module provides functionality to collect memory-related system information.
"""

import psutil
from src.utils.formatters import format_bytes

class MemoryCollector:
    """Collects memory-related system information."""
    
    @staticmethod
    def get_total_memory():
        """
        Get the total system memory.
        
        Returns:
            str: The total memory formatted with appropriate units.
        """
        total_memory = psutil.virtual_memory().total
        return format_bytes(total_memory)
    
    @staticmethod
    def get_used_memory():
        """
        Get the used system memory.
        
        Returns:
            str: The used memory formatted with appropriate units.
        """
        used_memory = psutil.virtual_memory().used
        return format_bytes(used_memory)
    
    @staticmethod
    def get_available_memory():
        """
        Get the available system memory.
        
        Returns:
            str: The available memory formatted with appropriate units.
        """
        available_memory = psutil.virtual_memory().available
        return format_bytes(available_memory)
    
    @staticmethod
    def get_memory_percent():
        """
        Get the memory usage percentage.
        
        Returns:
            float: The memory usage percentage.
        """
        return psutil.virtual_memory().percent
