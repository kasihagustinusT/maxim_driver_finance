#!/usr/bin/env python3
"""
Emergency fix untuk permissions dan data corruption
"""

import os
import sys
import csv
import json
from datetime import datetime

def fix_all_issues():
    print("🔧 Memperbaiki issues...")
    
    # 1. Fix folder permissions
    data_dir = 'data'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        print("✅ Created data directory")
    
    # 2. Fix file permissions
    csv_file = os.path.join(data_dir, 'riwayat_orderan.csv')
    config_file = os.path.join(data_dir, 'config.json')
    
    try:
        # Fix CSV file
        if not os.path.exists(csv_file) or os.stat(csv_file).st_size == 0:
            print("📝 Creating new CSV file with headers...")
            with open(csv_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([
                    'Tanggal & Jam', 'Total Orderan', 'Komisi (15%)',
                    'Tabungan Saldo (10%)', 'Tabungan BBM (10%)', 'Tabungan Oli (10%)',
                    'Pendapatan Bersih', 'Pendapatan Siap Pakai', 'Jenis Orderan', 'Tanggal Custom'
                ])
            print("✅ CSV file created")
        
        # Fix config file
        if not os.path.exists(config_file):
            print("⚙️ Creating config file...")
            config = {
                "company_name": "Maxim Finance AI",
                "tax_rate": 0.0,
                "currency": "IDR",
                "performance_metrics": {
                    "target_daily_income": 200000,
                    "target_weekly_orders": 20,
                    "efficiency_threshold": 50.0
                }
            }
            with open(config_file, 'w') as f:
                json.dump(config, f, indent=2)
            print("✅ Config file created")
        
        # 3. Set proper permissions
        os.chmod(data_dir, 0o755)
        os.chmod(csv_file, 0o644)
        os.chmod(config_file, 0o644)
        print("✅ Permissions fixed")
        
        # 4. Add sample data jika kosong
        with open(csv_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            if len(lines) <= 1:  # Hanya header
                print("📊 Adding sample data...")
                with open(csv_file, 'a', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    # Add 2 sample records
                    sample_data = [
                        [
                            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            100000, 15000, 10000, 10000, 10000, 85000, 55000, "Regular", ""
                        ],
                        [
                            (datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S"),
                            150000, 22500, 15000, 15000, 15000, 127500, 82500, "Premium", ""
                        ]
                    ]
                    for data in sample_data:
                        writer.writerow(data)
                print("✅ Sample data added")
        
        print("🎉 All issues fixed!")
        
    except Exception as e:
        print(f"❌ Error during fix: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    fix_all_issues()
