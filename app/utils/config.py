import json
import os
from typing import Dict, Any

class Config:
    def __init__(self, config_file: str = 'data/config.json'):
        self.config_file = config_file
        self.config = self.load_config()

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
        os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
        with open(self.config_file, 'w') as file:
            json.dump(config, file, indent=4)

    def get(self, key: str, default=None):
        """Get configuration value"""
        return self.config.get(key, default)

    def set(self, key: str, value: Any):
        """Set configuration value"""
        self.config[key] = value
        self.save_config(self.config)
