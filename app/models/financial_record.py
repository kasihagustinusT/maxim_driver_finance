from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class FinancialRecord:
    timestamp: datetime
    total_order: float
    commission: float
    saldo_savings: float
    bbm_savings: float
    oli_savings: float
    net_income: float
    usable_income: float
    order_type: str = "Regular"
    custom_date: Optional[str] = None
    
    def to_dict(self):
        """Convert record to dictionary for serialization"""
        return {
            'timestamp': self.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            'total_order': self.total_order,
            'commission': self.commission,
            'saldo_savings': self.saldo_savings,
            'bbm_savings': self.bbm_savings,
            'oli_savings': self.oli_savings,
            'net_income': self.net_income,
            'usable_income': self.usable_income,
            'order_type': self.order_type,
            'custom_date': self.custom_date or ""
        }
