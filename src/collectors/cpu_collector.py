#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
CPU information collector module.

This module provides functionality to collect CPU-related system information.
"""

import psutil

class CPUCollector:
    """Collects CPU-related system information."""
    
    @staticmethod
    def get_cpu_count(logical=True):
        """
        Get the number of CPU cores.
        
        Args:
            logical (bool): If True, return the number of logical cores,
                           otherwise return the number of physical cores.
        
        Returns:
            int: The number of CPU cores.
        """
        return psutil.cpu_count(logical=logical)
    
    @staticmethod
    def get_cpu_frequency():
        """
        Get the current CPU frequency.
        
        Returns:
            str: The current CPU frequency formatted as "X.XX MHz".
                 Returns "N/A" if the frequency cannot be determined.
        """
        freq = psutil.cpu_freq()
        if freq is None:
            return "N/A"
        return f"{freq.current:.2f} MHz"
    
    @staticmethod
    def get_cpu_usage():
        """
        Get the current CPU usage percentage.
        
        Returns:
            str: The CPU usage percentage formatted as "X.X%".
        """
        return f"{psutil.cpu_percent():.1f}"
