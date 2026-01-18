
special = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"

def is_password_secure(password):
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char in special for char in password):
        return False
    return True

print(is_password_secure("10 I Want To Hold Your Hand"))

# while True:
#     password = input('Enter your password: ')
#     if is_password_secure(password):
#         print('W password.')
#         break
#     else:
#         print('L password.')