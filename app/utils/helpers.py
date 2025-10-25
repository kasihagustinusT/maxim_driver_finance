def format_currency(amount: float) -> str:
    """Format currency to Indonesian Rupiah"""
    return 'Rp ' + format(int(amount), ',d').replace(',', '.')

def format_percentage(value: float) -> str:
    """Format percentage value"""
    return f"{value:.1f}%"

def validate_date(date_string: str) -> bool:
    """Validate date string in YYYY-MM-DD format"""
    from datetime import datetime
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def clean_numeric_input(value: str) -> float:
    """Clean and convert numeric input"""
    if not value:
        return 0.0
    
    cleaned = ''.join(ch for ch in str(value) if ch.isdigit() or ch == '.' or ch == '-')
    
    if not cleaned or cleaned == '-' or cleaned == '.':
        return 0.0
        
    try:
        return float(cleaned)
    except (ValueError, TypeError):
        return 0.0
