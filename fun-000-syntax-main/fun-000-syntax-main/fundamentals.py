#Question 1
def get_date_of_birth(id_number:str): 
    """STEP 2: Extract the date of birth from the ID number and return it as a string
    return format: DD/MM/YY"""
    day = id_number[4:6]
    month = id_number[2:4]
    year = id_number[0:2]
    return f"{day}/{month}/{year}"

#Question 2    
def get_gender(id_number):
    """STEP 3: Extract the gender from the ID number using the formula below and return
    it as a string"""
    gender = int(id_number[6:10])
    if gender > 4999:
        return 'Male'
    else:
        return 'Female'

#Question 3
def get_citizenship(id_number):
    """STEP 4: Extract the citizenship from the ID number using the formula below and 
    return it as a string"""
    citizenship = int(id_number[10:11])
    if citizenship < 1:
        return 'South African'
    else:
        return 'Non-South African'

#Question 4
def fizzbuzz(a):
    for i in range(1, a + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

#Question 5
def check_number(n: int):
    """Check a number and return appropriate message based on conditions"""
    if n == 0:
        return 'Neutral'
    elif n < 0:
        return 'Extremely Weird' if n % 2 != 0 else 'Very weird'
    elif n % 2 != 0:
        return 'Weird'
    elif 2 <= n <= 5:
        return 'Not Weird'
    elif 6 <= n <= 20:
        return 'Weird'
    else:
        return 'Not Weird'
