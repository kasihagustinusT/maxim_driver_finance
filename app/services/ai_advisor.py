from datetime import datetime
from typing import Dict, List, Any

class AIFinanceAdvisor:
    """AI Financial Advisor dengan analisis cerdas"""
    
    @staticmethod
    def analyze_performance(analytics_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Analisis performa dengan AI"""
        summary = analytics_data['summary']
        time_metrics = analytics_data['time_metrics']
        
        insights = []
        
        efficiency = summary['efficiency_ratio']
        if efficiency > 75:
            insights.append({
                "type": "success",
                "icon": "🚀",
                "title": "Efisiensi Elite",
                "message": f"Efisiensi {efficiency:.1f}% - Performa luar biasa!",
                "priority": "high"
            })
        elif efficiency > 60:
            insights.append({
                "type": "success", 
                "icon": "⭐",
                "title": "Efisiensi Optimal",
                "message": f"Efisiensi {efficiency:.1f}% - Pertahankan!",
                "priority": "medium"
            })
        elif efficiency < 40:
            insights.append({
                "type": "warning",
                "icon": "⚡",
                "title": "Butuh Optimasi",
                "message": f"Efisiensi {efficiency:.1f}% - Perlu evaluasi strategi",
                "priority": "high"
            })
        
        daily_data = analytics_data['daily_analytics']
        if len(daily_data) >= 3:
            dates = sorted(daily_data.keys())[-3:]
            revenues = [daily_data[date]['revenue'] for date in dates]
            
            if len(revenues) >= 2:
                trend = revenues[-1] - revenues[-2]
                if trend > 0:
                    insights.append({
                        "type": "success",
                        "icon": "📈",
                        "title": "Trend Positif",
                        "message": f"Revenue naik {trend:,.0f} dari hari sebelumnya",
                        "priority": "medium"
                    })
                elif trend < 0:
                    insights.append({
                        "type": "warning",
                        "icon": "📉",
                        "title": "Trend Menurun",
                        "message": f"Revenue turun {abs(trend):,.0f} dari hari sebelumnya",
                        "priority": "high"
                    })
        
        order_analytics = analytics_data['order_analytics']
        if order_analytics:
            valid_order_types = {k: v for k, v in order_analytics.items() if v.get('count', 0) > 0}
            if valid_order_types:
                best_type = max(valid_order_types.items(), key=lambda x: x[1].get('avg_value', 0))
                worst_type = min(valid_order_types.items(), key=lambda x: x[1].get('avg_value', 0))
                
                if best_type[1].get('avg_value', 0) > worst_type[1].get('avg_value', 0) * 1.5:
                    insights.append({
                        "type": "info",
                        "icon": "🎯",
                        "title": "Fokus Optimal",
                        "message": f"{best_type[0]} menghasilkan {best_type[1]['avg_value']:,.0f}/order",
                        "priority": "medium"
                    })
        
        today_revenue = time_metrics['today_revenue']
        if today_revenue > 0:
            time_now = datetime.now().hour
            expected_revenue = (today_revenue / time_now) * 12 if time_now > 0 else 0
            
            if expected_revenue > today_revenue * 1.2:
                insights.append({
                    "type": "success",
                    "icon": "🎉",
                    "title": "Performa Cemerlang",
                    "message": f"Diperkirakan {expected_revenue:,.0f} hari ini",
                    "priority": "medium"
                })
        
        insights.sort(key=lambda x: {'high': 0, 'medium': 1, 'low': 2}[x['priority']])
        return insights[:5]

    @staticmethod
    def generate_financial_tips(analytics_data: Dict[str, Any]) -> List[str]:
        """Generate tips finansial berdasarkan data"""
        tips = []
        summary = analytics_data['summary']
        
        if summary['total_orders'] < 10:
            tips.append("💡 **Mulai Kecil**: Fokus pada konsistensi daripada quantity")
        elif summary['total_orders'] < 50:
            tips.append("💡 **Scale Up**: Pertimbangkan untuk meningkatkan volume order")
        else:
            tips.append("💡 **Expert Level**: Optimasi dengan premium orders")
        
        if summary['efficiency_ratio'] < 50:
            tips.append("💰 **Optimasi Biaya**: Review pengeluaran BBM dan maintenance")
        elif summary['efficiency_ratio'] > 70:
            tips.append("💰 **Strategi Solid**: Pertahankan model bisnis current")
        
        current_hour = datetime.now().hour
        if 7 <= current_hour <= 9:
            tips.append("⏰ **Morning Rush**: Fokus pada jam sibuk pagi")
        elif 16 <= current_hour <= 19:
            tips.append("⏰ **Evening Peak**: Manfaatkan jam pulang kerja")
        
        return tips

    @staticmethod
    def predict_earnings(analytics_data: Dict[str, Any], days: int = 7) -> Dict[str, Any]:
        """Prediksi earnings berdasarkan historical data"""
        daily_data = analytics_data['daily_analytics']
        if len(daily_data) < 3:
            return {"prediction": 0, "confidence": "low", "daily_average": 0}
        
        revenues = [daily_data[date]['revenue'] for date in sorted(daily_data.keys())[-7:]]
        avg_revenue = sum(revenues) / len(revenues)
        
        prediction = avg_revenue * days
        confidence = "high" if len(revenues) >= 5 else "medium"
        
        return {
            "prediction": prediction,
            "confidence": confidence,
            "daily_average": avg_revenue
        }
