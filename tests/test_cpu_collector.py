#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Test module for CPU collector functionality.

This module contains tests for the CPU collector class.
"""

import unittest
from unittest.mock import patch, MagicMock
from src.collectors.cpu_collector import CPUCollector

class TestCPUCollector(unittest.TestCase):
    """Test cases for the CPU collector."""
    
    @patch('psutil.cpu_count')
    def test_get_cpu_count(self, mock_cpu_count):
        """Test getting CPU count."""
        # Set up mock
        mock_cpu_count.return_value = 8
        
        # Test logical cores
        result = CPUCollector.get_cpu_count(logical=True)
        self.assertEqual(result, 8)
        mock_cpu_count.assert_called_with(logical=True)
        
        # Test physical cores
        mock_cpu_count.reset_mock()
        mock_cpu_count.return_value = 4
        result = CPUCollector.get_cpu_count(logical=False)
        self.assertEqual(result, 4)
        mock_cpu_count.assert_called_with(logical=False)
    
    @patch('psutil.cpu_freq')
    def test_get_cpu_frequency(self, mock_cpu_freq):
        """Test getting CPU frequency."""
        # Set up mock for normal case
        mock_freq = MagicMock()
        mock_freq.current = 2500.0
        mock_cpu_freq.return_value = mock_freq
        
        # Test normal case
        result = CPUCollector.get_cpu_frequency()
        self.assertEqual(result, "2500.00 MHz")
        
        # Test case where frequency is not available
        mock_cpu_freq.return_value = None
        result = CPUCollector.get_cpu_frequency()
        self.assertEqual(result, "N/A")
    
    @patch('psutil.cpu_percent')
    def test_get_cpu_usage(self, mock_cpu_percent):
        """Test getting CPU usage."""
        # Set up mock
        mock_cpu_percent.return_value = 25.5
        
        # Test
        result = CPUCollector.get_cpu_usage()
        self.assertEqual(result, "25.5")
        mock_cpu_percent.assert_called_once()

if __name__ == '__main__':
    unittest.main()
