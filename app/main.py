#!/usr/bin/env python3
"""
Maxim Finance AI - Simplified for Railway
"""

import os
import sys
from http.server import HTTPServer

# Import modules
from handlers.api_handler import ExpertFinanceAPIHandler
from services.finance_manager import ExpertFinanceManager

if __name__ == "__main__":
    finance_manager = ExpertFinanceManager()
    
    def handler(*args):
        ExpertFinanceAPIHandler(*args, finance_manager=finance_manager)
    
    port = int(os.getenv('PORT', 8000))
    host = os.getenv('HOST', '0.0.0.0')
    
    server = HTTPServer((host, port), handler)
    
    print(f"🚀 Maxim Finance AI Started on {host}:{port}")
    print("📊 Dashboard available at: /dashboard")
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped")
