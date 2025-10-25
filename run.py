#!/usr/bin/env python3
"""
Maxim Finance AI - Railway Entry Point
"""

import os
import sys

# Add app directory to path
app_dir = os.path.join(os.path.dirname(__file__), 'app')
if app_dir not in sys.path:
    sys.path.insert(0, app_dir)

# Import dan run main
from main import main

if __name__ == "__main__":
    main()
