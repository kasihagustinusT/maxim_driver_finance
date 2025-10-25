import csv
import os
import json
from datetime import datetime
from typing import List, Dict, Any

class DataHandler:
    def __init__(self, data_file: str = 'data/riwayat_orderan.csv', config_file: str = 'data/config.json'):
        self.data_file = data_file
        self.config_file = config_file
        self.ensure_directories()

    def ensure_directories(self):
        """Ensure data directory exists"""
        os.makedirs('data', exist_ok=True)

    def clean_numeric_value(self, value: Any) -> float:
        """Clean and convert numeric values from CSV"""
        if not value or value == '':
            return 0.0
        
        value_str = str(value).strip()
        cleaned = ''.join(ch for ch in value_str if ch.isdigit() or ch == '.' or ch == '-')
        
        if not cleaned or cleaned == '-' or cleaned == '.':
            return 0.0
            
        try:
            return float(cleaned)
        except (ValueError, TypeError):
            return 0.0

    def initialize_data_file(self):
        """Initialize CSV file with headers"""
        if not os.path.exists(self.data_file) or os.stat(self.data_file).st_size == 0:
            with open(self.data_file, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([
                    'Tanggal & Jam', 'Total Orderan', 'Komisi (15%)',
                    'Tabungan Saldo (10%)', 'Tabungan BBM (10%)', 'Tabungan Oli (10%)',
                    'Pendapatan Bersih', 'Pendapatan Siap Pakai', 'Jenis Orderan', 'Tanggal Custom'
                ])

    def migrate_data_file(self):
        """Migrate existing data file to include Tanggal Custom column"""
        try:
            with open(self.data_file, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                rows = list(reader)
                
            if rows and 'Tanggal Custom' not in rows[0]:
                rows[0].append('Tanggal Custom')
                for i in range(1, len(rows)):
                    if len(rows[i]) < len(rows[0]):
                        rows[i].append('')
                
                with open(self.data_file, 'w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerows(rows)
                    
        except Exception as e:
            print(f"⚠️ Migration failed: {e}")

    def load_config(self) -> Dict[str, Any]:
        """Load configuration from JSON file"""
        try:
            with open(self.config_file, 'r') as file:
                return json.load(file)
        except:
            default_config = {
                "company_name": "Maxim Finance AI",
                "tax_rate": 0.0,
                "currency": "IDR",
                "performance_metrics": {
                    "target_daily_income": 200000,
                    "target_weekly_orders": 20,
                    "efficiency_threshold": 50.0
                }
            }
            self.save_config(default_config)
            return default_config

    def save_config(self, config: Dict[str, Any]):
        """Save configuration to JSON file"""
        with open(self.config_file, 'w') as file:
            json.dump(config, file, indent=4)

    def save_record(self, record_data: List):
        """Save record to CSV"""
        with open(self.data_file, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(record_data)

    def load_all_data(self) -> List[Dict[str, Any]]:
        """Load all data from CSV"""
        if not os.path.exists(self.data_file) or os.stat(self.data_file).st_size == 0:
            return []

        data = []
        with open(self.data_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for i, row in enumerate(reader):
                try:
                    if not any(row.values()):
                        continue
                        
                    row_values = ' '.join(str(v) for v in row.values()).lower()
                    if any(header in row_values for header in ['tanggal', 'orderan', 'komisi', 'tabungan', 'pendapatan']):
                        continue
                    
                    custom_date = row.get('Tanggal Custom', '')
                    
                    if custom_date and custom_date.strip():
                        display_date = custom_date
                    else:
                        timestamp_str = row.get('Tanggal & Jam', '')
                        if timestamp_str:
                            try:
                                display_date = timestamp_str.split(' ')[0]
                                datetime.strptime(display_date, '%Y-%m-%d')
                            except (ValueError, IndexError):
                                display_date = datetime.now().strftime('%Y-%m-%d')
                        else:
                            display_date = datetime.now().strftime('%Y-%m-%d')
                    
                    data.append({
                        'timestamp': row.get('Tanggal & Jam', ''),
                        'total_order': self.clean_numeric_value(row.get('Total Orderan', '0')),
                        'commission': self.clean_numeric_value(row.get('Komisi (15%)', '0')),
                        'saldo_savings': self.clean_numeric_value(row.get('Tabungan Saldo (10%)', '0')),
                        'bbm_savings': self.clean_numeric_value(row.get('Tabungan BBM (10%)', '0')),
                        'oli_savings': self.clean_numeric_value(row.get('Tabungan Oli (10%)', '0')),
                        'net_income': self.clean_numeric_value(row.get('Pendapatan Bersih', '0')),
                        'usable_income': self.clean_numeric_value(row.get('Pendapatan Siap Pakai', '0')),
                        'order_type': row.get('Jenis Orderan', 'Regular'),
                        'custom_date': custom_date,
                        'display_date': display_date
                    })
                    
                except (KeyError, ValueError, AttributeError) as e:
                    print(f"⚠️ Error parsing row {i}: {e}")
                    continue

        return data

    def delete_records(self, indices: List[int]) -> bool:
        """Delete records by indices"""
        try:
            with open(self.data_file, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                rows = list(reader)

            if len(rows) <= 1:
                return False

            valid_indices = [i + 1 for i in indices if 0 <= i < (len(rows) - 1)]
            if not valid_indices:
                return False

            for i in sorted(valid_indices, reverse=True):
                if i < len(rows):
                    rows.pop(i)

            with open(self.data_file, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerows(rows)

            return True
        except Exception as e:
            print(f"❌ Error deleting records: {e}")
            return False
