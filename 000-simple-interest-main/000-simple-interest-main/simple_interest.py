def calculate_simple_interest(principal: float, rate: float, time: float) -> float:
    try:
        principal = float(principal)
        rate = float(rate)
        time = float(time)
        
        if principal < 0 or rate < 0 or time < 0:
            raise ValueError("All values must be positive numbers")
            
        interest = (principal * rate * time) / 100
        return round(interest, 2)
        
    except ValueError as e:
        if str(e) == "All values must be positive numbers":
            raise
        raise ValueError("Invalid input: Please enter valid numbers only")

if __name__ == "__main__":
    principal = 5000  # Starting with R5000
    rate = 5         # 5% interest rate
    time = 2         # For 2 years
    
    interest = calculate_simple_interest(principal, rate, time)
    print(f"If you invest R{principal} for {time} years at {rate}% interest:")
    print(f"You will earn R{interest} in interest")

