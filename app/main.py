import webbrowser
from http.server import HTTPServer

from .handlers.api_handler import ExpertFinanceAPIHandler
from .services.finance_manager import ExpertFinanceManager

def main():
    """Main function to start the AI-powered server"""
    finance_manager = ExpertFinanceManager()
    
    def handler(*args):
        ExpertFinanceAPIHandler(*args, finance_manager=finance_manager)
    
    port = 8000
    server = HTTPServer(('localhost', port), handler)
    
    print(f"\n🚀 Maxim Finance AI System Started!")
    print(f"📍 Server running at: http://localhost:{port}/dashboard")
    print("\n🏗️  Professional Architecture:")
    print("   • Models: FinancialRecord, AnalyticsData")
    print("   • Services: FinanceManager, AIAdvisor, DataHandler")
    print("   • Handlers: APIHandler, TemplateRenderer")
    print("   • Utils: Config, Helpers")
    print("\n📊 Features:")
    print("   • Real-time Analytics & Visualizations")
    print("   • AI-powered Insights")
    print("   • Professional UI/UX")
    print("   • Mobile Responsive Design")
    print("\n🎯 Built by: Kasih")
    print("⏹️  Press Ctrl+C to stop the server\n")
    
    try:
        webbrowser.open(f'http://localhost:{port}/dashboard')
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 AI Finance server stopped.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
