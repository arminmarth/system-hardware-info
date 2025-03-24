#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Disk information collector module.

This module provides functionality to collect disk-related system information.
"""

import psutil
from src.utils.formatters import format_bytes

class DiskCollector:
    """Collects disk-related system information."""
    
    @staticmethod
    def get_disk_partitions():
        """
        Get information about all disk partitions.
        
        Returns:
            list: A list of disk partition objects.
        """
        return psutil.disk_partitions()
    
    @staticmethod
    def get_disk_usage(mountpoint):
        """
        Get disk usage information for a specific mountpoint.
        
        Args:
            mountpoint (str): The mountpoint to get usage information for.
            
        Returns:
            tuple: A tuple containing (total, used, free, percent) or None if access is denied.
        """
        try:
            usage = psutil.disk_usage(mountpoint)
            return (
                format_bytes(usage.total),
                format_bytes(usage.used),
                format_bytes(usage.free),
                usage.percent
            )
        except PermissionError:
            return None
    
    @staticmethod
    def get_all_disk_info():
        """
        Get information about all accessible disk partitions.
        
        Returns:
            list: A list of dictionaries containing disk information.
        """
        partitions = psutil.disk_partitions()
        disk_info = []
        
        for partition in partitions:
            try:
                usage = psutil.disk_usage(partition.mountpoint)
                disk_info.append({
                    'mountpoint': partition.mountpoint,
                    'device': partition.device,
                    'fstype': partition.fstype,
                    'total': usage.total,
                    'used': usage.used,
                    'free': usage.free,
                    'percent': usage.percent
                })
            except PermissionError:
                # Skip partitions we can't access
                pass
                
        return disk_info
