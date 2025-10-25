from dataclasses import dataclass
from typing import Dict, List, Any

@dataclass
class PerformanceMetrics:
    total_orders: int
    total_revenue: float
    total_net_income: float
    total_usable_income: float
    avg_order_value: float
    efficiency_ratio: float
    performance_score: float

@dataclass
class ChartData:
    revenue_trend: Dict[str, List]
    order_types: Dict[str, List]
    income_breakdown: Dict[str, List]
    daily_performance: Dict[str, List]

@dataclass
class AnalyticsData:
    summary: PerformanceMetrics
    time_metrics: Dict[str, Any]
    daily_analytics: Dict[str, Any]
    order_analytics: Dict[str, Any]
    financial_breakdown: Dict[str, float]
    ai_analysis: List[Dict]
    financial_tips: List[str]
    earnings_prediction: Dict[str, Any]
    chart_data: ChartData
