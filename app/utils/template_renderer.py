from datetime import datetime
from typing import Dict, Any

from ..services.finance_manager import ExpertFinanceManager

class TemplateRenderer:
    def __init__(self, finance_manager: ExpertFinanceManager):
        self.finance_manager = finance_manager

    def create_base_template(self, title: str, active_page: str, content: str) -> str:
        """Create base template untuk semua halaman"""
        def get_nav_class(page: str) -> str:
            if page == active_page:
                return "nav-active text-white shadow-lg"
            else:
                return "text-gray-600 hover:text-purple-600 hover:bg-gray-100"
        
        dashboard_class = get_nav_class('dashboard')
        orders_class = get_nav_class('orders')
        history_class = get_nav_class('history')
        targets_class = get_nav_class('targets')

        return f'''
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Maxim Finance AI</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        .gradient-bg {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }}
        .glass-card {{
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.3);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        }}
        .hover-lift:hover {{
            transform: translateY(-5px);
            transition: all 0.3s ease;
            box-shadow: 0 12px 40px rgba(0, 0, 0, 0.15);
        }}
        .chart-container {{
            position: relative;
            height: 300px;
            width: 100%;
        }}
        .nav-active {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-radius: 12px;
        }}
        .date-badge {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 2px 8px;
            border-radius: 12px;
            font-size: 0.75rem;
            font-weight: 600;
        }}
        @media (max-width: 768px) {{
            .mobile-stack {{
                flex-direction: column;
            }}
            .mobile-full {{
                width: 100%;
            }}
            .mobile-padding {{
                padding: 1rem;
            }}
            .mobile-text-center {{
                text-align: center;
            }}
        }}
    </style>
</head>
<body class="gradient-bg">
    <!-- Navigation -->
    <nav class="bg-white bg-opacity-90 backdrop-blur-lg shadow-lg sticky top-0 z-40">
        <div class="container mx-auto px-4">
            <div class="flex flex-col md:flex-row justify-between items-center py-4 space-y-4 md:space-y-0">
                <div class="flex items-center space-x-3">
                    <div class="w-10 h-10 bg-gradient-to-r from-purple-600 to-blue-600 rounded-full flex items-center justify-center">
                        <i class="fas fa-brain text-white text-lg"></i>
                    </div>
                    <h1 class="text-xl md:text-2xl font-bold text-gray-800">
                        Maxim Finance AI
                    </h1>
                </div>
                <div class="flex flex-wrap justify-center gap-2">
                    <a href="/dashboard" class="px-3 md:px-4 py-2 rounded-lg transition-all duration-300 {dashboard_class} mobile-text-center">
                        <i class="fas fa-tachometer-alt mr-2"></i>Dashboard
                    </a>
                    <a href="/orders" class="px-3 md:px-4 py-2 rounded-lg transition-all duration-300 {orders_class} mobile-text-center">
                        <i class="fas fa-plus-circle mr-2"></i>Add Order
                    </a>
                    <a href="/history" class="px-3 md:px-4 py-2 rounded-lg transition-all duration-300 {history_class} mobile-text-center">
                        <i class="fas fa-history mr-2"></i>History
                    </a>
                    <a href="/targets" class="px-3 md:px-4 py-2 rounded-lg transition-all duration-300 {targets_class} mobile-text-center">
                        <i class="fas fa-bullseye mr-2"></i>Targets
                    </a>
                </div>
            </div>
        </div>
    </nav>

    <!-- Alert Container -->
    <div id="alertContainer" class="fixed top-20 right-4 z-50 max-w-sm w-full md:w-auto mobile-padding"></div>

    <!-- Page Content -->
    <div class="container mx-auto px-4 py-6 md:py-8">
        {content}
    </div>

    <!-- Footer -->
    <footer class="bg-white bg-opacity-90 mt-12">
        <div class="container mx-auto px-4 py-6 text-center text-gray-600">
            <p class="text-sm md:text-base">Maxim Finance AI System • Powered by Artificial Intelligence • Professional Grade • Kasih</p>
        </div>
    </footer>

    <script>
        // Global utility functions
        function showAlert(message, type = 'success') {{
            const alertContainer = document.getElementById('alertContainer');
            const alert = document.createElement('div');
            
            let alertClass = 'bg-blue-100 border border-blue-400 text-blue-700';
            let icon = 'info-circle';
            
            if (type === 'success') {{
                alertClass = 'bg-green-100 border border-green-400 text-green-700';
                icon = 'check-circle';
            }} else if (type === 'error') {{
                alertClass = 'bg-red-100 border border-red-400 text-red-700';
                icon = 'exclamation-triangle';
            }}
            
            alert.className = `p-4 rounded-xl shadow-lg mb-4 transform transition-all duration-500 ease-in-out ${{alertClass}}`;
            alert.innerHTML = `
                <div class="flex items-center">
                    <i class="fas fa-${{icon}} mr-3"></i>
                    <div class="flex-1">
                        <p class="font-medium">${{message}}</p>
                    </div>
                    <button onclick="this.parentElement.parentElement.remove()" class="ml-4">
                        <i class="fas fa-times"></i>
                    </button>
                </div>
            `;
            alertContainer.appendChild(alert);
            
            setTimeout(() => {{
                if (alert.parentElement) {{
                    alert.style.opacity = '0';
                    alert.style.transform = 'translateX(100%)';
                    setTimeout(() => alert.remove(), 500);
                }}
            }}, 5000);
        }}

        // Format currency
        function formatCurrency(amount) {{
            return 'Rp ' + Math.round(amount).toLocaleString('id-ID');
        }}

        // Format percentage
        function formatPercentage(value) {{
            return value.toFixed(1) + '%';
        }}

        // Get today's date in YYYY-MM-DD format
        function getTodayDate() {{
            const now = new Date();
            return now.toISOString().split('T')[0];
        }}
    </script>
</body>
</html>
        '''



    def create_dashboard_page(self):
        """Create dashboard page dengan analytics real-time dan visualisasi"""
        return self.create_base_template(
            "AI Finance Dashboard",
            "dashboard",
            '''
            <div class="space-y-6 md:space-y-8">
                <!-- Header Stats -->
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 md:gap-6">
                    <!-- Total Revenue Card -->
                    <div class="glass-card rounded-2xl p-6 hover-lift">
                        <div class="flex items-center justify-between">
                            <div>
                                <p class="text-gray-600 text-sm font-medium">Total Revenue</p>
                                <h3 id="totalRevenue" class="text-2xl md:text-3xl font-bold text-gray-800 mt-2">Loading...</h3>
                            </div>
                            <div class="w-12 h-12 bg-gradient-to-r from-green-400 to-green-600 rounded-xl flex items-center justify-center">
                                <i class="fas fa-wallet text-white text-xl"></i>
                            </div>
                        </div>
                        <div class="mt-4 flex items-center text-sm">
                            <span class="text-green-600 font-medium" id="revenueTrend">+0%</span>
                            <span class="text-gray-500 ml-2">vs kemarin</span>
                        </div>
                    </div>

                    <!-- Usable Income Card -->
                    <div class="glass-card rounded-2xl p-6 hover-lift">
                        <div class="flex items-center justify-between">
                            <div>
                                <p class="text-gray-600 text-sm font-medium">Pendapatan Siap Pakai</p>
                                <h3 id="usableIncome" class="text-2xl md:text-3xl font-bold text-gray-800 mt-2">Loading...</h3>
                            </div>
                            <div class="w-12 h-12 bg-gradient-to-r from-blue-400 to-blue-600 rounded-xl flex items-center justify-center">
                                <i class="fas fa-money-bill-wave text-white text-xl"></i>
                            </div>
                        </div>
                        <div class="mt-4">
                            <div class="w-full bg-gray-200 rounded-full h-2">
                                <div id="incomeProgress" class="bg-blue-600 h-2 rounded-full" style="width: 0%"></div>
                            </div>
                        </div>
                    </div>

                    <!-- Total Orders Card -->
                    <div class="glass-card rounded-2xl p-6 hover-lift">
                        <div class="flex items-center justify-between">
                            <div>
                                <p class="text-gray-600 text-sm font-medium">Total Orders</p>
                                <h3 id="totalOrders" class="text-2xl md:text-3xl font-bold text-gray-800 mt-2">Loading...</h3>
                            </div>
                            <div class="w-12 h-12 bg-gradient-to-r from-purple-400 to-purple-600 rounded-xl flex items-center justify-center">
                                <i class="fas fa-chart-line text-white text-xl"></i>
                            </div>
                        </div>
                        <div class="mt-4">
                            <p class="text-gray-600 text-sm" id="orderStats">Hari ini: 0 orders</p>
                        </div>
                    </div>

                    <!-- Efficiency Score Card -->
                    <div class="glass-card rounded-2xl p-6 hover-lift">
                        <div class="flex items-center justify-between">
                            <div>
                                <p class="text-gray-600 text-sm font-medium">Efficiency Score</p>
                                <h3 id="efficiencyScore" class="text-2xl md:text-3xl font-bold text-gray-800 mt-2">Loading...</h3>
                            </div>
                            <div class="w-12 h-12 bg-gradient-to-r from-orange-400 to-orange-600 rounded-xl flex items-center justify-center">
                                <i class="fas fa-bolt text-white text-xl"></i>
                            </div>
                        </div>
                        <div class="mt-4">
                            <div class="w-full bg-gray-200 rounded-full h-2">
                                <div id="efficiencyProgress" class="bg-orange-600 h-2 rounded-full" style="width: 0%"></div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Visualisasi Data Section -->
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 md:gap-8">
                    <!-- Revenue Trend Chart -->
                    <div class="glass-card rounded-2xl p-6">
                        <h2 class="text-xl font-bold text-gray-800 mb-6">Trend Revenue 7 Hari Terakhir</h2>
                        <div class="chart-container">
                            <canvas id="revenueChart"></canvas>
                        </div>
                    </div>

                    <!-- Order Types Distribution -->
                    <div class="glass-card rounded-2xl p-6">
                        <h2 class="text-xl font-bold text-gray-800 mb-6">Distribusi Jenis Order</h2>
                        <div class="chart-container">
                            <canvas id="orderTypesChart"></canvas>
                        </div>
                    </div>

                    <!-- Income Breakdown -->
                    <div class="glass-card rounded-2xl p-6">
                        <h2 class="text-xl font-bold text-gray-800 mb-6">Breakdown Pendapatan</h2>
                        <div class="chart-container">
                            <canvas id="incomeBreakdownChart"></canvas>
                        </div>
                    </div>

                    <!-- Daily Performance -->
                    <div class="glass-card rounded-2xl p-6">
                        <h2 class="text-xl font-bold text-gray-800 mb-6">Performa Harian</h2>
                        <div class="chart-container">
                            <canvas id="dailyPerformanceChart"></canvas>
                        </div>
                    </div>
                </div>

                <!-- AI Insights Section -->
                <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 md:gap-8">
                    <!-- Main Analytics -->
                    <div class="lg:col-span-2 space-y-6 md:space-y-8">
                        <!-- Financial Breakdown -->
                        <div class="glass-card rounded-2xl p-6">
                            <h2 class="text-xl font-bold text-gray-800 mb-6">Financial Breakdown</h2>
                            <div class="grid grid-cols-2 md:grid-cols-3 gap-4" id="financialBreakdown">
                                <!-- Will be populated by JavaScript -->
                            </div>
                        </div>
                    </div>

                    <!-- AI Insights Sidebar -->
                    <div class="space-y-6 md:space-y-8">
                        <!-- AI Analysis -->
                        <div class="glass-card rounded-2xl p-6">
                            <h2 class="text-xl font-bold text-gray-800 mb-4 flex items-center">
                                <i class="fas fa-robot text-purple-600 mr-2"></i>
                                AI Analysis
                            </h2>
                            <div id="aiInsights" class="space-y-4">
                                <!-- Will be populated by JavaScript -->
                            </div>
                        </div>

                        <!-- Financial Tips -->
                        <div class="glass-card rounded-2xl p-6">
                            <h2 class="text-xl font-bold text-gray-800 mb-4 flex items-center">
                                <i class="fas fa-lightbulb text-yellow-500 mr-2"></i>
                                Financial Tips
                            </h2>
                            <div id="financialTips" class="space-y-3">
                                <!-- Will be populated by JavaScript -->
                            </div>
                        </div>

                        <!-- Earnings Prediction -->
                        <div class="glass-card rounded-2xl p-6">
                            <h2 class="text-xl font-bold text-gray-800 mb-4 flex items-center">
                                <i class="fas fa-crystal-ball text-green-500 mr-2"></i>
                                7-Day Prediction
                            </h2>
                            <div id="earningsPrediction">
                                <!-- Will be populated by JavaScript -->
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <script>
                // Load dashboard data
                async function loadDashboardData() {
                    try {
                        const response = await fetch('/api/analytics');
                        const data = await response.json();
                        
                        if (data.success) {
                            updateDashboard(data.analytics);
                            updateCharts(data.analytics.chart_data);
                        }
                    } catch (error) {
                        console.error('Error loading dashboard:', error);
                        showAlert('Gagal memuat data dashboard', 'error');
                    }
                }

                function updateDashboard(analytics) {
                    // Update header stats
                    document.getElementById('totalRevenue').textContent = formatCurrency(analytics.summary.total_revenue);
                    document.getElementById('usableIncome').textContent = formatCurrency(analytics.summary.total_usable_income);
                    document.getElementById('totalOrders').textContent = analytics.summary.total_orders.toLocaleString();
                    document.getElementById('efficiencyScore').textContent = formatPercentage(analytics.summary.efficiency_ratio);
                    
                    // Update progress bars
                    document.getElementById('incomeProgress').style.width = Math.min(100, (analytics.summary.total_usable_income / 10000000) * 100) + '%';
                    document.getElementById('efficiencyProgress').style.width = analytics.summary.efficiency_ratio + '%';
                    
                    // Update order stats
                    document.getElementById('orderStats').textContent = `Hari ini: ${analytics.time_metrics.today_orders} orders`;
                    
                    // Update AI Insights
                    updateAIInsights(analytics.ai_analysis);
                    
                    // Update Financial Tips
                    updateFinancialTips(analytics.financial_tips);
                    
                    // Update Financial Breakdown
                    updateFinancialBreakdown(analytics.financial_breakdown);
                    
                    // Update Earnings Prediction
                    updateEarningsPrediction(analytics.earnings_prediction);
                }

                function updateCharts(chartData) {
                    // Revenue Trend Chart
                    const revenueCtx = document.getElementById('revenueChart').getContext('2d');
                    new Chart(revenueCtx, {
                        type: 'line',
                        data: {
                            labels: chartData.revenue_trend.labels,
                            datasets: [{
                                label: 'Revenue',
                                data: chartData.revenue_trend.data,
                                borderColor: '#667eea',
                                backgroundColor: 'rgba(102, 126, 234, 0.1)',
                                borderWidth: 3,
                                fill: true,
                                tension: 0.4
                            }]
                        },
                        options: {
                            responsive: true,
                            maintainAspectRatio: false,
                            plugins: {
                                legend: {
                                    display: false
                                },
                                tooltip: {
                                    callbacks: {
                                        label: function(context) {
                                            return 'Revenue: ' + formatCurrency(context.raw);
                                        }
                                    }
                                }
                            },
                            scales: {
                                y: {
                                    beginAtZero: true,
                                    ticks: {
                                        callback: function(value) {
                                            return 'Rp ' + (value / 1000).toFixed(0) + 'K';
                                        }
                                    }
                                }
                            }
                        }
                    });

                    // Order Types Chart
                    const orderTypesCtx = document.getElementById('orderTypesChart').getContext('2d');
                    new Chart(orderTypesCtx, {
                        type: 'doughnut',
                        data: {
                            labels: chartData.order_types.labels,
                            datasets: [{
                                data: chartData.order_types.data,
                                backgroundColor: [
                                    '#667eea', '#764ba2', '#f093fb', '#f5576c', '#4facfe'
                                ],
                                borderWidth: 2,
                                borderColor: '#fff'
                            }]
                        },
                        options: {
                            responsive: true,
                            maintainAspectRatio: false,
                            plugins: {
                                legend: {
                                    position: 'bottom'
                                }
                            }
                        }
                    });

                    // Income Breakdown Chart
                    const incomeCtx = document.getElementById('incomeBreakdownChart').getContext('2d');
                    new Chart(incomeCtx, {
                        type: 'bar',
                        data: {
                            labels: chartData.income_breakdown.labels,
                            datasets: [{
                                label: 'Amount',
                                data: chartData.income_breakdown.data,
                                backgroundColor: [
                                    'rgba(239, 68, 68, 0.8)',
                                    'rgba(59, 130, 246, 0.8)',
                                    'rgba(16, 185, 129, 0.8)'
                                ],
                                borderWidth: 0
                            }]
                        },
                        options: {
                            responsive: true,
                            maintainAspectRatio: false,
                            plugins: {
                                legend: {
                                    display: false
                                },
                                tooltip: {
                                    callbacks: {
                                        label: function(context) {
                                            return formatCurrency(context.raw);
                                        }
                                    }
                                }
                            },
                            scales: {
                                y: {
                                    beginAtZero: true,
                                    ticks: {
                                        callback: function(value) {
                                            return 'Rp ' + (value / 1000).toFixed(0) + 'K';
                                        }
                                    }
                                }
                            }
                        }
                    });

                    // Daily Performance Chart
                    const dailyCtx = document.getElementById('dailyPerformanceChart').getContext('2d');
                    new Chart(dailyCtx, {
                        type: 'bar',
                        data: {
                            labels: chartData.daily_performance.labels,
                            datasets: [
                                {
                                    label: 'Revenue',
                                    data: chartData.daily_performance.revenue,
                                    backgroundColor: 'rgba(102, 126, 234, 0.8)',
                                    yAxisID: 'y'
                                },
                                {
                                    label: 'Orders',
                                    data: chartData.daily_performance.orders,
                                    backgroundColor: 'rgba(118, 75, 162, 0.8)',
                                    type: 'line',
                                    yAxisID: 'y1'
                                }
                            ]
                        },
                        options: {
                            responsive: true,
                            maintainAspectRatio: false,
                            scales: {
                                y: {
                                    type: 'linear',
                                    display: true,
                                    position: 'left',
                                    title: {
                                        display: true,
                                        text: 'Revenue'
                                    },
                                    ticks: {
                                        callback: function(value) {
                                            return 'Rp ' + (value / 1000).toFixed(0) + 'K';
                                        }
                                    }
                                },
                                y1: {
                                    type: 'linear',
                                    display: true,
                                    position: 'right',
                                    title: {
                                        display: true,
                                        text: 'Orders'
                                    },
                                    grid: {
                                        drawOnChartArea: false
                                    }
                                }
                            }
                        }
                    });
                }

                function updateAIInsights(insights) {
                    const container = document.getElementById('aiInsights');
                    if (insights.length === 0) {
                        container.innerHTML = '<p class="text-gray-500 text-center py-4">Tidak ada insights tersedia</p>';
                        return;
                    }

                    container.innerHTML = insights.map(insight => `
                        <div class="p-4 rounded-xl border-l-4 ${
                            insight.type === 'success' ? 'border-green-500 bg-green-50' :
                            insight.type === 'warning' ? 'border-yellow-500 bg-yellow-50' :
                            'border-blue-500 bg-blue-50'
                        }">
                            <div class="flex items-start">
                                <span class="text-lg mr-3">${insight.icon}</span>
                                <div>
                                    <h4 class="font-semibold text-gray-800">${insight.title}</h4>
                                    <p class="text-sm text-gray-600 mt-1">${insight.message}</p>
                                </div>
                            </div>
                        </div>
                    `).join('');
                }

                function updateFinancialTips(tips) {
                    const container = document.getElementById('financialTips');
                    if (tips.length === 0) {
                        container.innerHTML = '<p class="text-gray-500 text-center py-4">Tidak ada tips tersedia</p>';
                        return;
                    }

                    container.innerHTML = tips.map(tip => `
                        <div class="flex items-start p-3 bg-yellow-50 rounded-lg">
                            <i class="fas fa-lightbulb text-yellow-500 mt-1 mr-3"></i>
                            <p class="text-sm text-gray-700">${tip}</p>
                        </div>
                    `).join('');
                }

                function updateFinancialBreakdown(breakdown) {
                    const container = document.getElementById('financialBreakdown');
                    const items = [
                        { key: 'Komisi Maxim', icon: 'percentage', color: 'red' },
                        { key: 'Tabungan Saldo', icon: 'piggy-bank', color: 'blue' },
                        { key: 'Tabungan BBM', icon: 'gas-pump', color: 'green' },
                        { key: 'Tabungan Oli', icon: 'oil-can', color: 'purple' },
                        { key: 'Pendapatan Bersih', icon: 'chart-line', color: 'indigo' },
                        { key: 'Pendapatan Siap Pakai', icon: 'wallet', color: 'teal' }
                    ];

                    container.innerHTML = items.map(item => `
                        <div class="text-center p-4 bg-gray-50 rounded-xl">
                            <div class="w-10 h-10 mx-auto mb-2 rounded-full bg-${item.color}-100 flex items-center justify-center">
                                <i class="fas fa-${item.icon} text-${item.color}-600"></i>
                            </div>
                            <p class="text-xs text-gray-600 mb-1">${item.key}</p>
                            <p class="text-sm font-semibold text-gray-800">${formatCurrency(breakdown[item.key])}</p>
                        </div>
                    `).join('');
                }

                function updateEarningsPrediction(prediction) {
                    const container = document.getElementById('earningsPrediction');
                    const confidenceColors = {
                        low: 'red',
                        medium: 'yellow', 
                        high: 'green'
                    };

                    container.innerHTML = `
                        <div class="text-center">
                            <p class="text-2xl font-bold text-gray-800 mb-2">${formatCurrency(prediction.prediction)}</p>
                            <div class="flex items-center justify-center mb-3">
                                <span class="px-2 py-1 bg-${confidenceColors[prediction.confidence]}-100 text-${confidenceColors[prediction.confidence]}-600 rounded-full text-xs font-medium">
                                    ${prediction.confidence.toUpperCase()} CONFIDENCE
                                </span>
                            </div>
                            <p class="text-sm text-gray-600">Rata-rata: ${formatCurrency(prediction.daily_average)}/hari</p>
                        </div>
                    `;
                }

                // Load dashboard on page load
                document.addEventListener('DOMContentLoaded', loadDashboardData);
                // Refresh every 30 seconds
                setInterval(loadDashboardData, 30000);
            </script>
            '''
        )

    def create_orders_page(self):
        """Create orders management page"""
        return self.create_base_template(
            "Add New Order", 
            "orders",
            '''
            <div class="max-w-4xl mx-auto">
                <div class="glass-card rounded-2xl p-6 md:p-8">
                    <div class="text-center mb-8">
                        <h1 class="text-2xl md:text-3xl font-bold text-gray-800 mb-2">Tambah Order Baru</h1>
                        <p class="text-gray-600">Masukkan detail order untuk analisis finansial otomatis</p>
                    </div>

                    <form id="orderForm" class="space-y-6">
                        <!-- Order Amount -->
                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-2">
                                <i class="fas fa-money-bill-wave mr-2"></i>Total Orderan
                            </label>
                            <div class="relative">
                                <span class="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-500">Rp</span>
                                <input 
                                    type="number" 
                                    id="totalOrder" 
                                    required
                                    min="1000"
                                    step="1000"
                                    class="w-full pl-10 pr-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-purple-500 focus:border-transparent transition-all duration-300"
                                    placeholder="Masukkan total orderan"
                                >
                            </div>
                            <p class="text-xs text-gray-500 mt-1">Minimal Rp 1,000</p>
                        </div>

                        <!-- Order Type -->
                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-2">
                                <i class="fas fa-tags mr-2"></i>Jenis Orderan
                            </label>
                            <select 
                                id="orderType"
                                class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-purple-500 focus:border-transparent transition-all duration-300"
                            >
                                <option value="Regular">Regular</option>
                                <option value="Premium">Premium</option>
                                <option value="Express">Express</option>
                                <option value="Corporate">Corporate</option>
                                <option value="Special">Special</option>
                            </select>
                        </div>

                        <!-- Custom Date Selection -->
                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-2">
                                <i class="fas fa-calendar-alt mr-2"></i>Tanggal Custom (Opsional)
                            </label>
                            <input 
                                type="date" 
                                id="customDate"
                                max="''' + datetime.now().strftime('%Y-%m-%d') + '''"
                                class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-purple-500 focus:border-transparent transition-all duration-300"
                            >
                            <p class="text-xs text-gray-500 mt-1">Kosongkan untuk menggunakan tanggal hari ini</p>
                        </div>

                        <!-- Preview Section -->
                        <div id="previewSection" class="hidden glass-card rounded-xl p-6 border-2 border-dashed border-gray-300">
                            <h3 class="font-semibold text-gray-800 mb-4">Preview Perhitungan</h3>
                            <div class="grid grid-cols-2 gap-4 text-sm" id="previewCalculations">
                                <!-- Preview calculations will appear here -->
                            </div>
                        </div>

                        <!-- Action Buttons -->
                        <div class="flex flex-col md:flex-row gap-4 pt-6">
                            <button 
                                type="button"
                                onclick="calculatePreview()"
                                class="flex-1 px-6 py-3 bg-gray-600 text-white rounded-xl hover:bg-gray-700 transition-all duration-300 flex items-center justify-center"
                            >
                                <i class="fas fa-calculator mr-2"></i>Preview
                            </button>
                            <button 
                                type="submit"
                                class="flex-1 px-6 py-3 bg-gradient-to-r from-purple-600 to-blue-600 text-white rounded-xl hover:from-purple-700 hover:to-blue-700 transition-all duration-300 flex items-center justify-center"
                            >
                                <i class="fas fa-plus-circle mr-2"></i>Tambah Order
                            </button>
                        </div>
                    </form>

                    <!-- Quick Actions -->
                    <div class="mt-8 pt-6 border-t border-gray-200">
                        <h3 class="font-semibold text-gray-800 mb-4">Quick Actions</h3>
                        <div class="grid grid-cols-2 md:grid-cols-4 gap-3">
                            <button onclick="setQuickAmount(50000)" class="p-3 bg-blue-50 text-blue-600 rounded-lg hover:bg-blue-100 transition-colors">
                                Rp 50K
                            </button>
                            <button onclick="setQuickAmount(100000)" class="p-3 bg-green-50 text-green-600 rounded-lg hover:bg-green-100 transition-colors">
                                Rp 100K
                            </button>
                            <button onclick="setQuickAmount(200000)" class="p-3 bg-purple-50 text-purple-600 rounded-lg hover:bg-purple-100 transition-colors">
                                Rp 200K
                            </button>
                            <button onclick="setQuickAmount(500000)" class="p-3 bg-orange-50 text-orange-600 rounded-lg hover:bg-orange-100 transition-colors">
                                Rp 500K
                            </button>
                        </div>
                    </div>
                </div>
            </div>

            <script>
                function setQuickAmount(amount) {
                    document.getElementById('totalOrder').value = amount;
                    calculatePreview();
                }

                function calculatePreview() {
                    const totalOrder = parseFloat(document.getElementById('totalOrder').value);
                    
                    if (!totalOrder || totalOrder < 1000) {
                        document.getElementById('previewSection').classList.add('hidden');
                        return;
                    }

                    const commission = totalOrder * 0.15;
                    const saldoSavings = totalOrder * 0.10;
                    const bbmSavings = totalOrder * 0.10;
                    const oliSavings = totalOrder * 0.10;
                    const netIncome = totalOrder - commission;
                    const usableIncome = netIncome - (saldoSavings + bbmSavings + oliSavings);

                    document.getElementById('previewCalculations').innerHTML = `
                        <div class="text-gray-600">Total Order</div>
                        <div class="font-semibold">${formatCurrency(totalOrder)}</div>
                        
                        <div class="text-gray-600">Komisi (15%)</div>
                        <div class="text-red-600 font-semibold">-${formatCurrency(commission)}</div>
                        
                        <div class="text-gray-600">Tabungan Saldo (10%)</div>
                        <div class="text-blue-600 font-semibold">-${formatCurrency(saldoSavings)}</div>
                        
                        <div class="text-gray-600">Tabungan BBM (10%)</div>
                        <div class="text-green-600 font-semibold">-${formatCurrency(bbmSavings)}</div>
                        
                        <div class="text-gray-600">Tabungan Oli (10%)</div>
                        <div class="text-purple-600 font-semibold">-${formatCurrency(oliSavings)}</div>
                        
                        <div class="text-gray-600 font-medium border-t pt-2">Pendapatan Bersih</div>
                        <div class="font-bold text-gray-800 border-t pt-2">${formatCurrency(netIncome)}</div>
                        
                        <div class="text-gray-600 font-medium">Pendapatan Siap Pakai</div>
                        <div class="font-bold text-green-600">${formatCurrency(usableIncome)}</div>
                    `;

                    document.getElementById('previewSection').classList.remove('hidden');
                }

                // Form submission
                document.getElementById('orderForm').addEventListener('submit', async function(e) {
                    e.preventDefault();
                    
                    const totalOrder = parseFloat(document.getElementById('totalOrder').value);
                    const orderType = document.getElementById('orderType').value;
                    const customDate = document.getElementById('customDate').value || null;

                    if (!totalOrder || totalOrder < 1000) {
                        showAlert('Total order minimal Rp 1,000', 'error');
                        return;
                    }

                    try {
                        const response = await fetch('/api/add-order', {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json',
                            },
                            body: JSON.stringify({
                                total_order: totalOrder,
                                order_type: orderType,
                                custom_date: customDate
                            })
                        });

                        const result = await response.json();

                        if (result.success) {
                            showAlert(result.message, 'success');
                            document.getElementById('orderForm').reset();
                            document.getElementById('previewSection').classList.add('hidden');
                            
                            // Update analytics if available
                            if (result.analytics) {
                                // You can update any real-time components here
                            }
                        } else {
                            showAlert(result.message, 'error');
                        }
                    } catch (error) {
                        console.error('Error adding order:', error);
                        showAlert('Gagal menambah order', 'error');
                    }
                });

                // Real-time preview on input change
                document.getElementById('totalOrder').addEventListener('input', calculatePreview);
            </script>
            '''
        )

    def create_history_page(self):
        """Create transaction history page dengan perbaikan delete functionality"""
        return self.create_base_template(
            "Transaction History",
            "history", 
            '''
            <div class="space-y-6">
                <!-- Header -->
                <div class="flex flex-col md:flex-row md:items-center justify-between">
                    <div>
                        <h1 class="text-2xl md:text-3xl font-bold text-gray-800">Riwayat Transaksi</h1>
                        <p class="text-gray-600 mt-2">Kelola dan pantau semua orderan Anda</p>
                    </div>
                    <div class="mt-4 md:mt-0 flex space-x-3">
                        <button onclick="exportToCSV()" class="px-4 py-2 bg-green-500 text-white rounded-xl hover:bg-green-600 transition-colors flex items-center">
                            <i class="fas fa-file-export mr-2"></i>Export CSV
                        </button>
                        <button onclick="refreshData()" class="px-4 py-2 bg-blue-500 text-white rounded-xl hover:bg-blue-600 transition-colors flex items-center">
                            <i class="fas fa-sync-alt mr-2"></i>Refresh
                        </button>
                    </div>
                </div>

                <!-- Statistics Bar -->
                <div id="historyStats" class="glass-card rounded-2xl p-6">
                    <div class="grid grid-cols-2 md:grid-cols-4 gap-4 text-center">
                        <div>
                            <p class="text-sm text-gray-600">Total Transaksi</p>
                            <p id="totalTransactions" class="text-xl font-bold text-gray-800">0</p>
                        </div>
                        <div>
                            <p class="text-sm text-gray-600">Total Revenue</p>
                            <p id="totalRevenue" class="text-xl font-bold text-green-600">Rp 0</p>
                        </div>
                        <div>
                            <p class="text-sm text-gray-600">Pendapatan Bersih</p>
                            <p id="totalNetIncome" class="text-xl font-bold text-blue-600">Rp 0</p>
                        </div>
                        <div>
                            <p class="text-sm text-gray-600">Rata-rata/Order</p>
                            <p id="avgOrderValue" class="text-xl font-bold text-purple-600">Rp 0</p>
                        </div>
                    </div>
                </div>

                <!-- Filters -->
                <div class="glass-card rounded-2xl p-6">
                    <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-2">Tanggal Mulai</label>
                            <input type="date" id="startDate" class="w-full px-3 py-2 border border-gray-300 rounded-lg">
                        </div>
                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-2">Tanggal Akhir</label>
                            <input type="date" id="endDate" class="w-full px-3 py-2 border border-gray-300 rounded-lg">
                        </div>
                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-2">Jenis Order</label>
                            <select id="orderTypeFilter" class="w-full px-3 py-2 border border-gray-300 rounded-lg">
                                <option value="">Semua Jenis</option>
                                <option value="Regular">Regular</option>
                                <option value="Premium">Premium</option>
                                <option value="Express">Express</option>
                                <option value="Corporate">Corporate</option>
                                <option value="Special">Special</option>
                            </select>
                        </div>
                        <div class="flex items-end">
                            <button onclick="applyFilters()" class="w-full px-4 py-2 bg-purple-600 text-white rounded-lg hover:bg-purple-700 transition-colors">
                                Terapkan Filter
                            </button>
                        </div>
                    </div>
                </div>

                <!-- Transactions Table -->
                <div class="glass-card rounded-2xl p-6">
                    <div class="overflow-x-auto">
                        <table class="w-full">
                            <thead>
                                <tr class="border-b-2 border-gray-200">
                                    <th class="pb-4 text-left">
                                        <input type="checkbox" id="selectAll" onchange="toggleSelectAll()">
                                    </th>
                                    <th class="pb-4 text-left text-sm font-semibold text-gray-600">Tanggal</th>
                                    <th class="pb-4 text-left text-sm font-semibold text-gray-600">Jenis</th>
                                    <th class="pb-4 text-left text-sm font-semibold text-gray-600">Total Order</th>
                                    <th class="pb-4 text-left text-sm font-semibold text-gray-600">Komisi</th>
                                    <th class="pb-4 text-left text-sm font-semibold text-gray-600">Pendapatan Bersih</th>
                                    <th class="pb-4 text-left text-sm font-semibold text-gray-600">Siap Pakai</th>
                                </tr>
                            </thead>
                            <tbody id="transactionsTable">
                                <!-- Data will be populated by JavaScript -->
                            </tbody>
                        </table>
                    </div>

                    <!-- Empty State -->
                    <div id="emptyState" class="text-center py-12 hidden">
                        <i class="fas fa-receipt text-4xl text-gray-300 mb-4"></i>
                        <h3 class="text-lg font-semibold text-gray-500">Belum ada transaksi</h3>
                        <p class="text-gray-400 mt-2">Mulai dengan menambahkan order pertama Anda</p>
                    </div>

                    <!-- Loading State -->
                    <div id="loadingState" class="text-center py-8">
                        <i class="fas fa-spinner fa-spin text-2xl text-purple-600 mb-4"></i>
                        <p class="text-gray-600">Memuat data transaksi...</p>
                    </div>

                    <!-- Action Bar -->
                    <div id="actionBar" class="mt-6 pt-6 border-t border-gray-200 hidden">
                        <div class="flex flex-col md:flex-row md:items-center justify-between">
                            <div class="mb-4 md:mb-0">
                                <span id="selectedCount" class="text-sm text-gray-600">0 item terpilih</span>
                            </div>
                            <div class="flex space-x-3">
                                <button onclick="deleteSelected()" class="px-4 py-2 bg-red-500 text-white rounded-lg hover:bg-red-600 transition-colors flex items-center">
                                    <i class="fas fa-trash mr-2"></i>Hapus Terpilih
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <script>
                let allTransactions = [];
                let selectedTransactions = new Set();

                async function loadTransactionData() {
                    try {
                        document.getElementById('loadingState').classList.remove('hidden');
                        document.getElementById('emptyState').classList.add('hidden');
                        
                        const response = await fetch('/api/data');
                        const data = await response.json();
                        
                        if (data.success) {
                            allTransactions = data.transactions;
                            updateTransactionTable(allTransactions);
                            updateStatistics(data.analytics);
                        }
                    } catch (error) {
                        console.error('Error loading transactions:', error);
                        showAlert('Gagal memuat data transaksi', 'error');
                    } finally {
                        document.getElementById('loadingState').classList.add('hidden');
                    }
                }

                function updateTransactionTable(transactions) {
                    const tableBody = document.getElementById('transactionsTable');
                    
                    if (transactions.length === 0) {
                        document.getElementById('emptyState').classList.remove('hidden');
                        tableBody.innerHTML = '';
                        return;
                    }

                    // Sort by timestamp descending (newest first)
                    transactions.sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp));

                    tableBody.innerHTML = transactions.map((transaction, index) => `
                        <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                            <td class="py-4">
                                <input type="checkbox" value="${index}" onchange="toggleTransaction(${index})" 
                                       class="transaction-checkbox">
                            </td>
                            <td class="py-4">
                                <div class="flex items-center">
                                    <span class="date-badge">${transaction.display_date}</span>
                                </div>
                            </td>
                            <td class="py-4">
                                <span class="px-2 py-1 bg-blue-100 text-blue-600 rounded-full text-xs font-medium">
                                    ${transaction.order_type}
                                </span>
                            </td>
                            <td class="py-4 font-semibold text-gray-800">
                                ${formatCurrency(transaction.total_order)}
                            </td>
                            <td class="py-4 text-red-600">
                                -${formatCurrency(transaction.commission)}
                            </td>
                            <td class="py-4 text-blue-600">
                                ${formatCurrency(transaction.net_income)}
                            </td>
                            <td class="py-4 text-green-600 font-semibold">
                                ${formatCurrency(transaction.usable_income)}
                            </td>
                        </tr>
                    `).join('');

                    document.getElementById('emptyState').classList.add('hidden');
                }

                function updateStatistics(analytics) {
                    document.getElementById('totalTransactions').textContent = 
                        analytics.summary.total_orders.toLocaleString();
                    document.getElementById('totalRevenue').textContent = 
                        formatCurrency(analytics.summary.total_revenue);
                    document.getElementById('totalNetIncome').textContent = 
                        formatCurrency(analytics.summary.total_net_income);
                    document.getElementById('avgOrderValue').textContent = 
                        formatCurrency(analytics.summary.avg_order_value);
                }

                function toggleSelectAll() {
                    const selectAll = document.getElementById('selectAll');
                    const checkboxes = document.querySelectorAll('.transaction-checkbox');
                    
                    checkboxes.forEach((checkbox, index) => {
                        checkbox.checked = selectAll.checked;
                        if (selectAll.checked) {
                            selectedTransactions.add(index);
                        } else {
                            selectedTransactions.delete(index);
                        }
                    });
                    
                    updateActionBar();
                }

                function toggleTransaction(index) {
                    if (selectedTransactions.has(index)) {
                        selectedTransactions.delete(index);
                    } else {
                        selectedTransactions.add(index);
                    }
                    updateActionBar();
                }

                function updateActionBar() {
                    const actionBar = document.getElementById('actionBar');
                    const selectedCount = document.getElementById('selectedCount');
                    const selectAll = document.getElementById('selectAll');
                    
                    if (selectedTransactions.size > 0) {
                        actionBar.classList.remove('hidden');
                        selectedCount.textContent = `${selectedTransactions.size} item terpilih`;
                    } else {
                        actionBar.classList.add('hidden');
                    }
                    
                    // Update select all checkbox
                    const checkboxes = document.querySelectorAll('.transaction-checkbox');
                    selectAll.checked = checkboxes.length > 0 && selectedTransactions.size === checkboxes.length;
                    selectAll.indeterminate = selectedTransactions.size > 0 && selectedTransactions.size < checkboxes.length;
                }

                async function deleteSelected() {
                    if (selectedTransactions.size === 0) return;
                    
                    if (!confirm(`Apakah Anda yakin ingin menghapus ${selectedTransactions.size} transaksi?`)) {
                        return;
                    }

                    try {
                        const indices = Array.from(selectedTransactions);
                        const response = await fetch('/api/delete-orders', {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json',
                            },
                            body: JSON.stringify({ indices: indices })
                        });

                        const result = await response.json();

                        if (result.success) {
                            showAlert(result.message, 'success');
                            selectedTransactions.clear();
                            await loadTransactionData(); // Reload data
                        } else {
                            showAlert(result.message, 'error');
                        }
                    } catch (error) {
                        console.error('Error deleting transactions:', error);
                        showAlert('Gagal menghapus transaksi', 'error');
                    }
                }

                function applyFilters() {
                    // Filter implementation would go here
                    // This would filter the allTransactions array based on date range and order type
                }

                function exportToCSV() {
                    // CSV export implementation would go here
                    showAlert('Fitur export CSV akan segera hadir!', 'info');
                }

                function refreshData() {
                    loadTransactionData();
                }

                // Load data on page load
                document.addEventListener('DOMContentLoaded', loadTransactionData);
            </script>
            '''
        )

    def create_targets_page(self):
        """Create targets management page"""
        return self.create_base_template(
            "Performance Targets",
            "targets",
            '''
            <div class="max-w-4xl mx-auto">
                <div class="glass-card rounded-2xl p-6 md:p-8">
                    <div class="text-center mb-8">
                        <h1 class="text-2xl md:text-3xl font-bold text-gray-800 mb-2">Target & Konfigurasi</h1>
                        <p class="text-gray-600">Atur target performa dan konfigurasi sistem</p>
                    </div>

                    <!-- Current Performance -->
                    <div class="mb-8">
                        <h2 class="text-xl font-bold text-gray-800 mb-4">Performance Summary</h2>
                        <div id="performanceSummary" class="grid grid-cols-1 md:grid-cols-3 gap-4">
                            <!-- Will be populated by JavaScript -->
                        </div>
                    </div>

                    <!-- Configuration Form -->
                    <form id="configForm" class="space-y-6">
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <!-- Daily Income Target -->
                            <div>
                                <label class="block text-sm font-medium text-gray-700 mb-2">
                                    <i class="fas fa-bullseye mr-2"></i>Target Pendapatan Harian
                                </label>
                                <div class="relative">
                                    <span class="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-500">Rp</span>
                                    <input 
                                        type="number" 
                                        id="targetDailyIncome"
                                        class="w-full pl-10 pr-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-purple-500 focus:border-transparent"
                                        placeholder="Masukkan target harian"
                                    >
                                </div>
                            </div>

                            <!-- Weekly Orders Target -->
                            <div>
                                <label class="block text-sm font-medium text-gray-700 mb-2">
                                    <i class="fas fa-chart-line mr-2"></i>Target Order Mingguan
                                </label>
                                <input 
                                    type="number" 
                                    id="targetWeeklyOrders"
                                    class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-purple-500 focus:border-transparent"
                                    placeholder="Masukkan target order mingguan"
                                >
                            </div>

                            <!-- Efficiency Threshold -->
                            <div>
                                <label class="block text-sm font-medium text-gray-700 mb-2">
                                    <i class="fas fa-tachometer-alt mr-2"></i>Batas Efisiensi (%)
                                </label>
                                <input 
                                    type="number" 
                                    id="efficiencyThreshold"
                                    min="0"
                                    max="100"
                                    step="1"
                                    class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-purple-500 focus:border-transparent"
                                    placeholder="Batas efisiensi minimum"
                                >
                            </div>

                            <!-- Company Name -->
                            <div>
                                <label class="block text-sm font-medium text-gray-700 mb-2">
                                    <i class="fas fa-building mr-2"></i>Nama Perusahaan
                                </label>
                                <input 
                                    type="text" 
                                    id="companyName"
                                    class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-purple-500 focus:border-transparent"
                                    placeholder="Nama perusahaan Anda"
                                >
                            </div>
                        </div>

                        <!-- Action Buttons -->
                        <div class="flex flex-col md:flex-row gap-4 pt-6">
                            <button 
                                type="button"
                                onclick="loadCurrentConfig()"
                                class="flex-1 px-6 py-3 bg-gray-600 text-white rounded-xl hover:bg-gray-700 transition-all duration-300 flex items-center justify-center"
                            >
                                <i class="fas fa-sync-alt mr-2"></i>Reset
                            </button>
                            <button 
                                type="submit"
                                class="flex-1 px-6 py-3 bg-gradient-to-r from-purple-600 to-blue-600 text-white rounded-xl hover:from-purple-700 hover:to-blue-700 transition-all duration-300 flex items-center justify-center"
                            >
                                <i class="fas fa-save mr-2"></i>Simpan Konfigurasi
                            </button>
                        </div>
                    </form>

                    <!-- System Information -->
                    <div class="mt-8 pt-6 border-t border-gray-200">
                        <h3 class="text-lg font-semibold text-gray-800 mb-4">Informasi Sistem</h3>
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <div class="bg-gray-50 rounded-xl p-4">
                                <h4 class="font-semibold text-gray-700 mb-2">Rates Default</h4>
                                <div class="space-y-2 text-sm">
                                    <div class="flex justify-between">
                                        <span>Komisi Maxim:</span>
                                        <span class="font-semibold">15%</span>
                                    </div>
                                    <div class="flex justify-between">
                                        <span>Tabungan Saldo:</span>
                                        <span class="font-semibold">10%</span>
                                    </div>
                                    <div class="flex justify-between">
                                        <span>Tabungan BBM:</span>
                                        <span class="font-semibold">10%</span>
                                    </div>
                                    <div class="flex justify-between">
                                        <span>Tabungan Oli:</span>
                                        <span class="font-semibold">10%</span>
                                    </div>
                                </div>
                            </div>
                            <div class="bg-gray-50 rounded-xl p-4">
                                <h4 class="font-semibold text-gray-700 mb-2">Status Sistem</h4>
                                <div class="space-y-2 text-sm">
                                    <div class="flex justify-between">
                                        <span>AI Analysis:</span>
                                        <span class="text-green-600 font-semibold">Active</span>
                                    </div>
                                    <div class="flex justify-between">
                                        <span>Data Storage:</span>
                                        <span class="text-green-600 font-semibold">CSV</span>
                                    </div>
                                    <div class="flex justify-between">
                                        <span>Real-time Updates:</span>
                                        <span class="text-green-600 font-semibold">Enabled</span>
                                    </div>
                                    <div class="flex justify-between">
                                        <span>Last Backup:</span>
                                        <span class="font-semibold">Just now</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <script>
                async function loadCurrentConfig() {
                    try {
                        const response = await fetch('/api/config');
                        const data = await response.json();
                        
                        if (data.success) {
                            const config = data.config;
                            const metrics = config.performance_metrics || {};
                            
                            // Fill form fields
                            document.getElementById('targetDailyIncome').value = metrics.target_daily_income || '';
                            document.getElementById('targetWeeklyOrders').value = metrics.target_weekly_orders || '';
                            document.getElementById('efficiencyThreshold').value = metrics.efficiency_threshold || '';
                            document.getElementById('companyName').value = config.company_name || '';
                            
                            showAlert('Konfigurasi berhasil dimuat', 'success');
                        }
                    } catch (error) {
                        console.error('Error loading config:', error);
                        showAlert('Gagal memuat konfigurasi', 'error');
                    }
                }

                async function updatePerformanceSummary() {
                    try {
                        const response = await fetch('/api/analytics');
                        const data = await response.json();
                        
                        if (data.success) {
                            const analytics = data.analytics;
                            const summary = analytics.summary;
                            
                            document.getElementById('performanceSummary').innerHTML = `
                                <div class="bg-blue-50 rounded-xl p-4 text-center">
                                    <p class="text-sm text-blue-600 mb-1">Efisiensi Saat Ini</p>
                                    <p class="text-2xl font-bold text-blue-700">${formatPercentage(summary.efficiency_ratio)}</p>
                                </div>
                                <div class="bg-green-50 rounded-xl p-4 text-center">
                                    <p class="text-sm text-green-600 mb-1">Score Performa</p>
                                    <p class="text-2xl font-bold text-green-700">${Math.round(summary.performance_score)}/100</p>
                                </div>
                                <div class="bg-purple-50 rounded-xl p-4 text-center">
                                    <p class="text-sm text-purple-600 mb-1">Avg Order Value</p>
                                    <p class="text-2xl font-bold text-purple-700">${formatCurrency(summary.avg_order_value)}</p>
                                </div>
                            `;
                        }
                    } catch (error) {
                        console.error('Error loading performance summary:', error);
                    }
                }

                // Form submission
                document.getElementById('configForm').addEventListener('submit', async function(e) {
                    e.preventDefault();
                    
                    const configData = {
                        performance_metrics: {
                            target_daily_income: parseInt(document.getElementById('targetDailyIncome').value) || 0,
                            target_weekly_orders: parseInt(document.getElementById('targetWeeklyOrders').value) || 0,
                            efficiency_threshold: parseFloat(document.getElementById('efficiencyThreshold').value) || 0
                        },
                        company_name: document.getElementById('companyName').value
                    };

                    try {
                        const response = await fetch('/api/update-config', {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json',
                            },
                            body: JSON.stringify(configData)
                        });

                        const result = await response.json();

                        if (result.success) {
                            showAlert(result.message, 'success');
                            updatePerformanceSummary();
                        } else {
                            showAlert(result.message, 'error');
                        }
                    } catch (error) {
                        console.error('Error updating config:', error);
                        showAlert('Gagal memperbarui konfigurasi', 'error');
                    }
                });

                // Load data on page load
                document.addEventListener('DOMContentLoaded', function() {
                    loadCurrentConfig();
                    updatePerformanceSummary();
                });
            </script>
            '''
        )
