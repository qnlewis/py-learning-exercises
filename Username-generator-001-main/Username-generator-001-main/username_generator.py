def user_details():
    
    firstname = input("Enter your first name: ")
    lastname = input("Enter your last name: ")
    year = input("Enter your cohort year: ")
    campus = input("Enter your campus: ")
    return firstname, lastname, year, campus



def create_user_name(firstname, lastname, year, campus):
    
    campus_actual = {
        "Durban": "DBN",
        "Johannesburg": "JHB",
        "Cape Town": "CPT"
    }

    if campus not in campus_actual:
        raise ValueError("Invalid campus or no capitalization.")

    first_part = (firstname[-3:] if len(firstname) >= 3 else firstname + 'O' * (3 - len(firstname))).upper()
    last_part = (lastname[:3] if len(lastname) >= 3 else lastname + 'O' * (3 - len(lastname))).upper()
    campus_part = campus_actual[campus]
    username = f"{first_part}{last_part}{campus_part}{year}"
    return username

def user_campus():
    
    campus = input("Enter your campus: ")
    return campus

def main():
    firstname, lastname, year, campus = user_details()

    if not firstname.isalpha() or not lastname.isalpha():
        print("First name and last name should not contain digits.")
        return
    
    try:
        year = int(year)
        if year < 2025:
            print("Cohort year should be a valid cohort year.")
            return
    except ValueError:
        print("Cohort year should be a number.")
        return
    
    try:
        username = create_user_name(firstname, lastname, str(year), campus)
        print(f"Generated Username: {username}")
        confirmation = input("Is the username correct? (yes/no): ")
        if confirmation.lower() == 'yes' or confirmation.lower() == 'y':
            print("Username confirmed.")
        elif confirmation.lower() == 'no' or confirmation.lower() == 'n':
            print("Please restart the process to generate a new username.")
        else:
            print("Please restart the process to generate a new username.")
    except ValueError:
        print("Invalid")

if __name__ == "__main__":
    main()
    pass