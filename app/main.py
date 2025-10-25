#!/usr/bin/env python3
"""
Maxim Finance AI System - Main Application
"""

import os
import sys
from http.server import HTTPServer

# ABSOLUTE IMPORTS - tambahkan path ke sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

# Sekarang gunakan absolute imports
from app.handlers.api_handler import ExpertFinanceAPIHandler
from app.services.finance_manager import ExpertFinanceManager

def main():
    """Main function"""
    finance_manager = ExpertFinanceManager()
    
    def handler(*args):
        ExpertFinanceAPIHandler(*args, finance_manager=finance_manager)
    
    port = int(os.getenv('PORT', 8000))
    host = os.getenv('HOST', '0.0.0.0')
    
    server = HTTPServer((host, port), handler)
    
    print(f"\n🚀 Maxim Finance AI System Started!")
    print(f"📍 Server running at: http://{host}:{port}")
    print("\n📊 Features:")
    print("   • Real-time Analytics & Visualizations")
    print("   • AI-powered Insights") 
    print("   • Professional UI/UX")
    print("   • Mobile Responsive Design")
    print("\n🎯 Built by: Kasih")
    print("⏹️  Press Ctrl+C to stop the server\n")
    
    try:
        # Di production, jangan buka browser
        if os.getenv('RAILWAY_ENVIRONMENT') is None:
            import webbrowser
            webbrowser.open(f'http://localhost:{port}/dashboard')
        
        print(f"✅ Server ready!")
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 AI Finance server stopped.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
