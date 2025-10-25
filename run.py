#!/usr/bin/env python3
"""
Maxim Finance AI - Railway Entry Point
"""

import os
import sys

# Install package in development mode
sys.path.insert(0, os.path.dirname(__file__))

from app.main import main

if __name__ == "__main__":
    main()
