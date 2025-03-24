#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Test module for formatters utility functions.

This module contains tests for the formatters utility functions.
"""

import unittest
from src.utils.formatters import format_bytes

class TestFormatters(unittest.TestCase):
    """Test cases for the formatters utility functions."""
    
    def test_format_bytes(self):
        """Test formatting bytes to appropriate units."""
        # Test bytes
        self.assertEqual(format_bytes(500), "500.00 B")
        
        # Test kilobytes
        self.assertEqual(format_bytes(1500), "1.46 KB")
        
        # Test megabytes
        self.assertEqual(format_bytes(1500000), "1.43 MB")
        
        # Test gigabytes
        self.assertEqual(format_bytes(1500000000), "1.40 GB")
        
        # Test terabytes
        self.assertEqual(format_bytes(1500000000000), "1.36 TB")
        
        # Test zero
        self.assertEqual(format_bytes(0), "0.00 B")

if __name__ == '__main__':
    unittest.main()
