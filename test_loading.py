#!/usr/bin/env python3
"""
Test script untuk check data loading
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.services.data_handler import DataHandler

def test_data_loading():
    print("🧪 Testing data loading...")
    
    handler = DataHandler()
    
    # Test config loading
    config = handler.load_config()
    print(f"✅ Config loaded: {config.get('company_name')}")
    
    # Test data loading
    data = handler.load_all_data()
    print(f"✅ Data records loaded: {len(data)}")
    
    if data:
        print("📊 Sample record:")
        print(data[0])
    else:
        print("ℹ️ No data records found")
    
    print("🎉 Test completed!")

if __name__ == "__main__":
    test_data_loading()
