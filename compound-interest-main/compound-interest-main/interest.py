import re
import datetime
from typing import Union

def simulate(opening_balance: float, rate: str, time: datetime.timedelta,) -> float:
    """Calculate the future value of an investment with compound interest.
    
    Args:
        opening_balance: Initial amount of money invested
        rate: Interest rate specification (e.g., "10% annually" or "1% monthly")
        time: Duration of the investment as a timedelta
    
    Returns:
        The final balance after applying compound interest
    
    Raises:
        ValueError: If the rate format is invalid"""
    
    rate_match = re.match(r"^(\d+\.?\d*)%\s+(annually|monthly)$", rate.strip().lower())
    if not rate_match:
        raise ValueError(f"Invalid rate format: {rate}. Expected format like '10% annually' or '1% monthly'")
    
    percentage = float(rate_match.group(1))
    period = rate_match.group(2)
    decimal_rate = percentage / 100
    
    if period == "monthly":
        months = time.days / 30
        final_balance = opening_balance * (1 + decimal_rate) ** months
    else:
        years = time.days / 360
        final_balance = opening_balance * (1 + decimal_rate) ** years
    
    return final_balance