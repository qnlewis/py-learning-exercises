def change(amount_due, amount_paid):
    values = sorted([20000, 10000, 5000, 2000, 1000, 500, 200,
                    100, 50, 20, 10, 5, 2, 1,
                    0.5, 0.2, 0.1, 0.05, 0.02, 0.01], reverse=True)
    
    change_amount = amount_paid - amount_due
    curated_result = {}
    
    for value in values:
        if change_amount >= value:
            count = int(change_amount // value)
            curated_result[value] = count
            change_amount -= value * count
            change_amount = round(change_amount, 2)
            
    return curated_result

if __name__ == '__main__':
    print(change(100, 200))