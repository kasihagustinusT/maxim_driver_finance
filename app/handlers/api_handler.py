import json
import urllib.parse
from http.server import BaseHTTPRequestHandler
from datetime import datetime

# Gunakan absolute imports
import os
import sys
current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from app.services.finance_manager import ExpertFinanceManager
from app.utils.template_renderer import TemplateRenderer

class ExpertFinanceAPIHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, finance_manager=None, **kwargs):
        self.finance_manager = finance_manager or ExpertFinanceManager()
        self.template_renderer = TemplateRenderer(self.finance_manager)
        super().__init__(*args, **kwargs)


    def do_GET(self):
        """Handle GET requests"""
        try:
            parsed_path = urllib.parse.urlparse(self.path)
            path = parsed_path.path

            if path == '/' or path == '/dashboard':
                self.serve_dashboard()
            elif path == '/orders':
                self.serve_orders_page()
            elif path == '/history':
                self.serve_history_page()
            elif path == '/targets':
                self.serve_targets_page()
            elif path == '/api/data':
                self.serve_complete_data()
            elif path == '/api/analytics':
                self.serve_analytics()
            elif path == '/api/insights':
                self.serve_insights()
            elif path == '/api/config':
                self.serve_config()
            else:
                self.send_error(404, "Endpoint not found")
        except Exception as e:
            print(f"❌ Error in do_GET: {e}")
            self.send_error(500, f"Internal server error: {str(e)}")

    def do_POST(self):
        """Handle POST requests"""
        try:
            parsed_path = urllib.parse.urlparse(self.path)
            path = parsed_path.path

            if path == '/api/add-order':
                self.add_order()
            elif path == '/api/delete-orders':
                self.delete_orders()
            elif path == '/api/update-config':
                self.update_config()
            else:
                self.send_error(404, "Endpoint not found")
        except Exception as e:
            print(f"❌ Error in do_POST: {e}")
            self.send_error(500, f"Internal server error: {str(e)}")

    def serve_dashboard(self):
        """Serve the dashboard page"""
        try:
            html_content = self.template_renderer.create_dashboard_page()
            self.send_success_response(html_content, 'text/html')
        except Exception as e:
            self.send_error(500, f"Error generating dashboard: {str(e)}")

    def serve_orders_page(self):
        """Serve the orders management page"""
        try:
            html_content = self.template_renderer.create_orders_page()
            self.send_success_response(html_content, 'text/html')
        except Exception as e:
            self.send_error(500, f"Error generating orders page: {str(e)}")

    def serve_history_page(self):
        """Serve the transaction history page"""
        try:
            html_content = self.template_renderer.create_history_page()
            self.send_success_response(html_content, 'text/html')
        except Exception as e:
            self.send_error(500, f"Error generating history page: {str(e)}")

    def serve_targets_page(self):
        """Serve the targets management page"""
        try:
            html_content = self.template_renderer.create_targets_page()
            self.send_success_response(html_content, 'text/html')
        except Exception as e:
            self.send_error(500, f"Error generating targets page: {str(e)}")

    def serve_complete_data(self):
        """Serve complete data dengan analytics real-time"""
        try:
            data = self.finance_manager.get_all_data()
            analytics = self.finance_manager.get_real_time_analytics()
            insights = self.finance_manager.get_performance_insights()

            response = {
                "success": True,
                "transactions": data,
                "analytics": analytics,
                "insights": insights,
                "timestamp": datetime.now().isoformat()
            }

            self.send_json_response(response)
        except Exception as e:
            print(f"❌ Error serving complete data: {e}")
            self.send_error(500, f"Error serving data: {str(e)}")

    def serve_analytics(self):
        """Serve analytics data saja"""
        try:
            analytics = self.finance_manager.get_real_time_analytics()
            response = {
                "success": True,
                "analytics": analytics
            }
            self.send_json_response(response)
        except Exception as e:
            print(f"❌ Error serving analytics: {e}")
            self.send_error(500, f"Error serving analytics: {str(e)}")

    def serve_insights(self):
        """Serve performance insights"""
        try:
            insights = self.finance_manager.get_performance_insights()
            response = {
                "success": True,
                "insights": insights
            }
            self.send_json_response(response)
        except Exception as e:
            print(f"❌ Error serving insights: {e}")
            self.send_error(500, f"Error serving insights: {str(e)}")

    def serve_config(self):
        """Serve current configuration"""
        try:
            response = {
                "success": True,
                "config": self.finance_manager.config
            }
            self.send_json_response(response)
        except Exception as e:
            print(f"❌ Error serving config: {e}")
            self.send_error(500, f"Error serving config: {str(e)}")

    def add_order(self):
        """Handle adding new order"""
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))

            total_order = data.get('total_order')
            order_type = data.get('order_type', 'Regular')
            custom_date = data.get('custom_date')

            if total_order is None:
                self.send_error(400, "Total order is required")
                return

            try:
                total_order = float(total_order)
            except (ValueError, TypeError):
                self.send_error(400, "Total order must be a valid number")
                return

            if total_order < 1000:
                self.send_error(400, "Total order must be at least Rp 1,000")
                return

            result = self.finance_manager.add_order(total_order, order_type, custom_date)

            if result["success"]:
                self.send_json_response(result)
            else:
                self.send_json_response(result, 400)

        except Exception as e:
            print(f"❌ Error adding order: {e}")
            self.send_error(500, f"Error adding order: {str(e)}")

    def delete_orders(self):
        """Handle deleting orders"""
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))

            indices = data.get('indices', [])

            if not indices:
                self.send_error(400, "No indices provided")
                return

            result = self.finance_manager.delete_orders(indices)

            if result["success"]:
                self.send_json_response(result)
            else:
                self.send_json_response(result, 400)

        except Exception as e:
            print(f"❌ Error deleting orders: {e}")
            self.send_error(500, f"Error deleting orders: {str(e)}")

    def update_config(self):
        """Handle updating configuration"""
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))

            result = self.finance_manager.update_config(data)

            if result["success"]:
                self.send_json_response(result)
            else:
                self.send_json_response(result, 400)

        except Exception as e:
            print(f"❌ Error updating config: {e}")
            self.send_error(500, f"Error updating config: {str(e)}")

    def send_success_response(self, content: str, content_type: str = 'text/html'):
        """Send successful response"""
        self.send_response(200)
        self.send_header('Content-type', f'{content_type}; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode('utf-8'))

    def send_json_response(self, data: dict, status_code: int = 200):
        """Send JSON response"""
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=False).encode('utf-8'))
