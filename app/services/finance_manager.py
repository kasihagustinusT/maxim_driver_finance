from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional

from ..models.financial_record import FinancialRecord
from .ai_advisor import AIFinanceAdvisor
from .data_handler import DataHandler

class ExpertFinanceManager:
    def __init__(self):
        self.data_handler = DataHandler()
        self.ai_advisor = AIFinanceAdvisor()
        self.config = self.data_handler.load_config()
        
        # Constants
        self.COMMISSION_RATE = 0.15
        self.SALDO_SAVINGS_RATE = 0.10
        self.BBM_SAVINGS_RATE = 0.10
        self.OLI_SAVINGS_RATE = 0.10
        
        self.initialize_files()

    def initialize_files(self):
        """Initialize file data"""
        self.data_handler.initialize_data_file()
        self.data_handler.migrate_data_file()

    def update_config(self, new_config: Dict[str, Any]) -> Dict[str, Any]:
        """Update configuration dengan validasi"""
        try:
            if 'performance_metrics' in new_config:
                if 'performance_metrics' not in self.config:
                    self.config['performance_metrics'] = {}
                
                for key, value in new_config['performance_metrics'].items():
                    self.config['performance_metrics'][key] = value
            
            for key, value in new_config.items():
                if key != 'performance_metrics':
                    self.config[key] = value
            
            self.data_handler.save_config(self.config)
            return {"success": True, "message": "✅ Konfigurasi berhasil diperbarui!"}
        except Exception as e:
            return {"success": False, "message": f"❌ Error: {str(e)}"}

    def calculate_finances(self, total_order: float, order_type: str = "Regular", custom_date: Optional[str] = None) -> FinancialRecord:
        """Calculate financial components"""
        commission = total_order * self.COMMISSION_RATE
        saldo_savings = total_order * self.SALDO_SAVINGS_RATE
        bbm_savings = total_order * self.BBM_SAVINGS_RATE
        oli_savings = total_order * self.OLI_SAVINGS_RATE

        net_income = total_order - commission
        usable_income = net_income - (saldo_savings + bbm_savings + oli_savings)

        return FinancialRecord(
            timestamp=datetime.now(),
            total_order=total_order,
            commission=commission,
            saldo_savings=saldo_savings,
            bbm_savings=bbm_savings,
            oli_savings=oli_savings,
            net_income=net_income,
            usable_income=usable_income,
            order_type=order_type,
            custom_date=custom_date
        )

    def add_order(self, total_order: float, order_type: str = "Regular", custom_date: Optional[str] = None) -> Dict[str, Any]:
        """Add new order dengan analytics real-time"""
        try:
            if total_order < 1000:
                return {"success": False, "message": "Total order minimal Rp 1,000"}

            if custom_date:
                try:
                    datetime.strptime(custom_date, '%Y-%m-%d')
                except ValueError:
                    return {"success": False, "message": "❌ Format tanggal tidak valid. Gunakan format YYYY-MM-DD"}

            record = self.calculate_finances(total_order, order_type, custom_date)
            
            # Save record
            self.data_handler.save_record([
                record.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                record.total_order,
                record.commission,
                record.saldo_savings,
                record.bbm_savings,
                record.oli_savings,
                record.net_income,
                record.usable_income,
                record.order_type,
                record.custom_date or ""
            ])
            
            analytics = self.get_real_time_analytics()
            insights = self.get_performance_insights()
            ai_analysis = self.ai_advisor.analyze_performance(analytics)
            
            return {
                "success": True, 
                "message": f"✅ Order {order_type} sebesar Rp {total_order:,.0f} berhasil ditambahkan!",
                "analytics": analytics,
                "insights": insights,
                "ai_analysis": ai_analysis,
                "record": record.to_dict()
            }
        except Exception as e:
            return {"success": False, "message": f"Error: {str(e)}"}

    def get_all_data(self) -> List[Dict[str, Any]]:
        """Get all transaction data"""
        return self.data_handler.load_all_data()

    def delete_orders(self, indices: List[int]) -> Dict[str, Any]:
        """Delete orders by indices"""
        try:
            success = self.data_handler.delete_records(indices)
            if not success:
                return {"success": False, "message": "Gagal menghapus data"}

            analytics = self.get_real_time_analytics()
            insights = self.get_performance_insights()
            ai_analysis = self.ai_advisor.analyze_performance(analytics)

            return {
                "success": True,
                "message": f"🗑️ Berhasil menghapus {len(indices)} data transaksi",
                "analytics": analytics,
                "insights": insights,
                "ai_analysis": ai_analysis
            }
        except Exception as e:
            return {"success": False, "message": f"Error: {str(e)}"}

    def get_real_time_analytics(self) -> Dict[str, Any]:
        """Get real-time analytics data"""
        try:
            data = self.get_all_data()
            if not data:
                return self.get_empty_analytics()

            # Basic summary
            total_orders = len(data)
            total_revenue = sum(item['total_order'] for item in data)
            total_net_income = sum(item['net_income'] for item in data)
            total_usable_income = sum(item['usable_income'] for item in data)

            # Time-based metrics
            today = datetime.now().date()
            today_str = today.isoformat()
            
            today_data = [item for item in data if item['display_date'] == today_str]
            
            weekly_data = []
            for item in data:
                try:
                    item_date = datetime.strptime(item['display_date'], '%Y-%m-%d').date()
                    if (today - item_date).days <= 7:
                        weekly_data.append(item)
                except ValueError:
                    continue

            # Performance metrics
            efficiency_ratio = (total_usable_income / total_revenue * 100) if total_revenue > 0 else 0
            performance_score = min(100, efficiency_ratio * 1.5)

            # Daily analytics
            daily_analytics = {}
            for item in data:
                date = item['display_date']
                if date not in daily_analytics:
                    daily_analytics[date] = {'revenue': 0, 'orders': 0, 'income': 0}
                daily_analytics[date]['revenue'] += item['total_order']
                daily_analytics[date]['orders'] += 1
                daily_analytics[date]['income'] += item['usable_income']

            # Order type analytics
            order_analytics = {}
            for item in data:
                order_type = item['order_type']
                if order_type not in order_analytics:
                    order_analytics[order_type] = {'count': 0, 'revenue': 0, 'avg_value': 0}
                order_analytics[order_type]['count'] += 1
                order_analytics[order_type]['revenue'] += item['total_order']

            for order_type in order_analytics:
                if order_analytics[order_type]['count'] > 0:
                    order_analytics[order_type]['avg_value'] = (
                        order_analytics[order_type]['revenue'] / order_analytics[order_type]['count']
                    )

            # Financial breakdown
            financial_breakdown = {
                "Komisi Maxim": sum(item['commission'] for item in data),
                "Tabungan Saldo": sum(item['saldo_savings'] for item in data),
                "Tabungan BBM": sum(item['bbm_savings'] for item in data),
                "Tabungan Oli": sum(item['oli_savings'] for item in data),
                "Pendapatan Bersih": total_net_income,
                "Pendapatan Siap Pakai": total_usable_income
            }

            # AI Analysis
            ai_analysis = self.ai_advisor.analyze_performance({
                "summary": {
                    "total_orders": total_orders,
                    "total_revenue": total_revenue,
                    "total_net_income": total_net_income,
                    "total_usable_income": total_usable_income,
                    "efficiency_ratio": efficiency_ratio,
                    "performance_score": performance_score
                },
                "time_metrics": {
                    "today_orders": len(today_data),
                    "today_revenue": sum(item['total_order'] for item in today_data),
                    "weekly_orders": len(weekly_data),
                    "weekly_revenue": sum(item['total_order'] for item in weekly_data)
                },
                "daily_analytics": daily_analytics,
                "order_analytics": order_analytics,
                "financial_breakdown": financial_breakdown
            })

            # Financial tips
            financial_tips = self.ai_advisor.generate_financial_tips({
                "summary": {
                    "total_orders": total_orders,
                    "efficiency_ratio": efficiency_ratio
                }
            })

            # Earnings prediction
            earnings_prediction = self.ai_advisor.predict_earnings({
                "daily_analytics": daily_analytics
            })

            # Chart data
            chart_data = self.generate_chart_data(data, daily_analytics)

            return {
                "summary": {
                    "total_orders": total_orders,
                    "total_revenue": total_revenue,
                    "total_net_income": total_net_income,
                    "total_usable_income": total_usable_income,
                    "avg_order_value": total_revenue / total_orders if total_orders > 0 else 0,
                    "efficiency_ratio": efficiency_ratio,
                    "performance_score": performance_score
                },
                "time_metrics": {
                    "today_orders": len(today_data),
                    "today_revenue": sum(item['total_order'] for item in today_data),
                    "weekly_orders": len(weekly_data),
                    "weekly_revenue": sum(item['total_order'] for item in weekly_data)
                },
                "daily_analytics": daily_analytics,
                "order_analytics": order_analytics,
                "financial_breakdown": financial_breakdown,
                "ai_analysis": ai_analysis,
                "financial_tips": financial_tips,
                "earnings_prediction": earnings_prediction,
                "chart_data": chart_data
            }
        except Exception as e:
            print(f"❌ Error in get_real_time_analytics: {e}")
            return self.get_empty_analytics()

    def generate_chart_data(self, data: List[Dict], daily_analytics: Dict) -> Dict[str, Any]:
        """Generate chart data untuk visualisasi"""
        if not data:
            return self.get_empty_chart_data()

        try:
            # Revenue trend - last 7 days
            dates = sorted(daily_analytics.keys())[-7:]
            revenue_trend = {
                "labels": dates,
                "data": [daily_analytics[date]['revenue'] for date in dates]
            }

            # Order types distribution
            order_types = {}
            for item in data:
                order_type = item['order_type']
                if order_type not in order_types:
                    order_types[order_type] = 0
                order_types[order_type] += 1

            order_types_chart = {
                "labels": list(order_types.keys()),
                "data": list(order_types.values())
            }

            # Income breakdown
            total_commission = sum(item['commission'] for item in data)
            total_savings = sum(item['saldo_savings'] + item['bbm_savings'] + item['oli_savings'] for item in data)
            total_net = sum(item['net_income'] for item in data)

            income_breakdown = {
                "labels": ["Komisi", "Tabungan", "Pendapatan Bersih"],
                "data": [total_commission, total_savings, total_net]
            }

            # Daily performance (last 5 days)
            recent_dates = sorted(daily_analytics.keys())[-5:]
            daily_performance = {
                "labels": recent_dates,
                "revenue": [daily_analytics[date]['revenue'] for date in recent_dates],
                "orders": [daily_analytics[date]['orders'] for date in recent_dates]
            }

            return {
                "revenue_trend": revenue_trend,
                "order_types": order_types_chart,
                "income_breakdown": income_breakdown,
                "daily_performance": daily_performance
            }
        except Exception as e:
            print(f"❌ Error generating chart data: {e}")
            return self.get_empty_chart_data()

    def get_empty_analytics(self) -> Dict[str, Any]:
        """Return empty analytics structure"""
        return {
            "summary": {
                "total_orders": 0,
                "total_revenue": 0,
                "total_net_income": 0,
                "total_usable_income": 0,
                "avg_order_value": 0,
                "efficiency_ratio": 0,
                "performance_score": 0
            },
            "time_metrics": {
                "today_orders": 0,
                "today_revenue": 0,
                "weekly_orders": 0,
                "weekly_revenue": 0
            },
            "daily_analytics": {},
            "order_analytics": {},
            "financial_breakdown": {
                "Komisi Maxim": 0,
                "Tabungan Saldo": 0,
                "Tabungan BBM": 0,
                "Tabungan Oli": 0,
                "Pendapatan Bersih": 0,
                "Pendapatan Siap Pakai": 0
            },
            "ai_analysis": [],
            "financial_tips": [],
            "earnings_prediction": {"prediction": 0, "confidence": "low", "daily_average": 0},
            "chart_data": self.get_empty_chart_data()
        }

    def get_empty_chart_data(self) -> Dict[str, Any]:
        """Return empty chart data structure"""
        return {
            "revenue_trend": {"labels": [], "data": []},
            "order_types": {"labels": [], "data": []},
            "income_breakdown": {"labels": [], "data": []},
            "daily_performance": {"labels": [], "revenue": [], "orders": []}
        }

    def get_performance_insights(self) -> List[Dict[str, Any]]:
        """Get expert performance insights"""
        try:
            analytics = self.get_real_time_analytics()
            return analytics.get('ai_analysis', [])
        except:
            return []
